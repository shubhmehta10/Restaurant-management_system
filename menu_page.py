from tkinter import *
import pandas as pd

def order():
    pass

def add():
    pass

def clear():
    pass


tab_n = [1, 2, 3, 4] #__________LIST OF TABLE NUMBERS
root = Tk()
root.title("Python Project (Restaurant Ordering System)")   #____Header Title
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  #Width and height according to users PC
t = h - 200 #THIS WAS -150
m2 = w/2

root.geometry("%dx%d+0+0" % (w, h))     #Defining Window Geometry
root.state('zoomed')
root.configure(bg='black')
root.resizable(0, 0)                    #Disabling Resizing of Window

#__________Frame and Label for Title
title = Frame(root, width=w, bd=15, height=170, relief='ridge', bg='grey')
title.pack(side=TOP)
title_label = Label(title, font=('Algerian', 60, 'bold'), bg='grey', text="FOOD ORDERING SYSTEM", justify=CENTER)
title_label.pack(pady=20)
title.pack_propagate(0)

#___________________Left Partition
left = Frame(root, width=w/2, height=t, bd=15, relief='ridge', bg='grey')
left.pack(side=LEFT)
left.pack_propagate(0)

#___________________Right Partition
right = Frame(root, width=w/2, height=t, bd=15, relief='ridge', bg='grey')
right.pack(side=RIGHT)
right.pack_propagate(0)

#____________Frame for table selection button
tab_button_frame = Frame(left,width=w/2,height=90, bd=15, relief='raised', bg='grey')
tab_button_frame.pack(side=TOP)
tab_button_frame.pack_propagate(0)

#____________Frame for menu
menu = Frame(left, width=w/2, height=t-90,bd=15,relief='raised',bg='grey')
menu.pack(side=BOTTOM)
menu.grid_propagate(0)
menu.pack_propagate(0)

#______________Frame for order summary
summary = Frame(right, width=w/2, height=t-140,bd=15,relief='raised',bg='grey')
summary.pack(side=TOP)
summary.pack_propagate(0)
summary.grid_propagate(0)

#_______________Frame for buttons
bottom_frame = Frame(right,width=w/2,height=100, bd=12, relief='raised', bg='grey')
bottom_frame.pack(side=BOTTOM)
bottom_frame.pack_propagate(0)

#_________________Frame and button for ordering items
order_button_frame = Frame(bottom_frame,width=w/4,height=90,bd=10,relief='sunken',bg='grey')
order_button_frame.pack(side=LEFT)
order = Button(order_button_frame,text="Order",command=order,width=14,height=1,font=('Arial',20,'bold'))
order.pack()

#_________________Frame and button for clearing selection
clear_button_frame = Frame(bottom_frame,width=w/4,height=1,bd=10,relief='sunken',bg='grey')
clear_button_frame.pack(side=RIGHT)
clear = Button(clear_button_frame,text="Clear Selection",font=('Arial',20,'bold'),width=14,height=1,command=clear)
clear.pack()

#_________________Frame and button for adding items
add_button_frame = Frame(bottom_frame,width=w/4,height=1,bd=10,relief='sunken',bg='grey')
add_button_frame.pack(side=BOTTOM)
add = Button(add_button_frame,text="Add",font=('Arial',20,'bold'),width=10,height=1,command=add)
add.pack()

table = StringVar(root)     #Defining table for optionmenu
table.set('Table Number')  # set the default option

#___________________OptionMenu for table numbers
table_menu = OptionMenu(tab_button_frame, table, *tab_n)
table_menu.configure(width=20,height=3,font=('Arial',15,'bold'),relief='raised',bd=10)
Label(tab_button_frame, text="Choose Table Number : ",font=('Arial',25,'bold'), bg='grey').pack(side=LEFT)
table_menu.pack()


#________________________Listbox for Menu
box1 = Listbox(menu,bd=15,height=14,width=47,font=('Garamond',24,'bold'),selectmode="multiple")
box1.pack(side=LEFT)
box1.pack_propagate(0)

#_______________Common Scrollbar for textboxes
yscrollbar = Scrollbar(summary, orient='vertical')
yscrollbar.grid(row=0, column=4,sticky=N+S+W)

#_______Textbox for orders
Torder = Text(summary, bg='white', bd=16, height=int(t/45), width=int(m2/30),font=('Garamond',22,'bold'))
Torder.grid(row=0, column=1)
Torder.bind('<MouseWheel>')

#_______Textbox for quantity
Tqty = Text(summary, bg='white', bd=16, height=int(t/45), width=int(m2/90),font=('Garamond',22,'bold'))
Tqty.grid(row=0,column=2)
Tqty.bind('<MouseWheel>')

#_______Textbox for status
Tstat = Text(summary, bg='white', bd=16, height=int(t/45), width=int(m2/75),font=('Garamond',22,'bold'))
Tstat.grid(row=0,column=3)
Tstat.bind('<MouseWheel>')    #Binding scrollwheel function to mouse-scroll event

#_________reading menu dataframe
#df_dish = pd.read_csv("CSV\\Menu.csv")#___________________________________FILE LOCATION HERE

#_______________________Inserting Order and Price from menu into listbox
# for i in range(len(df_dish["Dish"])):
#     box1_el = str(df_dish["Dish"][i])+":      Rs."+ str(df_dish["Price"][i])
#     box1.insert('end',box1_el)

root.mainloop()             #_____________Keeps the root window in loop
