import tkinter
from tkinter import *
import pandas as pd
from PIL import Image, ImageTk


def scrollwheel(event):
    return 'break'


def onscroll(axis, *args):
    global Tqty,Tstat,Torder
    Tqty.yview(*args)
    Torder.yview(*args)
    Tstat.yview(*args)


def change_table(*args):
    #Changing state of textbox for editing
    Torder.configure(state='normal')
    Tstat.configure(state='normal')
    Tqty.configure(state='normal')
    df_orders=pd.read_csv("CSV\\Kitchen.csv") #__________________________________________FILE LOC HERE
    #Dropping orders of tables other than the selected table
    for n in range(len(df_orders["order"])):
        if int(df_orders["table"][n]) != int(table.get()):
            df_orders.drop(n, inplace = True)
    df_orders.drop(["table"], axis = 1, inplace = True)
    #Clearing Textboxes of previous values
    Torder.delete('1.0',END)
    Tqty.delete('1.0',END)
    Tstat.delete('1.0',END)
    #Inserting current table's orders to textboxes
    Torder.insert('end',"ORDERS" +"\n")
    Tqty.insert('end',"QTY" + "\n")
    Tstat.insert('end',"STATUS" + "\n")
    for i in range(len(df_orders["order"])):
        Torder.insert('end',df_orders["order"].tolist()[i] +"\n")
        Tqty.insert('end',str(df_orders["qty"].tolist()[i]) + "\n")
        Tstat.insert('end', str(df_orders["status"].tolist()[i]) + "\n")
    # Changing state of textbox to stop editing once orders are entered
    Torder.configure(state='disabled')
    Tstat.configure(state='disabled')
    Tqty.configure(state='disabled')
    global b_add
    b_add = False


def order():
    if b_add == False:
        no_order()
        return
    qty = Tqty.get("1.0", "end-1c").split("\n")
    while ("" in qty):
        qty.remove("")
    if len(qty[1:]) != len(to_kitchen["qty"].tolist()):
        confirm_frame = Toplevel(relief='ridge', bd=20, bg='grey')
        confirm_frame.title("Invalid Quantities")
        confirm_frame.geometry("650x100+550+400")
        confirm_frame.resizable(0, 0)
        confirm_label = Label(confirm_frame, text="===== Invalid Quantity for Dish!!! =====",
                              font=('Arial', 18, 'bold'), bd=10, relief='groove', pady=20)
        confirm_label.pack()
        return
    to_kitchen["qty"] = qty[1:]
    for i in range(len(to_kitchen["qty"].tolist())):
        if int(to_kitchen["qty"][i]) < 1:
            to_kitchen.drop(i, inplace=True)
    to_kitchen.to_csv("CSV\\Kitchen.csv", mode='a', header=False, index=False)  # ___________FILE LOC HERE
    change_table()
    confirm()


def add():
    x = []
    y = []
    b = True
    sel_order1 = [str(box1.get(idx)) for idx in box1.curselection()]
    #Seperating SELECTED Order and Price from Listbox into 2 lists
    for j in sel_order1:
        l = j.split(sep=":      Rs.")
        for s in l:
            if b == True:
                x.append(s)
                b = False
            else:
                y.append(s)
                b = True
    global to_kitchen
    to_kitchen = pd.DataFrame()
    to_kitchen["order"],to_kitchen["price"],to_kitchen["qty"],to_kitchen["status"],to_kitchen["table"] = x,y,1,"False",int(table.get())
    to_kitchen = to_kitchen[["table","order","qty","price","status"]]

    #Changing state of textbox for editing
    Torder.configure(state='normal')
    Tstat.configure(state='normal')
    Tqty.configure(state='normal')
    #Clearing Textboxes of previous values
    Torder.delete('1.0',END)
    Tqty.delete('1.0',END)
    Tstat.delete('1.0',END)
    # ____________Inserting added items to textboxes
    Torder.insert('end',"ORDERING NOW" +"\n")
    Tqty.insert('end',"QTY" + "\n")
    Tstat.insert('end',"STATUS" + "\n")
    for i in range(len(to_kitchen["order"])):
        Torder.insert('end',to_kitchen["order"].tolist()[i] +"\n")
        Tqty.insert('end',str(to_kitchen["qty"].tolist()[i]) + "\n")
        Tstat.insert('end', str(to_kitchen["status"].tolist()[i]) + "\n")
    #Changing state of textbox to stop editing once orders are entered
    Torder.configure(state='disabled')
    Tstat.configure(state='disabled')
    global b_add
    b_add = True


def clear():
    box1.selection_clear(0, END)
    change_table()


def home():
    pass

def confirm(*args):
    confirm_frame = Toplevel(relief='ridge', bd=20, bg='grey')
    confirm_frame.title("Order Confirmation")
    confirm_frame.geometry("650x100+550+400")
    confirm_frame.resizable(0, 0)
    confirm_label = Label(confirm_frame, text="===== Your order has been placed =====", font=('Arial', 18, 'bold'), bd=10, relief='groove',pady=20)
    confirm_label.pack()

def no_order(*args):
    no_order_frame = Toplevel(relief='ridge', bd=20, bg='grey')
    no_order_frame.title("Order Confirmation")
    no_order_frame.geometry("650x100+550+400")
    no_order_frame.resizable(0, 0)
    no_order_label = Label(no_order_frame, text="===== No new orders added!!! =====", font=('Arial', 18, 'bold'), bd=10, relief='groove',pady=20)
    no_order_label.pack()

