# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:19:53 2017

@author: Chintan
"""
import random, os, broize
from gtts import gTTS
from playsound import playsound
import speech_recognition as hear

def greeting(sentence):
    for word in sentence:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
        
if __name__ == "__main__":
    #for reference of first response
    #GREETING_KEYWORDS = ("hello", "hi", "hey", "hey there", "hola", "greetings", "what's up")
    #GREETING_RESPONSES = ("hi", "hello there", "hiya", "heya", "*nods*", "hola")
    flag = 0
    if os.path.exists('counter.txt'):
        file = open('counter.txt', 'r')
        flag = int(file.read())
        file.close()
    else:
        file = open('counter.txt', 'w')
        file.write(str(flag))
        file.close()
    ##########################GET CHOICE###############################
##    r = hear.Recognizer()
##    with hear.Microphone() as source:
##        print("Talk or chat?")
##        print("To chat using keyboard, say chat. Otherwise, shoot away!!")
##        audio = r.listen(source)
##    sentence = "chat"
##    try:
##        sentence = str(r.recognize_google(audio))
##        print("YOU : ", sentence)
##    except hear.UnknownValueError:
##        print("Sorry! Couldn't understand")
##    except hear.RequestError as e:
##        print("Could not request Google API Services ", e.format(0))
##    ################################CHAT###############################
    if True:
    #if sentence == "chat":
        print("BOT : Hi! You are?")
        name = str(input("YOU : "))
        print("BOT : Hello " + name + "! How are you doing?")
        while(True):
            sentence = str(input("YOU : "))
            if sentence == "bye":
                break
            response = str(broize.broback(sentence))
            print("BOT : " + response)
    ##################################TALK#################################
    else:
        while(True):
            with hear.Microphone() as source:
                print("I'm listening...")
                audio = r.listen(source)
            sentence = ''
            try:
                sentence = str(r.recognize_google(audio))
                print("YOU : ", sentence)
            except hear.UnknownValueError:
                print("Sorry! Couldn't understand")
            except hear.RequestError as e:
                print("Could not request Google API Services ", e.format(0))
            if sentence == "bye":
                break
            response = str(broize.broback(sentence))
            s = gTTS(text=response, lang='en')
            print(flag)
            s.save(str(flag)+'.mp3')
            playsound(str(flag)+'.mp3')
            flag+=1
            file = open('counter.txt', 'w')
            file.write(str(flag))
            file.close()
            #print(flag)
            print("BOT : " + response)

        
