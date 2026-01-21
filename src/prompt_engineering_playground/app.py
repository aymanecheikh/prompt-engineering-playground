from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

with open("src/prompt_engineering_playground/prompts/fallen_angel.md", 'r', encoding="utf-8") as f:
  instructions = f.read()

response = client.responses.create(
  model="gpt-5.2-pro",
  instructions=instructions,
  input= "My entirely family was killed simply because of who we are. I've spent my life since then surviving and adapting. Over time, I found my craft and built on it. I have tasted success. I am richer than I have ever been. But no matter how hard I try... no matter how much I achieve, I am never accepted by these people. Even in a society based entirely on merit, my merit seems to be inherently less valuable. It angers me to the core, but I will never let it defeat me. I must keep going. Where do I go from here?"
)

print(response.output_text)