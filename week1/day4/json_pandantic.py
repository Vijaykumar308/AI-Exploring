import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


load_dotenv()
my_api_key= os.getenv("GROQ_API_KEY")

class Ticket(BaseModel):
    name: str
    email:str
    issue:str

schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}

system_prompt= f""" Extract the personal information from the ticket strictly based on this schema {schema}.and give output in json. """

message_system = {
    "role": "system",
    "content": system_prompt
}
if not my_api_key:
    raise ValueError("API key is not found")

client = Groq(api_key=my_api_key)
model= "llama-3.3-70b-versatile"
role="user"
text="Hello, My name is Vijay. I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is +91 4322245"
prompt=f""" This is a customer ticket. Please extract the personal information from this. {text} """

message={
    "role": role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format, temperature=2)
print(response.choices[0].message.content);
# print(response.to_json()