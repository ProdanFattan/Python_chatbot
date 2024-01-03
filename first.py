from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pt
import speech_recognition as sr
import threading

eng = pt.init()
myBot = ChatBot("My Bot")


voices = eng.getProperty('voices')
print(voices)


eng.setProperty('voice', voices[0].id)


def speak(word):
    eng.say(word)
    eng.runAndWait()


convo = [
    'Hello',
    'Hi there',
    'What is your name ?',
    'My name is Wednesday, created by Fattan Prodan',
    'How are you?',
    'I am doing great these days',
    'Thank you',
    'In which language you talk?',
    'I mostly talk in english'

]
    
trainer = ListTrainer(myBot)
trainer.train(convo)


screen = Tk()
screen.geometry("500x660")
screen.title("Chat Bot")
img = PhotoImage(file="ab3.png")
pLabel = Label(screen, image = img)
pLabel.pack(pady= 10)


frame = Frame(screen)


def repeatF():
    while TRUE:
        take_question()


def take_question():
    s = sr.Recognizer()
    with sr.Microphone() as m:
        audio = s.listen(m)
        query = s.recognize_google(audio,language='eng')
        tField.delete(0,END)
        tField.insert(0,query)
        ask_from_bot()


def ask_from_bot():
    query = tField.get()
    botAns = myBot.get_response(query)
    msg.insert(END, "You: "+query)
    msg.insert(END, "Bot: "+str(botAns))
    speak(botAns)
    tField.delete(0,END)
    msg.yview(END)

sc = Scrollbar(frame)
msg = Listbox(frame,width=80,height=20,yscrollcommand= sc.set)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()


tField = Entry(screen,font=("Verdana", 20))
tField.pack(fill=X, pady=10)

btn = Button(screen,text="Ask", font=("Verdana", 20), command= ask_from_bot)
btn.pack()


def enter_f(event):
    btn.invoke()

screen.bind('<Return>', enter_f)

t = threading.Thread(target=repeatF)

t.start()

screen.mainloop()


