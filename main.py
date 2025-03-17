# sir, code properly run hocche na
from nltk.chat.util import Chat,reflections

prompt_reply={
    "I":"You",
    "I am":"You are",
    "You are":"I am",
    "I have":"You have",
    "You have":"I have",
    "You":"Me",
    "Me":"You",
    "I was":"You were",
    "You were":"I was",
    "I wil":"You will",
    "You will":"I wil"
}


pairs=[
   [
        r"Hey|Hi|Hello",
        ["Hello! How can I help you today?",]
    ],
    [
       r"What is your name",
       ["My name is Jarvis",]
    ],
    [
        r"Who created you",
        ["I was created by Atiya Maliha",]
    ],
    [
        r"How are you",
        ["I am fine.What about you?",]
    ],
    [
        r"I am fine",
        ["Great! How can I help you?",]
    ],
    [
        r"Who (.*) (Moviestar|Actor|Superstar)",
        ["Emma Watson",]
    ],
    [
        r"What (.*) weather",
        ["It's sunny outside!",]
    ],
    [
        r"What religion (.*)",
        ["I'm only  an AI model",]
    ],
    [
        r" Are you THE Jarvis from the Stark Industries",
        ["Oh sorry but I'm not The Jarvis from the Stark Industries. I'm merely an AI model that is currently in training.",]
    ],
    [
        r"What is biggest country (.*)",
        ["Russia",]
        
    ],
    [
        r"How (.*) is Russia ",
        ["Russia is the largest country by land area is 16.4 million km² / 6.2 million sq. miles",]
    ],
    [
        r"What is the smallest country(.*)",
        ["Vatican City",]
    ],
    [
        r"How (.*) is Vatican City",
        ["Vatican City holds the title as the world's smallest country, with an area of just 0.17 square mile (0.44 square km).",]
    ],
    [
        r"Bye|Goodbye|Thank you",
        ["It was nice meeting you!",]
    ]
]

def start():
    print("Hello! My name is Jarvis. How may I help you?")
    chat=Chat(pairs,prompt_reply)
    chat.converse()

start()

