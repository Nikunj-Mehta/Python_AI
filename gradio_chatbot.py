# gradio_chatbot.py
import os
from dotenv import load_dotenv
from groq import Groq
import tiktoken
import gradio as gr

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Chatbot settings
MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.7
MAX_TOKEN = 60
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."
messages = [{"role": "system", "content": SYSTEM_PROMPT}]
TOKEN_BUDGET = 100

# Token encoding
try:
    ENCODING = tiktoken.encoding_for_model(MODEL)
except KeyError:
    print(f"Warning: Tokenizer for {MODEL} not found. Using cl100k_base fallback.")
    ENCODING = tiktoken.get_encoding("cl100k_base")

def count_token(text):
    return len(ENCODING.encode(text))

def total_tokens_used(messages):
    return sum(count_token(msg["content"]) for msg in messages)

def enforce_token_budget(messages, budget=TOKEN_BUDGET):
    while total_tokens_used(messages) > budget:
        if len(messages) <= 2:
            break
        messages.pop(1)

def chat(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKEN
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    enforce_token_budget(messages)
    return reply

# Gradio interface
iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Groq Chatbot (Sassy)",
    description="A fed-up and sassy assistant powered by Groq API. Type your message and hit Enter or click Send!"
)

# Launch with public shareable link
iface.launch(share=True)
