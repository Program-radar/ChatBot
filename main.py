# chat bot main file
import pyttsx3 as voice
from wikipedia import summary as wiki_summary, PageError, DisambiguationError
from googlesearch import search


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
        quit_chat = False

    elif message == "search":
        quit_search = "yes"
        while quit_search.lower() == "yes":
            voice_engine.say("Search on google")
            voice_engine.runAndWait()
            query = input("\nSearch on google: ")
            for s in search(query, tld="com", num=10, stop=10, pause=2):
                print(s)
            quit_search = input("\ndo you want to search again?[yes,no] ")

    else:
        try:
            print_and_say(responses[message.lower()])
        except KeyError:
            # if response not found
            # search for it in wikipedia
            # and show a summary of it
            try:
                wiki = wiki_summary(message.title(), sentences=2)
                wikiSentence = wiki.split(". ")
                print_and_say("\n".join(wikiSentence))
            except (PageError, DisambiguationError) as e:
                # if document not found on wikipedia
                print_and_say(f"{message} did not match any documents on Wikipedia\n"
                              "Suggestions:\n"
                              "    Make sure all words are spelled correctly.\n"
                              "    Try different keywords.\n"
                              "    Try more general keywords.\n"
                              "    Try fewer keywords.")
