import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key= os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key is not found")

client = Groq(api_key=my_api_key)
model= "llama-3.3-70b-versatile"
role="user"
prompt="Suggesst a 10 names in a list order for my company for tutorials where students will learn programming React, javascript, DSA, AL/ML stuff"

message_system = {
    "role":"system",
    "content":"You are my brand manager who suggest the name of my company. Name should be in one world"
}

message={
    "role": role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, temperature=2)
print(response.choices[0].message.content);
# print(response.to_json())