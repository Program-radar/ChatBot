# chat bot main file
import pyttsx3 as voice


responses = {
    "hello": "Hello, what's up ?",
    "how is it going ?": "Good, How about you ?",
    "how are you": "I am feel fantastic",
    "what is your name": "I am Chat Bot builds with python you can call anything.",
    "what do you do ?":  "I chat with you. You can tell me anything. I won't tell anyone about it, Trust Me!"
}

# initializing voice
voice_engine = voice.init()

voice_engine.say("Hello, I am virtual assistant. How can I help you ?")

voice_engine.runAndWait()
