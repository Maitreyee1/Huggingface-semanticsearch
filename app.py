from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import os
from openai import OpenAI  # or your preferred client
from pinecone import Pinecone, ServerlessSpec
import gradio as gr
import json
from tqdm.auto import tqdm

#Setup API Keys
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)  # or openai.api_key = api_key
papi_key = os.getenv("PINECONE_API_KEY")
environment = os.getenv("PINECONE_ENVIRONMENT")

#Load dataset and consolidate questions from the dataset into a single list. 
dataset = load_dataset('quora', trust_remote_code=True, split='train[240000:290000]')
questions = []
for record in dataset['questions']:
    questions.extend(record['text'])
question = list(set(questions))

#Load the model- Sentence Transformers for CPU. 
model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

#Initialize Pinecone singleton object with API keys and set an index name.
pc = Pinecone(api_key=papi_key)
INDEX_NAME = 'semanticsearch'

#Delete any existing indices
if INDEX_NAME in [index.name for index in pc.list_indexes()]:
    pc.delete_index(INDEX_NAME)

#Create a new index for the dataset with shape of the embeddings, cosine similarity, and setup Serverless index with AWS. 
pc.create_index(name=INDEX_NAME, 
    dimension=model.get_sentence_embedding_dimension(), 
    metric='cosine',
    spec=ServerlessSpec(cloud='aws', region='us-east-1'))
index = pc.Index(INDEX_NAME)


batch_size=200
vector_limit=80000
questions = question[:vector_limit]


for i in tqdm(range(0, len(questions), batch_size)):
    # find end of batch
    i_end = min(i+batch_size, len(questions))
    # create IDs batch of vectors.
    ids = [str(x) for x in range(i, i_end)]
    # create metadata batch
    metadatas = [{'text': text} for text in questions[i:i_end]]
    # create vector embeddings that creates a tuple of ID, Vector Embedding, and Metadata associated with it.
    xc = model.encode(questions[i:i_end])
    # create records list for upsert
    records = zip(ids, xc, metadatas)
    # upsert to Pinecone
    index.upsert(vectors=records)


def run_query(query):
    #Build Vector Embedding of the user query. 
    embedding = model.encode(query).tolist()
    #Run the query against Pinecone
    results = index.query(top_k=5, vector=embedding, include_metadata=True, include_values=False)
    answers= []
    for result in results['matches']:
        answers.append([round(result['score'], 2), result['metadata']['text']])  
    return "\n".join(f"Similarity percentage: {score * 100:.2f} % , {text}" for score, text in answers)


# Create the Gradio interface
demo = gr.Interface(fn=run_query, inputs=gr.Textbox(label="User Input", placeholder="Type your question here..."), outputs=gr.Textbox(label="Matching Questions from Vector Database"))

# Launch the app
demo.launch(share=True)