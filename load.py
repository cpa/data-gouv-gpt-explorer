import chromadb
import tqdm
import pandas as pd

from chromadb.utils import embedding_functions

# Source : https://www.data.gouv.fr/fr/datasets/catalogue-des-donnees-de-data-gouv-fr/
CSV_FILE = 'export-dataset-20230828-054744.csv.gz'
CHROMA_PATH = "data-big"

df = pd.read_csv(CSV_FILE, sep=';', encoding='utf-8')
df['description'] = df['description'].astype(str)
df['title'] = df['title'].astype(str)

emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-mpnet-base-v2")

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.create_collection(name="data_gouv_datasets", embedding_function=emb_fn)


def add_row(collection, row):
    collection.add(
        documents=[row['title'] + ' - ' + row['description']],
        metadatas=[row],
        ids=[row['id']]
    )

for index, row in tqdm.tqdm(df.iterrows(), total=df.shape[0]):
    row_dict = row.to_dict()
    add_row(collection, row_dict)
