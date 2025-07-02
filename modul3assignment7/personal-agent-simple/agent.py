# agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories.sql import SQLChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.chains import ConversationChain
from langchain.chains import LLMMathChain
from langchain.tools import Tool
from tools import TOOLS
from dotenv import load_dotenv

import os

# Load environment variables from .env file
load_dotenv()

# === Setup API Key ===
# Load API key from .env file
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("⚠️  Error: GOOGLE_API_KEY not found!")
    print("Please make sure you have a .env file with your Gemini API key:")
    print("GOOGLE_API_KEY=your_actual_api_key_here")
    print("You can get an API key from: https://makersuite.google.com/app/apikey")
    exit(1)

print("✅ API key loaded successfully from .env file")

# === Setup LLM ===
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

# === Setup Memory with SQLite ===
history = SQLChatMessageHistory(session_id="default", connection="sqlite:///memory.db")
memory = ConversationBufferMemory(
    chat_memory=history,
    memory_key="chat_history", 
    return_messages=True
)

# === Define Agent ===
agent = initialize_agent(
    tools=TOOLS,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# === Simple Agent Loop ===
print("🧠 Personal Assistant Agent (type 'exit' to quit)")
print("Try: 'hello aya', 'what time is it', or any other question!")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break

    try:
        response = agent.invoke({"input": user_input})
        print(f"Agent: {response['output']}")
    except Exception as e:
        print(f"Error: {e}")
        print("Please try again.")
