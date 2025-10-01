import os
from dotenv import load_dotenv
from groq import Groq
import tiktoken

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key) # Creates a Groq API client using your API key so that Python can send requests to Groq’s servers.
MODEL = "llama-3.3-70b-versatile"  # Use a supported Groq model
TEMPERATURE = 0.7
MAX_TOKEN = 60
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."
messages = [{"role": "system", "content": SYSTEM_PROMPT}] # Used to change the persona of response(A de-brief of who this is) and the agent will keep it in mind and will give answers according to that. This is a list and we defined it outside because we don't want to create it again and again and we will append everything the user asks adn agent replys. It is a list of dictionaries.
TOKEN_BUDGET = 100 # When the budget exceeds over 100 the we will remove the user's first message from history.

# Encoding is the process of converting a character into its corresponding numeric code according to a specific character set.
def get_encoding(model):
  try:
    return tiktoken.encoding_for_model(model) # From tiktoken we are going to find specific encoding for the model
  except KeyError:
    print(f"Warning: Tokenizer for model '{model}' not found. Falling back to 'cl100k_base'.") # To handle if any error occurs.
    return tiktoken.get_encoding("cl100k_base") # Since the encoding for the specific model is not available so it will use the encoding of cl100k_base.
  
ENCODING = get_encoding(MODEL) # the encoding will be stored in the variable

# Now we are going to count to token
def count_token(text):
  return len(ENCODING.encode(text)) # Returns the length of whatever encoding methood is used and using the .encode method form tiktoken library and looking at the text.

# It is going to return the total tokens used form the message content which is entered.
def total_tokens_used(messages):
  try:
    return sum(count_token(msg["content"]) for msg in messages)
  except Exception as e:
    print(f"[token count error]: {e}")
    return 0
  
# Enforce the token limit so that we can't enter more than to it.
def enforce_token_budget(messages, budget=TOKEN_BUDGET):
  try:
    while total_tokens_used(messages) > budget:
      if len(messages) <= 2:
        break
      messages.pop(1) #While the tokens used is more that the budget then we will be popping off the oldest message. Except we are not going to pop the system message therefor pop(1).
  except Exception as e:
    print(f"[token budget error]: {e}")


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
  
  enforce_token_budget(messages)

  return reply

while True:
  user_input = input("You: ")
  if user_input.strip().lower() in {"exit", "quit"}:
    print("Assistant: Bye! Have a good day!")
    break
  answer = chat(user_input)
  print("Assistant: ", answer)
  print("Current tokens: ", total_tokens_used(messages))