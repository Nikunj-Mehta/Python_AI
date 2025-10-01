# Hugging Face Chatbot

This project is a conversational chatbot that utilizes the Hugging Face API to generate responses based on user input. The chatbot is designed to be simple and easy to use, making it a great starting point for anyone interested in building AI-driven applications.

## Project Structure

```
huggingface-chatbot
├── src
│   ├── chatbot.py       # Main logic for the chatbot
│   └── utils.py         # Utility functions for the project
├── .env                 # Environment variables (API key)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nikunj-Mehta/Python_AI.git
   cd huggingface-chatbot
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your Hugging Face API key to the `.env` file:
     ```
     HUGGINGFACE_API_KEY=your_api_key_here
     ```

## Usage

To run the chatbot, execute the following command:

```bash
python src/chatbot.py
```

You can then interact with the chatbot by typing your messages in the console.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.