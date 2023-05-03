from tkinter import *
from PIL import Image
from threading import Thread

root=Tk()
root.geometry("800x550")
root.config(background="black")

gifImage="face-id-glitch.gif"
open_image=Image.open(gifImage)

frames = open_image.n_frames

imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]

count = 0

showAnimation = None

def history():

    import Voice_ass
    Voice_ass.cmd()
    
    
    
def animation(count):
    
    global showAnimation
    newImage = imageObject[count]

    gif_label.configure(image=newImage)
    count += 1

    if count == frames:
        count = 0
    showAnimation = root.after(50,lambda:animation(count))

    
   
    
gif_label = Label(root,image="",bg="Black")
gif_label.place(x=190,y=20,width=450,height=500)

Btn_history= Button(root,text="History",font=("arial",20),bg="black",fg="white",
                    border=0,activebackground="black",activeforeground="blue",
                    command=history)
Btn_history.place(x=30,y=20)

animation(count)

root.mainloop()

