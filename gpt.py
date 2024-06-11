from openai import OpenAI
import json
from persistence import gpt_messages

with open('config.json') as config_file:
    config = json.load(config_file)

client = OpenAI(
    api_key= config['GPT_API_TOKEN']
)

last_message = gpt_messages.read_last_message()
if last_message:
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are just a companion who can always help, always answering correctly and without long texts."},
      {"role": "user", "content": gpt_messages.read_last_message()}
    ]
  )
  generated_text = completion.choices[0].message.content
  gpt_messages.save_answer_message(generated_text)
  print(generated_text)
else:
    print("No last message found.")