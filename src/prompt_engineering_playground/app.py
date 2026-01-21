from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
  model="gpt-5.2-pro",
  input= [
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text":"You are a fallen angel"
        },
        {
          "type": "input_text",
          "text":"Respond in only one sentence"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "What happened to you?"
        }
      ]
    }
  ]
)

print(response.output_text)