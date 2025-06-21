## Vector Databases

A vector database is a specialized type of database designed to store, index, and search high-dimensional vector embeddings which are typically used in AI, machine learning, and search applications. Vector databases enable semantic search by comparing how _close_ two items are in embedding (vector) space, not based on keyword matching alone , but also based on semantics or meaning of the words.

This repository contains code built on use cases in the course: Deeplearning.ai – [Building Applications with Vector Databases](https://learn.deeplearning.ai/courses/building-applications-vector-databases/lesson/la6ct/semantic-search)

The code has been initially deployed on Hugging Face Spaces. Application Links below-

####  [Semantic Search Gradio App  on Hugging Face](https://huggingface.co/spaces/Maitreyee22/semanticsearch)

Individual links are also present in respective READMEs in the folders.

Have fun!

### Text Embeddings

Text embeddings are numerical representations of text (words, sentences, or entire documents) that capture their semantic meaning that could be used by machine learning models. Machines don’t understand natural languages. They understand numbers. So, embeddings convert natural language into a dense vector of numbers, where the position and direction of the vector encodes meaning. Words with similar meanings end up with similar vectors (i.e., close in the embedding space).

Example: King and Queen are semantically similar and are closer in the vector space.
![image](https://github.com/user-attachments/assets/1bea1cac-229b-49b1-9263-e70021af7622)

Source: ChatGPT
![image](https://github.com/user-attachments/assets/b17468ad-5b6b-4c88-a2f7-fc098b5f82d7)


Source: ChatGPT


### Pinecone

Pinecone is a vector database designed specifically for semantic search and other applications involving high-dimensional embeddings like those from NLP, computer vision, and recommendation systems. Pinecone stores, indexes, and retrieves vector representations (like text embeddings) efficiently by using Fast similarity search, Scalable and real-time querying and its integration with machine learning pipelines. Pinecone retrieves the most similar vectors from its index using approximate nearest neighbor (ANN) algorithms.

Pinecone works as follows:


![image](https://github.com/user-attachments/assets/ad5a9d25-4581-4945-977b-cb74c26dbe14)


Source: ChatGPT

