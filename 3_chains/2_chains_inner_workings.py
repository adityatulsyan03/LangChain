from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda,RunnableSequence

# Load environment variables from .env
load_dotenv()

# Create a Gemini model
model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You love facts and you tell facts about {animal}"),
        ("human","Tell me {count} facts.")
    ]
)

format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_promt = RunnableLambda(lambda x: model.invoke(x.to_messages()))
prase_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt,middle=[invoke_promt],last=prase_output)

result = chain.invoke({"animal":"cats","count":3})

print(result)