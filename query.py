import tqdm
import pandas as pd
import chromadb


CHROMA_PATH = "data"

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(name="data_gouv_datasets")

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
