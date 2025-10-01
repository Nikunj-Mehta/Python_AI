import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key) # Creates a Groq API client using your API key so that Python can send requests to Groq’s servers.
MODEL = "llama-3.3-70b-versatile"  # Use a supported Groq model
TEMPERATURE = 0.7
MAX_TOKEN = 60
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."
messages = [{"role": "system", "content": SYSTEM_PROMPT}] # Used to change the persona of response(A de-brief of who this is) and the agent will keep it in mind and will give answers according to that. This is a list and we defined it outside because we don't want to create it again and again and we will append everything the user asks adn agent replys.

def chat(user_input):
  messages.append({"role": "user", "content": user_input}) # We are adding the user's msg at the end of the list to keep track of history.

  response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature=TEMPERATURE, # Lower the temp same(similar) the output, more the temp random and different the output (0 = predictable but reliable, 1 = creative and sometimes may give random text as output)
    max_tokens=MAX_TOKEN
  )

  # print(response) # This response is an object and we are accessing the field which we want for output.
  reply = response.choices[0].message.content
  messages.append({"role": "assistant", "content": reply}) # adding the assistant's reply in the list.
  return reply

while True:
  user_input = input("You: ")
  if user_input.strip().lower() in {"exit", "quit"}:
    print("Assistant: Bye! Have a good day!")
    break
  answer = chat(user_input)
  print("Assistant: ", answer)