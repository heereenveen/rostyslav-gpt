def read_last_message():
    try:
        with open("last_message.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
    
def save_answer_message(answer):
    with open("answer_message.txt", "w") as file:
        file.write(answer)