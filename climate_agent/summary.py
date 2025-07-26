from climate_agent.vector_store import load_vector_store

vector_store = load_vector_store() # Load the vector store


if vector_store is None:
    raise ValueError("Vector store could not be loaded. Ensure it exists or create it first.")

# Importing the Groq LLM key
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_KEY")

from langchain_groq import ChatGroq
# LLM Initialization
llm = ChatGroq(
    model_name="llama3-8b-8192",
    groq_api_key=GROQ_API_KEY,
    temperature=0  # Set to 0 for factual, retrieval-based answers
)

SUMMARY_PROMPT_TEMPLATE = """
You are an AI assistant. Given the following context, summarize it in a clear and concise paragraph:

Context:
{context}

Summary:
"""

# the prompt template for summarization

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

summary_prompt = PromptTemplate.from_template(SUMMARY_PROMPT_TEMPLATE)


def generate_summary_from_store():
    if vector_store is None:
        raise ValueError("Vector store is not loaded. Cannot generate summary.")
    
    
    docs = vector_store.similarity_search("Climate change", k=5)
    context = "\n".join([doc.page_content for doc in docs])

    summary_chain = RunnableSequence(
        summary_prompt | llm
    )       

    summary = summary_chain.invoke({"context": context})
    return summary
