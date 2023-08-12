import tkinter as tk
from PIL import Image, ImageTk
import random

window= tk.Tk()
window.geometry("1000x1000")
window.title("ROLLY POLLY")
def roll_dice():
    a = random.randint(1,6)
    label = tk.Label(window,text=a).pack()
button = tk.Button(window,text="PRESS ME",command=roll_dice)
button.pack()
dice= ["C:/Users/khush/Downloads/1FFF.png","C:/Users/khush/Downloads/2FFF.png","C:/Users/khush/Downloads/3DD.png","C:/Users/khush/Downloads/4FF.png","C:/Users/khush/Downloads/5FF.png","C:/Users/khush/Downloads/6FF.png"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)
label1.image = image1 
label2.image = image2

label1.place(x = 0, y = 100)
label2.place(x = 500, y = 100)


def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2



button=tk.Button(window,text="ROLLY POLLY", bg='black', fg= 'white', font='Times 20 bold', command=dice_roll)
button.place(x= 450,y=0)
window.mainloop()  #Display window


