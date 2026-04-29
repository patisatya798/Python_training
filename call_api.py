import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
Question = input("Enter the city name")

completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",  
    messages=[
        {
            "role": "user",
            "content": Question
        }
    ],
    temperature=1,
    max_completion_tokens=512,
    top_p=1,
    stream=True
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")