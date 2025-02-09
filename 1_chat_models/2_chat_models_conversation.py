from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load .env file

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

messages = [
    SystemMessage("You are an expert in social media content strategy"), 
    HumanMessage("Give a short tip to create engaging posts on Instagram"), 
]

result = llm.invoke(messages)

print(result.content)