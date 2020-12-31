# chat bot main file
import pyttsx3 as voice


responses = {
    "hello": "Hello, what's up ?",
    "how is it going ?": "Good, How about you ?",
    "how are you": "I am feel fantastic",
    "what is your name": "I am Chat Bot builds with python you can call me anything.",
    "what do you do ?":  "I chat with you. You can tell me anything. I won't tell anyone about it, Trust Me!"
}

# initializing voice
voice_engine = voice.init()


# print first element and say second element
# if program need something else to say pass argument to second parameter
# if not, don't pass it and program will say exactly what printed
def print_and_say(message_to_print, message_to_say=None):
    print(message_to_print)
    if message_to_say is None:
        voice_engine.say(message_to_print)
    else:
        voice_engine.say(message_to_say)
    voice_engine.runAndWait()


quit_chat = True

# start chat process
print_and_say("Type 'q' at anytime to quit. ",
              "Start chatting.\n Remember you can quit at any time by Typing 'q' ")
while quit_chat:
    message = input("\nType your message: ")

    if message == "q":
        # quit chat
        print_and_say("It was good talk, See you later!")
    else:
        try:
            print_and_say(responses[message])
        except KeyError:
            # if response not found
            print_and_say("I can't understand, Suggestions:\n"
                          "   Make sure all words are spelled correctly.\n"
                          "   Try different keywords.\n"
                          "   Try more general keywords.\n"
                          "   Try fewer keywords.")
            voice_engine.runAndWait()
