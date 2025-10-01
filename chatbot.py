import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"  # Use a supported Groq model

conversation_history = []

def chat_with_model(user_input):
    # Prepare messages for Groq API
    messages = []
    for turn in conversation_history:
        messages.append({"role": "user", "content": turn['user']})
        messages.append({"role": "assistant", "content": turn['bot']})
    messages.append({"role": "user", "content": user_input})

    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        bot_reply = completion.choices[0].message.content.strip()
        conversation_history.append({"user": user_input, "bot": bot_reply})
        return bot_reply
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        response = chat_with_model(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
