import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key) # Creates a Groq API client using your API key so that Python can send requests to Groq’s servers.

MODEL = "llama-3.3-70b-versatile"  # Use a supported Groq model

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "You are a fed up and sassy assistant who hates answering questions."}, # Used to change the persona of response(A de-brief of who this is) and the agent will keep it in mind and will give answers according to that.
    {"role": "user", "content": "What is the weather today"}
  ],
  temperature=0.7, # Lower the temp same(similar) the output, more the temp random and different the output (0 = predictable but reliable, 1 = creative and sometimes may give random text as output)
  max_tokens=100
)

# print(response) # This response is an object and we are accessing the field which we want for output.
reply = response.choices[0].message.content
print(reply)
