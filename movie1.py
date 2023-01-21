from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageTk
import random
import datetime
import os
from pathlib import Path
import shutil
import numpy as np
import cv2
import sys
from moviepy.editor import *




prompts = ["What's one thing you're really passionate about and why?", "What's a favorite memory from your childhood?",
"If you could have any job in the world, what would it be, why?", "Tell a big challenge you have faced and how you overcame it?",
"What do you think is the key to a happy and fulfilling life?", "What are some of your favorite ways to relax and unwind after a long day?",
"If you could have dinner with any historical figure, who would it be, why?", "What is something you've always wanted to try?",
"What is the most important lesson you've learned in your life so far?", "If you could change one thing about the world, what would it be?", "What is the meaning of life?",
"What is the purpose of human existence?", "Is there a higher power or spiritual force?", "Is there an afterlife?", "What is the nature of reality?",
"How do our thoughts and emotions shape your day?", "How do our beliefs shape our reality?", "Take a moment to reflect on who you are today"
, "What is the relationship between the mind and body?", "What is the nature of time?", "How do our experiences shape who we are?", "What is the role of free will?",
"What is the connection between morality and human behavior?", "Is there such thing as objective truth?", "Tell me about one of your goals", 
"What is the role of history in shaping our understanding of the world?", "How does our understanding of the world change over time?", "Tell me how your day went", 
"What was one good thing that happened today?"]

count = 0
def rec_vid():
    global count
    date = datetime.date.today()
    month = int(date.month)
    day = int(date.day) + count
    filename = str(month) + "-" + str(day) + ".mp4"
    count += 2
    

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename,fourcc, 20.0, (640,480))
    cap = cv2.VideoCapture(0)

    while (True):
        ret,frame = cap.read()
        out.write(frame)     
        cv2.imshow('Video',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    downloads_path = str(Path.home()) + "/Downloads/" + filename
    src_path = downloads_path
    dst_path = os.getcwd() + "/Videos" + filename
    shutil.move(src_path, dst_path)
    

def exit_program():
    sys.exit("Exit")

def second_window():
    global count
    window_2 = Toplevel()
    window_2.geometry("420x600")
    window_2.title("Record Your Videos")
    window_2.config(background= "#ddc1a7")

    # Prompt label
    prompt_label= Label(window_2, text = random.choice(prompts), font = ('Poppins', 10, 'bold'), fg = "white", bg= "#745e4d", relief = RAISED, bd = 5, padx = 5, pady= 10) 
    prompt_label.pack()
    
    # Record button
    button2 = Button(window_2, text = "Record", font = ("Poppins", 20, "bold"), fg = "red", bg = "#745e4d", relief = RAISED, bd = 5, padx = 2, pady= 10, command = rec_vid)
    button2.place(x = 150, y = 500)

    # Exit application button
    button3 = Button(window_2, text = "Exit", font = ("Poppins", 20, "bold"), fg = "Blue", bg = "#745e4d", relief = RAISED, bd = 5, padx = 2, pady= 10, command = exit_program)
    button3.place(x = 320, y = 500)

    # View Montage button
    # if count >= 4:
    #     button4 = Button(window_2, text = "View Montage!", font = ("Magneto", 20, "bold"), fg = "Green", bg = "#745e4d", relief = RAISED, bd = 5, padx = 2, pady= 10, command = makeMontage)
    #     button4.place(x = 320, y = 500)
    #     clip1 = VideoFileClip("1-15.mp4")
    #     clip2 = VideoFileClip("1-16.mp4")
    #     clip3 = VideoFileClip("1-17.mp4")
    #     clip4 = VideoFileClip("1-18.mp4")
    #     clip5 = VideoFileClip("1-19.mp4")

    #     final_clip = concatenate_videoclips([clip1,clip2,clip3,clip4,clip5])

    #     final_clip.write_videofile("Montage.mp4")


# Main window
WIDTH = 420
HEIGHT = 600
window = Tk()
window.geometry("420x600")
window.title("Home")
icon = PhotoImage(file = "1.png")
window.iconphoto(True, icon)
window.config(background = "#745e4d")

# Add photo to label
photo = PhotoImage(file= '1.png')

# Label = an area widget that holds text and/or an image within a window
label = Label(window, text = "Debrief", font = ('Magneto', 40, 'bold'), fg = "white", bg= "#745e4d", relief = RAISED, bd = 10, padx = 10, pady= 10, image= photo) 
label.pack()

# Lead to recording page button
button = Button(window, text = "Press for Daily Prompt", font = ("Poppins", 20, "bold"), fg = "white", bg = "#745e4d", activeforeground = "#745e4d", activebackground= "black", command = second_window)
button.pack()



window.mainloop()


