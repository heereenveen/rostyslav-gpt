from openai import OpenAI
import json

with open('config.json') as config_file:
    config = json.load(config_file)

client = OpenAI(
    api_key= config['GPT_API_TOKEN']
)

def read_last_message():
    try:
        with open("last_message.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
    
def save_answer_message(answer):
    with open("answer_message.txt", "w") as file:
        file.write(answer)

last_message = read_last_message()
if last_message:
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are just a companion who can always help, always answering correctly and without long texts."},
      {"role": "user", "content": read_last_message()}
    ]
  )
  generated_text = completion.choices[0].message.content
  save_answer_message(generated_text)
  print(generated_text)
else:
    print("No last message found.")