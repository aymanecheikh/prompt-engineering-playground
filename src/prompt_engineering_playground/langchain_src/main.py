from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

load_dotenv()

llm_openai = ChatOpenAI(model="gpt-5.2-pro")
response_openai = llm_openai.invoke(
  "This is my first OpenAI prompt via LangChain"
)

print(response_openai)