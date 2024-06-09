from openai import OpenAI
import json

with open('config.json') as config_file:
    config = json.load(config_file)

client = OpenAI(
    api_key= config['GPT_API_TOKEN']
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are just a companion who can always help, always answering correctly and without long texts."},
    {"role": "user", "content": "Hi!"}
  ]
)

print(completion.choices[0].message)