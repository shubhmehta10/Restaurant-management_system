# ____________________________________importing all the required libraries
from tkinter import *
import pandas as pd
import tkinter.ttk as ttk


# ___________________________________________________function for the Confirm Button for finishing Order
def confirm(*args):
    pass

# _______________________________________________function for Refresh Button to Display Orders with status update
def refresh():
    pass


# ________________________________________________function to cancel an order
def cancel():
    pass


# ___________________________________________Start of Mainloop GUI

tab_n = [1, 2, 3, 4, 5, 6]  # LIST OF TABLE NUMBERS
root = Tk()
root.title("Python Project (Restaurant Ordering System)")  # ____Header Title
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  # Width and height according to users PC
t = h - 100

# ________________________________________________________Main Window
root.geometry("%dx%d+0+0" % (w, h))
root.state('zoomed')
root.configure(bg='black')
root.resizable(0, 0)

# __________________________________________________Title of Main Window
title = Frame(root, width=w, bd=15, height=100, relief='ridge', bg='grey')
title.pack(side=TOP)
title.pack_propagate(0)
title_label = Label(title, font=('Algerian', 60, 'bold'), bg='grey', text="KITCHEN", justify=CENTER)
title_label.pack(padx=50)

# __________________________________________________Left Partition
left = Frame(root, width=3 / 4 * w, height=t, bd=15, relief='ridge', bg='grey')
left.pack(side=LEFT)
left.pack_propagate(0)

# __________________________________________________Right Partition
right = Frame(root, width=w / 4, height=t, bd=15, relief='ridge', bg='grey')
right.pack(side=RIGHT)
right.pack_propagate(0)

# ____________________________________________________Frame and Label for pending orders
pending_frame = Frame(left, width=3 / 4 * w, height=90, bd=18, relief='ridge', bg='grey')
pending_frame.pack(side=TOP)
pending_frame.pack_propagate(0)
Label(pending_frame, text="Pending Orders:", font=('algerian', 35, 'bold'), bg='grey', justify=CENTER).pack()

# _____________________________________________________Frame for menu
menu = Frame(left, width=3 / 4 * w, height=t - 90, bd=15, relief='raised', bg='grey')
menu.pack(side=BOTTOM)
menu.grid_propagate(0)
menu.pack_propagate(0)

# _______________________________________________Display window for Orders
style = ttk.Style()
style.configure("Treeview", highlightthickness=0, bd=10, font=('Garamond', 21, 'bold'),rowheight=45)  # Modify the font of the body
style.configure("Treeview.Heading", font=('Times New Roman', 25, 'bold'))
kitchen = ttk.Treeview(menu, columns=("Index", "Table", "Order", "Qty", "Status"), height=29, selectmode='browse')
kitchen["displaycolumns"] = ("Table", "Order", "Qty", "Status")  # ________________HIDES INDEX COLUMN
kitchen['show'] = 'headings'
kitchen.pack()
kitchen.pack_propagate(0)
kitchen.column("0", width=220, anchor='n')
kitchen.column("1", width=220, anchor='n')
kitchen.column("2", width=500, anchor='w')
kitchen.column("3", width=215, anchor='n')
kitchen.column("4", width=200, anchor='n')
kitchen.heading("1", text="Table")
kitchen.heading("2", text="Order")
kitchen.heading("3", text="Qty")
kitchen.heading("4", text="Status")

# ______________________________________________________Right Window GUI
right_frame = Frame(right, width=w / 2, height=t, bd=15, relief='raised', bg='grey')
right_frame.pack(side=RIGHT)
right_frame.pack_propagate(0)

# ______________________________________________________Done Button GUI
done_button_frame = Frame(right_frame, width=w / 4, height=1, bd=10, relief='sunken', bg='grey')
done_button_frame.pack(side=TOP, pady=100)
done = Button(done_button_frame, text="Done", width=20, height=1, font=('Arial', 20, 'bold'), command=confirm)
done.pack()

# ______________________________________________________Refresh Button GUI
refresh_button_frame = Frame(right_frame, width=w / 4, height=1, bd=10, relief='sunken', bg='grey')
refresh_button_frame.pack(side=TOP, pady=50)
refresh_button = Button(refresh_button_frame, text="Refresh", width=20, height=1, font=('Arial', 20, 'bold'),
                        command=refresh)
refresh_button.pack()

# ______________________________________________________Cancel Button GUI
cancel_button_frame = Frame(right_frame, width=w / 4, height=20, bd=10, relief='sunken', bg='grey')
cancel_button_frame.pack(side=BOTTOM, pady=80)
cancel = Button(cancel_button_frame, text="Cancel Order", font=('Arial', 20, 'bold'), width=20, height=1,
                command=cancel)
cancel.pack()

# # _______________________________________________________FILE Reading for Orders:
# df_dish = pd.read_csv("CSV\\Kitchen.csv")  # _____________________________________________________File loc here
# for i in range(len(df_dish["order"])):
#     kitchen.insert(parent='', index='end', values=(i, df_dish["table"][i], df_dish["order"][i], df_dish["qty"][i],
#                                                    df_dish["status"][i]))  # inserting values to treeview

root.mainloop()  # _____________Keeps the root window in loop
