
# Groq API Chatbot

This project is a simple conversational chatbot that uses the Groq API to generate responses based on user input. The chatbot is stateless and provides direct answers to your questions, making it easy to use and extend.


## Project Structure

```
BasicChatBot
├── huggingface-chatbot
│   └── src
│       ├── chatbot.py         # Console chatbot logic
│       ├── gradio_chatbot.py  # Gradio web UI for chatbot
├── .env                      # Environment variables (API key)
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nikunj-Mehta/Python_AI.git
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # Or on Mac/Linux: source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install groq
   ```

4. **Set up your Groq API key**:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_actual_groq_api_key
     ```



## Usage

### Console Chatbot
To start the chatbot in the console, run:

```bash
python huggingface-chatbot/src/chatbot.py
```

Type your message and press Enter to get a response. Type `exit` to end the conversation.

### Gradio Web Chatbot
To launch the chatbot with a web interface (Gradio), run:

```bash
python BasicChatbot/gradio_chatbot.py
```

This will start a Gradio server and open a browser window for chatting. You can deploy this for a week by keeping the script running.



## Features

- Uses Groq API for fast, accurate responses
- Stateless: each reply is based only on your latest input
- Console and Gradio web UI options
- Easy to customize for other models or prompts

## Contributing

Feel free to submit issues or pull requests for improvements or new features.



## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

Created by Nikunj Mehta

- GitHub: [Nikunj-Mehta](https://github.com/Nikunj-Mehta)
- LinkedIn: [nikunj-mehta-016a2a2b0](https://www.linkedin.com/in/nikunj-mehta-016a2a2b0/)