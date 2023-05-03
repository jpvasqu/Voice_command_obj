
import webbrowser
import datetime
import pathlib

import os
import email_alert
import SMS

import cv2
import pyttsx3
import google_search

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

cascade_path=pathlib.Path(cv2.__file__).parent.absolute()/'D:\john paul file\My Code\python code\PycharmProjects\haarcascade_frontalface_default.xml'
clf=cv2.CascadeClassifier(str(cascade_path))

def action(text):

    if text == "identify":
        camera=cv2.VideoCapture(0)
        engine.say("identifying Face")
        engine.runAndWait()

        while True:
            _, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = clf.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

            for(x,y,width,height) in faces:
                cv2.rectangle(frame,(x,y),(x+width,y+height),(255,0,0),1)

            cv2.imshow("Faces",frame)

            if cv2.waitKey(1)==ord("q"):
                break

        cv2.destroyAllWindows()

    if text == 'tell me the time' or text== "time":
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
        
    elif text == 'radio on' or text=="radio":
        a='opening Radio..'
        engine.say(a)
        engine.runAndWait()
        webbrowser.open('https://radio.org.ph/#monster')
               
    elif text == 'open youtube' or text=="youtube":
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
        
    elif text == "quit" or text == "clear window":
        os.system("taskkill /im chrome.exe /f")
        
        
    elif text == "emergency" or text == "help": 
        SMS.sms()
        email_alert.email_alert("S.O.S", "Help Me please ", "johnpaul.vasquez@evsu.edu.ph")
        engine.say("Help will come soon... Just wait")
        engine.runAndWait()
    elif text == "google":
        google_search.find()

    else:
        engine.say("What do you mean?")
        engine.runAndWait()
        

if __name__ == "__main__":
    while True:
        var= str(input("Ask: "))
        action(var)      
