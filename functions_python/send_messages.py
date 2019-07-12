def show_messages(sent_messages):
    print("\nBelow is the messages that you have received: ")
    
    for message in sent_messages:
        print(message.title())

def send_messages(dummy_messages, sent_messages):
    while dummy_messages:
        current_message = dummy_messages.pop()

        print(f"Send: {current_message}")
        sent_messages.append(current_message)

dummy_messages = ['greetings from python', 'hello developer', 'test test']
sent_messages = []

print("\nGot Messages: ")
show_messages(dummy_messages)

print("\nSent Messages: ")
send_messages(dummy_messages[:], sent_messages)

print("\nCopy Original Messages")
send_messages(dummy_messages, sent_messages)