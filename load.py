import chromadb
import tqdm
import pandas as pd

# Source : https://www.data.gouv.fr/fr/datasets/catalogue-des-donnees-de-data-gouv-fr/
CSV_FILE = 'export-dataset-20230828-054744.csv.gz'
CHROMA_PATH = "data-test"

# Uncomment to generate the pickle file
df = pd.read_csv(CSV_FILE, sep=';', encoding='utf-8')
df['description'] = df['description'].astype(str)
df['title'] = df['title'].astype(str)

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.create_collection(name="data_gouv_datasets")


def add_row(collection, row):
    collection.add(
        documents=[row['title'] + ' - ' + row['description']],
        metadatas=[row],
        ids=[row['id']]
    )

for index, row in tqdm.tqdm(df.iterrows(), total=df.shape[0]):
    row_dict = row.to_dict()
    add_row(collection, row_dict)
    break
