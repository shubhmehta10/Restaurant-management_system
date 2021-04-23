import os
import sys
from tkinter import *
from PIL import ImageTk,Image


def menu():
    os.system('python menu_page.py')

def kitchen():
    os.system('python kitchen_page.py')

def checkout():
    os.system('python checkout_page.py')


root = Tk()
root.title("FOOD ORDERING SYSTEM")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  # Width and height according to users PC
t = h - 100

root.geometry("%dx%d+0+0" % (w, h))
root.state('zoomed')
root.configure(bg='black')
root.resizable(0, 0)

# Title of Main Window
title = Frame(root, width=w, bd=15, height=170, relief='ridge', bg='grey')
title.pack(side=TOP)
title.pack_propagate(0)
title_label = Label(title, font=('Algerian', 60, 'bold'), bg='grey', text="FOOD ORDERING SYSTEM", justify=CENTER)
title_label.pack(pady=20)

#frame
frame1 = Frame(root, width= w, height =t, relief='ridge', bg='grey', bd=15)
frame1.pack()
frame1.pack_propagate(0)

#frame for image
image_frame = Frame(frame1, width=w, height=531, relief='ridge',bg='grey',bd=15)
image_frame.pack(side=TOP)
image_frame.pack_propagate(0)
image1 = Image.open("Images\\BG.jpeg")
image1 = image1.resize((w,531),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image1)
image_label = Label(image_frame,image=photo,padx=10,pady=10)
image_label.pack()


#frame for buttons
button_frame = Frame(frame1, width=w, height=180, relief='ridge',bg='grey',bd=15)
button_frame.pack(side=BOTTOM,fill=Y)

#Menu Button GUI
menu_button_frame = Frame(button_frame, width=w, height=1, bd=10, relief='sunken', bg='grey')
menu_button_frame.pack(side=LEFT)
menu_button = Button(menu_button_frame, text="MENU", width=30, height=1, font=('Arial', 20, 'bold'), command=menu)
menu_button.pack()

# Kitchen Button GUI
kitchen_button_frame = Frame(button_frame, width=w, height=1, bd=10, relief='sunken', bg='grey')
kitchen_button_frame.pack(side=LEFT)
kitchen_button = Button(kitchen_button_frame, text="KITCHEN", width=30, height=1, font=('Arial', 20, 'bold'),command=kitchen)
kitchen_button.pack()

# checkout Button GUI
checkout_button_frame = Frame(button_frame, width=w, height=1, bd=10, relief='sunken', bg='grey')
checkout_button_frame.pack(side=RIGHT)
checkout_button = Button(checkout_button_frame, text="CHECKOUT", width=30, height=1, font=('Arial', 20, 'bold'),command=checkout)
checkout_button.pack()


root.mainloop()
