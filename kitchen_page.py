from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import os

def confirm(*args):
    df_dish = pd.read_csv("CSV\\Kitchen.csv")                        #______________________________________________File Loc Here
    x = kitchen.item(kitchen.selection())['values'][0]
    df_dish.loc[x,"status"] = True
    df_dish.to_csv("CSV\\Kitchen.csv", index=False)

#_________________________________________Order Confirmation
    confirm_frame = Toplevel(relief='ridge', bd=20, bg='grey')
    confirm_frame.title("Billing Confirmation")
    confirm_frame.geometry("650x100+600+400")
    confirm_label = Label(confirm_frame, text="===== Order is ready to be served =====", font=('Arial', 20, 'bold'), bd=15, relief='groove',pady=5)
    confirm_label.pack()
    refresh()


def refresh():
    kitchen.delete(*kitchen.get_children())
    df_dish = pd.read_csv("CSV\\Kitchen.csv")  # ________________________________________________________________________File Loc Here
    for i in range(len(df_dish["order"])):
        kitchen.insert(parent='', index='end', values=(i, df_dish["table"][i], df_dish["order"][i], df_dish["qty"][i],
                                                       df_dish["status"][i]))  # inserting new values to treeview


def cancel():
    df_dish = pd.read_csv("CSV\\Kitchen.csv")  # ______________________________________________File Loc Here
    x = kitchen.item(kitchen.selection())['values'][0]

    df_dish.drop(x, inplace=True)
    df_dish.to_csv("CSV\\Kitchen.csv", index=False)  # ______________________________________________File Loc Here

    # __________________________________________________________________Order cancellation
    cancel_win_frame = Toplevel(relief='ridge', bd=20, bg='grey')
    cancel_win_frame.title("Billing Confirmation")
    cancel_win_frame.geometry("650x100+600+400")
    cancel_win_label = Label(cancel_win_frame, text="===== Order is Cancelled =====", font=('Arial', 20, 'bold'), bd=15,
                             relief='groove', pady=5)
    cancel_win_label.pack()
    refresh()


def home():
    os.system('python home_page.py')

tab_n = [1, 2, 3, 4]
root = Tk()
root.title("KITCHEN")
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
title_label = Label(title, font=('Algerian', 60, 'bold'), bg='grey', text="KITCHEN", justify=CENTER)
title_label.pack(pady=20)

# Left Partition
left = Frame(root, width=3 / 4 * w, height=t, bd=15, relief='ridge', bg='grey')
left.pack(side=LEFT)
left.pack_propagate(0)

# Right Partition
right = Frame(root, width=w / 4, height=t, bd=15, relief='ridge', bg='grey')
right.pack(side=RIGHT)
right.pack_propagate(0)

# Frame and Label for pending orders
pending_frame = Frame(left, width=3 / 4 * w, height=90, bd=18, relief='ridge', bg='grey')
pending_frame.pack(side=TOP)
pending_frame.pack_propagate(0)
Label(pending_frame, text="Pending Orders:", font=('algerian', 35, 'bold'), bg='grey', justify=CENTER).pack()

# Frame for menu
menu = Frame(left, width=3 / 4 * w, height=t - 90, bd=15, relief='raised', bg='grey')
menu.pack(side=BOTTOM)
menu.grid_propagate(0)
menu.pack_propagate(0)

# Display window for Orders
style = ttk.Style()
style.configure("Treeview", highlightthickness=0, bd=10, font=('Garamond', 21, 'bold'),
                rowheight=45)  # Modify the font of the body
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

# Right Window GUI
right_frame = Frame(right, width=w / 2, height=t, bd=15, relief='raised', bg='grey')
right_frame.pack(side=RIGHT)
right_frame.pack_propagate(0)

# Done Button GUI
done_button_frame = Frame(right_frame, width=w / 4, height=1, bd=10, relief='sunken', bg='grey')
done_button_frame.pack(side=TOP, pady=50)
done = Button(done_button_frame, text="DONE", width=20, height=1, font=('Arial', 20, 'bold'), command=confirm)
done.pack()

# Refresh Button GUI
refresh_button_frame = Frame(right_frame, width=w / 4, height=1, bd=10, relief='sunken', bg='grey')
refresh_button_frame.pack(side=TOP, pady=30)
refresh_button = Button(refresh_button_frame, text="REFRESH", width=20, height=1, font=('Arial', 20, 'bold'),command=refresh)
refresh_button.pack()

# Home Button GUI
home_button_frame = Frame(right_frame, width=w / 4, height=1, bd=10, relief='sunken', bg='grey')
home_button_frame.pack(side=BOTTOM, pady=50)
home_button = Button(home_button_frame, text="HOME", width=20, height=1, font=('Arial', 20, 'bold'),command=home)
home_button.pack()

# Cancel Button GUI
cancel_button_frame = Frame(right_frame, width=w / 4, height=1, bd=10, relief='sunken', bg='grey')
cancel_button_frame.pack(side=BOTTOM, pady=20)
cancel_button = Button(cancel_button_frame, text="CANCEL ORDER", width=20, height=1, font=('Arial', 20, 'bold'),command=cancel)
cancel_button.pack()

root.mainloop()
