import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# --- 1. Load Environment Variables ---
# This securely loads the API key from your .env file.
load_dotenv()
groq_api_key = os.getenv("GROK_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found. Make sure it's in your .env file.")

print("✅ Groq API Key loaded successfully.")

try:
    # --- 2. Initialize the Groq LLM ---
    # We are creating an instance of the LLM, specifying the model we want to use.
    # 'llama3-8b-8192' is a great, fast choice.
    # temperature=0 makes the model's answers more predictable and less "creative".
    llm = ChatGroq(
        model_name="llama3-8b-8192",
        groq_api_key=groq_api_key,
        temperature=0
    )
    print("✅ Groq LLM initialized successfully.")
    print("🚀 Attempting to invoke the model...")

    # --- 3. Prepare the Prompt ---
    # Modern LLMs work best with a "chat" format. We give it a system instruction
    # and then the user's question.
    messages = [
        SystemMessage(content="You are a helpful science expert who explains complex topics clearly and concisely."),
        HumanMessage(content="What is climate change?"),
    ]

    # --- 4. Invoke the LLM and Get the Response ---
    response = llm.invoke(messages)

    print("\n--- SUCCESS ---")
    # The actual text from the model is stored in the 'content' attribute.
    print(f"Response from Groq: \n\n{response.content}")

except Exception as e:
    print("\n--- FAILED ---")
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()