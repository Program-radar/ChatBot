# chat bot main file
import pyttsx3 as voice


responses = {
    "hello": "Hello, what's up ?",
    "how is it going ?": "Good, How about you ?",
    "how are you": "I am feel fantastic",
    "what is your name": "I am Chat Bot builds with python you can call me anything.",
    "what do you do ?":  "I chat with you. You can tell me anything. I won't tell anyone about it, Trust Me!"
}

# asking user to choose between text and voice
text_or_voice = input("Welcome to the Chat Bot! How do you like to chat ?[text/voice] ")
quit_chat = True

if text_or_voice == "text":
    print("Type 'q' at any time to quit")
    while quit_chat:
        message = input("\nType your message: ")
        if message == "q":
            quit_chat = False
        else:
            try:
                print(responses[message])
            except KeyError:
                print("I can't understand, Suggestions:\n"
                      "   Make sure all words are spelled correctly.\n"
                      "   Try different keywords.\n"
                      "   Try more general keywords.\n"
                      "   Try fewer keywords")

elif text_or_voice == "voice":
    # initializing voice
    voice_engine = voice.init()
    voice_engine.say("Hello, I am virtual assistant. How can I help you ? ")
    voice_engine.runAndWait()