#table number button
tab_n = [1, 2, 3, 4]
root = Tk()
root.title("MENU")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
t = h - 200
m2 = w/2
# Create a photoimage object of the image in the path
# image1 = Image.open("Images\\BG.jpeg")
# test = ImageTk.PhotoImage(image1)
#
# label1 = tkinter.Label(image=test)
# label1.image = test
#
# # Position image
# label1.place(x=w, y=h)

root.geometry("%dx%d+0+0" % (w, h))
root.state('zoomed')
root.configure(bg='black')
root.resizable(0, 0)

#Frame and Label for Title
title = Frame(root, width=w, bd=15, height=170, relief='ridge', bg='grey')
title.pack(side=TOP)
title_label = Label(title, font=('Algerian', 60, 'bold'), bg='grey', text="MENU", justify=CENTER)
title_label.pack(pady=20)
title.pack_propagate(0)

#Left Partition
left = Frame(root, width=w/2, height=t, bd=15, relief='ridge', bg='grey')
left.pack(side=LEFT)
left.pack_propagate(0)

#Right Partition
right = Frame(root, width=w/2, height=t, bd=15, relief='ridge', bg='grey')
right.pack(side=RIGHT)
right.pack_propagate(0)

#Frame for table selection button
tab_button_frame = Frame(left,width=w/2,height=90, bd=15, relief='raised', bg='grey')
tab_button_frame.pack(side=TOP)
tab_button_frame.pack_propagate(0)

#Frame for menu
menu = Frame(left, width=w/2, height=t-90,bd=15,relief='raised',bg='grey')
menu.pack(side=BOTTOM)
menu.grid_propagate(0)
menu.pack_propagate(0)

#Frame for order summary
summary = Frame(right, width=w/2, height=t-140,bd=15,relief='raised',bg='grey')
summary.pack(side=TOP)
summary.pack_propagate(0)
summary.grid_propagate(0)

#Frame for buttons
bottom_frame = Frame(right,width=w/2,height=100, bd=12, relief='raised', bg='grey')
bottom_frame.pack(side=BOTTOM)
bottom_frame.pack_propagate(0)

#Frame and button for ordering items
order_button_frame = Frame(bottom_frame,width=w/4,height=90,bd=10,relief='sunken',bg='grey')
order_button_frame.pack(side=LEFT)
order = Button(order_button_frame,text="ORDER",command=order,width=15,height=10,font=('Arial',15,'bold'))
order.pack()

#Frame and button for clearing selection
clear_button_frame = Frame(bottom_frame,width=w/4,height=1,bd=10,relief='sunken',bg='grey')
clear_button_frame.pack(side=RIGHT)
clear = Button(clear_button_frame,text="CLEAR SELECTION",font=('Arial',15,'bold'),width=15,height=10,command=clear)
clear.pack()

#Frame and button for home
home_button_frame = Frame(bottom_frame,width=w/4,height=1,bd=10,relief='sunken',bg='grey')
home_button_frame.pack(side=RIGHT)
home = Button(home_button_frame,text="HOME",font=('Arial',15,'bold'),width=12,height=10,command=home)
home.pack()

#Frame and button for adding items
add_button_frame = Frame(bottom_frame,width=w/4,height=1,bd=10,relief='sunken',bg='grey')
add_button_frame.pack(side=LEFT)
add = Button(add_button_frame,text="ADD",font=('Arial',15,'bold'),width=15,height=10,command=add)
add.pack()

table = StringVar(root)
table.set('Table Number')

#OptionMenu for table numbers
table_menu = OptionMenu(tab_button_frame, table, *tab_n)
table_menu.configure(width=20,height=3,font=('Arial',15,'bold'),relief='raised',bd=10)
Label(tab_button_frame, text="Choose Table Number : ",font=('Arial',25,'bold'), bg='grey').pack(side=LEFT)
table_menu.pack()


#Listbox for Menu
box1 = Listbox(menu,bd=15,height=14,width=47,font=('Garamond',24,'bold'),selectmode="multiple")
box1.pack(side=LEFT)
box1.pack_propagate(0)

#Common Scrollbar for textboxes
yscrollbar = Scrollbar(summary, orient='vertical')
yscrollbar.grid(row=0, column=4,sticky=N+S+W)

#Textbox for orders
Torder = Text(summary, bg='white', bd=16, height=int(t/45), width=int(m2/30),font=('Garamond',22,'bold'))
Torder.grid(row=0, column=1)
Torder.bind('<MouseWheel>')

#Textbox for quantity
Tqty = Text(summary, bg='white', bd=16, height=int(t/45), width=int(m2/90),font=('Garamond',22,'bold'))
Tqty.grid(row=0,column=2)
Tqty.bind('<MouseWheel>')

#Textbox for status
Tstat = Text(summary, bg='white', bd=16, height=int(t/45), width=int(m2/75),font=('Garamond',22,'bold'))
Tstat.grid(row=0,column=3)
Tstat.bind('<MouseWheel>')

#reading menu dataframe
df_dish = pd.read_csv("CSV\\Menu.csv")

#Inserting Order and Price from menu into listbox
for i in range(len(df_dish["Dish"])):
     box1_el = str(df_dish["Dish"][i])+":      Rs."+ str(df_dish["Price"][i])
     box1.insert('end',box1_el)

root.mainloop()
