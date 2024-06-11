def save_last_message(message):
    with open("last_message.txt", "w") as file:
        file.write(message)

def read_answer_message():
    with open("answer_message.txt", "r") as file:
        return file.read().strip()