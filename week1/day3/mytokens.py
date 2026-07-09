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

prompt1 = "Hi!"
prompt2 = "What you know about AI and ML. Explain in detail"
prompt3 = "Tell me something about yourself"

prompts = [prompt1, prompt2, prompt3];

for prompt in prompts:
   
    message={
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages, temperature=2, max_tokens=50)
    usages = response.usage
    print(f"Prompt: {prompt} --> your token: {usages.prompt_tokens} completion token: {usages.completion_tokens} total token: {usages.prompt_tokens + usages.completion_tokens} finish reason: {response.choices[0].finish_reason}")
    # print(response.choices[0].message.content);

