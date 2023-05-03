import sys
import threading
import tkinter as tk

import speech_recognition
import pyttsx3
import Voice_ass

class Assistan:
    def __init__(self):
        self.root=tk.Tk()
        self.label=tk.Label(text="🤖",font=("Arial",120,"bold"))
        self.label.pack()
        threading.Thread(target=self.run_assistant).start()
        self.root.mainloop()
        
    def run_assistant(self):
        self.speaker=pyttsx3.init()
        self.voices=self.speaker.getProperty('voices')
        self.speaker.setProperty('voice',self.voices[1].id)
        self.recognizer= speech_recognition.Recognizer()

        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                    self.recorded_audio=self.recognizer.listen(mic)
                    text= self.recognizer.recognize_google(self.recorded_audio,language="en_US")
                    text2=text.lower()

                    if "hello" in text2:
                        self.label.config(fg="red")
                        audio=self.recognizer.listen(mic)
                        text=self.recognizer.recognize_google(audio,language="en_US")
                        
                        text1=text.lower()
                        if "start" in text1:
                            self.label.config(fg="blue")
                            Voice_ass.cmd()

                        if text1 == "stop":
                            self.speaker.say("Good Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit()

                        else:
                            self.label.config(fg="black")

                            
            except:
                self.label.config(fg="black")
                continue
        
Assistan()