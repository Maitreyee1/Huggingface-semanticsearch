The code is hosted on a Hugging Face Spaces- Gradio App with text inputs and outputs. Here is the link to the app!

####  [Semantic Search Gradio App  on Hugging Face](https://huggingface.co/spaces/Maitreyee22/semanticsearch)

Here is a sample output:
![Hugging Face App](https://github.com/user-attachments/assets/7971379f-9f1b-4a4d-9c90-e8c10d7e73fa)

The code is organized in two files - 
- app.py - Gradio application with the main code.
- requirements.txt - Set of libraries imported and used in the code that need to be specified for installation and loading during deployment on HuggingFace Spaces.

Note: The app runs on CPU free tier, hence has limitations with accuracy of the results. Higher computation power can improve results by providing larger datasets for training. 

Following are some concepts related to the implementation of the application. 

# Semantic Search

Semantic Search is a method of search that is focused on the meaning of the words or sentences in comparison to keyword search on the exact match of keywords.

![image](https://github.com/user-attachments/assets/d0a3e830-6ea4-4dd7-b83b-a120dbab1ef8)

Source: ChatGPT

![image](https://github.com/user-attachments/assets/edf9210e-42e1-4d3a-b105-2d15044b447c)

Source: ChatGPT

![image](https://github.com/user-attachments/assets/bb630d27-14b6-459c-a535-1358fc410615)

Source: Deeplearning.ai – Building Applications with Vector Databases

## How Semantic Search works

- Conversion of natural language data like documents and fetching queries into vector representation or embeddings.

- Application of similarity metrics like cosine similarity to compare vectors for semantic similarity.

- Output results for vectors that are similar in meaning. 

## Using Vector Database-Pinecone for Semantic Search

In this application, the Pinecone vector database is used to build a semantic search application for question similarity. The user can input a question and the model returns similar questions asked on Quora. The API keys are set as Secrets in the Spaces Settings-> Variables and Secrets. 

 1. Import a subset of the Quora database, and convert it into embeddings using
    SentenceTransformers.
  
 2. Pinecone API key is set, an index is created in Pinecone and the
    embeddings are stored in Pinecone.
    
 3. User input for a question is encoded and converted into the vector for
    comparison.
        
 4. Query the subset of the Quora database that is converted and stored as embeddings in Pinecone.
    
 5. Based on cosine similarity, similar questions from the database are matched.
 Here is the mathematical formula how cosine similarity is calculated for two vectors: 
![image](https://github.com/user-attachments/assets/ff8d86b9-aa8e-48d1-9db7-36c8c7228204)


[Source](https://www.google.com/url?sa=i&url=https%3A%2F%2Ftowardsdatascience.com%2Fcosine-similarity-how-does-it-measure-the-similarity-maths-behind-and-usage-in-python-50ad30aad7db%2F&psig=AOvVaw370oMkE5xhZcwxgWVSJDux&ust=1750570086889000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCNDI5vTjgY4DFQAAAAAdAAAAABAE)
 
 7. Return results for semantic similarity with similarity percentage
    and questions matched based on the user input query.
