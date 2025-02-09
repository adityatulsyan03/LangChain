from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load .env file

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

result = llm.invoke("What is the current time in India?")

print(result)