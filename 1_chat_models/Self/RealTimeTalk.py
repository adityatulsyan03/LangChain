from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
messages = []

def set_role():
    role = input("What role do you want the AI to play: ")
    line = f"You are an expert in {role}"  # using f-string for clarity
    messages.append(SystemMessage(line))
    
def add_problem():
    problem = input("Enter your Problem: ")
    messages.append(HumanMessage(problem))

def get_ai_response():
    # If the last message is from the AI, ask for a rephrasing
    if messages and isinstance(messages[-1], AIMessage):
        messages.append(HumanMessage("Tell the last response in a different way"))
    result = llm.invoke(messages)
    messages.append(AIMessage(result.content))
    print("The AI Response is:")
    print(result.content)

def print_messages():
    for message in messages:
        instance_name = type(message).__name__
        print(f"{instance_name}: {message.content}")

print("Start...")
options = {
    0: set_role,
    1: add_problem,
    2: get_ai_response,
    3: print_messages
}

while True:
    try:
        option = int(input("Enter the Option (any other number to exit): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    
    # If option is not defined in our options dict, exit the loop.
    if option not in options:
        break
    
    # Call the corresponding function
    options[option]()

print("THE END...")