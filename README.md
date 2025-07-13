# Rostyslav-GPT

This project is a simple Telegram chatbot that uses the GPT-3.5 OpenAI API to generate responses to user messages.

## Installation

1. Clone the repository:
```
git clone https://github.com/heereenveen/rostyslav-gpt.git
```
2. Install the required dependencies:
```
pip install requirements.txt
```
3. Create a `config.json` file in the project root directory with the following structure:
```json
{
  "GPT_API_TOKEN": "your_openai_api_key",
  "BOT_API_TOKEN": "your_telegram_bot_token"
}
```

## Usage

1. Run the `main.py` script to start the bot:
```
python main.py
```
2. Send a message to the bot, and it will respond with a generated message.

## API

The chatbot uses the following APIs:

- OpenAI API for generating responses using the GPT-3.5 language model.
- Aiogram for handling Telegram bot interactions.
