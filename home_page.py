from tkinter import *

root = Tk()
root.title("HOME")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
t = h - 200
m2 = w/2

root.geometry("%dx%d+0+0" % (w, h))
root.state('zoomed')
root.configure(bg='black')
root.resizable(0, 0)

#Frame and Label for Title
title = Frame(root, width=w, bd=15, height=170, relief='ridge', bg='grey')
title.pack(side=TOP)
title_label = Label(title, font=('Algerian', 60, 'bold'), bg='grey', text="FOOD ORDERING SYSTEM", justify=CENTER)
title_label.pack(pady=20)
title.pack_propagate(0)

#Frame and label
f = Frame(root, width=w, height=t, bd=15, relief='ridge', bg='grey')
f.pack(side=LEFT)
f.pack_propagate(0)

#Frame for buttons
bottom_frame = Frame(f,width=w,height=t, bd=12, relief='raised', bg='grey')
bottom_frame.pack(side=LEFT)
bottom_frame.pack_propagate(0)

#Frame and button for ordering items
order_button_frame = Frame(bottom_frame,width=w/4,height=90,bd=10,relief='sunken',bg='grey')
order_button_frame.pack(side=LEFT)
order = Button(order_button_frame,text="Order",width=14,height=1,font=('Arial',20,'bold'))
order.pack()

#Frame and button for clearing selection
clear_button_frame = Frame(bottom_frame,width=w/4,height=1,bd=10,relief='sunken',bg='grey')
clear_button_frame.pack(side=RIGHT)
clear = Button(clear_button_frame,text="Clear Selection",font=('Arial',20,'bold'),width=14,height=1)
clear.pack()

#Frame and button for adding items
add_button_frame = Frame(bottom_frame,width=w/4,height=1,bd=10,relief='sunken',bg='grey')
add_button_frame.pack(side=TOP)
add = Button(add_button_frame,text="Add",font=('Arial',20,'bold'),width=10,height=1)
add.pack()

root.mainloop()