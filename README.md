
# Groq API Chatbot

This project is a simple conversational chatbot that uses the Groq API to generate responses based on user input. The chatbot is stateless and provides direct answers to your questions, making it easy to use and extend.

## Project Structure

```
huggingface-chatbot
├── src
│   ├── chatbot.py       # Main logic for the chatbot
├── .env                 # Environment variables (API key)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
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

To start the chatbot, run:

```bash
python src/chatbot.py
```

Type your message and press Enter to get a response. Type `exit` to end the conversation.


## Features

- Uses Groq API for fast, accurate responses
- Stateless: each reply is based only on your latest input
- Easy to customize for other models or prompts

## Contributing

Feel free to submit issues or pull requests for improvements or new features.


## License

This project is licensed under the MIT License. See the LICENSE file for details.