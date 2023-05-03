from googlesearch import search
import webbrowser
import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def find():
        engine.say("what do you want me to search")
        engine.runAndWait()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source,duration=0.5)
            recorded_audio=recognizer.listen(source)

        try:
            
            text=recognizer.recognize_google(recorded_audio,language='en_US')
            search1=text.lower()
            print('Your message:',text)
            
        except Exception as ex:
            print(ex)

        for i in search(search1, num_results=1, advanced= True):
            webbrowser.open(i.url)
            break
if __name__ == "__main__":
     find()