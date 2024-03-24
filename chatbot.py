def get_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there!"
    elif "how are you" in message:
        return "I'm doing well, thank you!"
    else:
        return "I'm sorry, I don't understand that."
