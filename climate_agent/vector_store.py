import os
# from langchain.vectorstores import Chroma


from langchain_community.vectorstores import Chroma
# Importing the load and chunk functions
from climate_agent.embedder import load_and_chunk_documents, embed_chunks

# Importing for the saving of Urls function
from climate_agent.ingest import ingest_documents

# Import Embeddings
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv  

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Create the embeddings object
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-mpnet-base-v2",        
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
)   

#   define the vector store STORAGE PLACE

PERSIST_DIR = "data/vector_store"

def create_and_save_vector_store():
    """Creates and saves the vector store."""
    # Load and chunk documents
    chunks = load_and_chunk_documents()

    # Get raw text from chunks
    texts = [chunk.page_content for chunk in chunks]

    # Embed the text chunks
    vectors = embed_chunks(texts)

    # Create a vector store
    vector_store = Chroma.from_texts(texts, embeddings, persist_directory=PERSIST_DIR)

    # Save the vector store
    vector_store.persist()
    print(f"[📦] Vector store saved at: {PERSIST_DIR}")

    return vector_store

def load_vector_store():
    """Loads the vector store."""
    if not os.path.exists(PERSIST_DIR):
        print(f"[⚠️] Vector store directory does not exist: {PERSIST_DIR}")
        return None

    vector_store = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
    print(f"[📂] Loaded vector store from: {PERSIST_DIR}")

    return vector_store


def ingest_and_process(urls = None):
    """Ingests documents and creates the vector store."""
    print("[🔄] Starting ingestion and vector store creation...")

    # Create and save the vector store
    ingest_documents(urls)
    print("[📥] Documents ingested successfully.")
    vector_store = create_and_save_vector_store()

    if vector_store:
        print("[✅] Vector store created and saved successfully.")
    else:
        print("[❌] Failed to create vector store.")

    return {"status": "success", "message": "Vector store created and saved successfully."}
