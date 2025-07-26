import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA

# --- 1. CHANGE YOUR IMPORTS ---
# REMOVE the HuggingFaceEndpoint import
# from langchain_huggingface import HuggingFaceEndpoint 
# ADD the ChatGroq import
from langchain_groq import ChatGroq

from climate_agent.vector_store import load_vector_store

# Load environment variables
load_dotenv()

# --- 2. INITIALIZE THE GROQ LLM ---
# Get the Groq API key from your .env file
GROQ_API_KEY = os.getenv("GROQ_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file.")

# Create the LLM instance using ChatGroq.
# This replaces all your old HuggingFaceEndpoint code.
llm = ChatGroq(
    model_name="llama3-8b-8192",
    groq_api_key=GROQ_API_KEY,
    temperature=0  # Set to 0 for factual, retrieval-based answers
)


# --- 3. NO CHANGES NEEDED BELOW THIS LINE ---
# The rest of your architecture works perfectly with the new llm object.

print("✅ Vector store and Groq LLM loaded successfully.")

# Load the vector store
vector_store = load_vector_store()
if vector_store is None:
    raise ValueError("Vector store could not be loaded. Ensure it exists or create it first.")

retriever = vector_store.as_retriever(search_kwargs={"k": 5})

# Set up the QA Chain
# We pass our new 'llm' object right into the chain.
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
)

# Main function
def ask_question(question: str):
    print(f"[❓] Question received: {question}")
    
    # The .invoke() method works identically.
    response = qa_chain.invoke({"query": question})
    
    return {
        "question": question,
        "answer": response["result"],
        "sources": [doc.metadata.get("source", "unknown") for doc in response["source_documents"]]
    }