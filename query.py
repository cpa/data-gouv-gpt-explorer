import tqdm
import pandas as pd
import chromadb

from chromadb.utils import embedding_functions

CHROMA_PATH = "data-big"

emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-mpnet-base-v2")

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(name="data_gouv_datasets", embedding_function=emb_fn)

q = input("Recherche : ")

results = collection.query(
    query_texts=[q], # Add your query here
    n_results=10
)

for row in results['metadatas'][0]:
    print(row['title'])
    print(row['description'])
    print(row['url'])
    print("=======================================")
