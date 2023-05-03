import speech_recognition as sr
import command
import pyttsx3
import reply
import random

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

ran=random.randint(0,len(reply.char)-1)
ran1=random.randint(0,len(reply.ask)-1)



def cmd():
  
        engine.say(reply.ask[ran1])
        engine.runAndWait()
        with sr.Microphone() as source:
            print("Clearing background noises...Pleasw wait")
           
            recognizer.adjust_for_ambient_noise(source,duration=0.5)
            recorded_audio=recognizer.listen(source)
        try:
            
            text=recognizer.recognize_google(recorded_audio,language='en_US')
            text=text.lower()
            print('Your message:',text)
            
        except Exception as ex:
            print(ex)
        while True:

            try:
              
              command.action(text)
              break

            except:
                engine.say(reply.char[ran])
                engine.runAndWait()
                break
if __name__ == "__main__":
    cmd()
    
