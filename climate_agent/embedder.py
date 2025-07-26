import os
from langchain_community.document_loaders import WebBaseLoader , TextLoader
from climate_agent.config import RAW_DATA_PATH

# To split the loaded documents 
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Importing the embeddings
from langchain_huggingface import HuggingFaceEndpointEmbeddings


from dotenv import load_dotenv
load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print("Your API key is:", HUGGINGFACE_API_KEY[:10], "..." if HUGGINGFACE_API_KEY else "❌ Not set")

## CREATE THE EMBEDDING OBJECT
# New:
# embeddings = HuggingFaceEndpointEmbeddings(
#     model="sentence-transformers/all-mpnet-base-v2",
#     huggingfacehub_api_token=HUGGINGFACE_API_KEY,
# )

from langchain_huggingface import HuggingFaceEndpointEmbeddings

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-mpnet-base-v2",        
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
)


def load_and_chunk_documents(folder_path="data/raw" ):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") and not filename.endswith("_meta.txt"):
            loader = TextLoader(os.path.join(folder_path, filename), encoding="utf-8")
            docs = loader.load()
            documents.extend(docs)

            

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    print(f"[🔪] Split into {len(chunks)} chunks.")
    return chunks

def embed_chunks(documents):
    """Embeds the documents using the HuggingFace embeddings."""
    if not documents:
        print("[⚠️] No documents to embed.")
        return []

    print(f"[🔗] Embedding {len(documents)} documents...")
    embedded_docs = embeddings.embed_documents(documents)
    print(f"[✅] Embedded {len(embedded_docs)} documents.")

    return embedded_docs