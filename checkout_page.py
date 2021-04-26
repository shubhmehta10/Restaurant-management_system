# import libraries
from tkinter import *
import pandas as pd
import tkinter.ttk as ttk
from datetime import datetime

# GST (Tax) VARIABLE
GST = 0.18
# Function for when button is pressed
def button_bill() :
    # Reading CSV file
    df_bill = pd.read_csv("CSV\\Kitchen.csv")  # _______________________FILENAME(Bill)
    df_return = pd.read_csv("CSV\\Kitchen.csv")  # _______________________FILENAME(Return)
    df_bill["amount"] = df_bill["qty"] * df_bill["price"]

    for i in range(len(df_bill["amount"])) :
        if int(df_bill["table"][i]) != int(table.get()) :  # Dropping unwanted table orders from bill
            df_bill.drop(i, inplace=True)

        elif df_bill["status"][i] == False :  # Checking if all orders are done
            # _________________Pop-up for unfulfilled orders
            unfulfilled = Toplevel(relief='ridge', bd=20, bg='grey')
            unfulfilled.title("ORDER UNFULFILLED")
            unfulfilled.geometry("650x120+550+400")
            unfulfilled.resizable(0, 0)
            unfulfilled_label = Label(unfulfilled, text="===== Orders are pending for this table!!! =====",
                                      font=('Arial', 16, 'bold'), bd=15, relief='groove', pady=20)
            unfulfilled_label.pack()
            return

        elif int(df_bill["table"][i]) == int(table.get()) :  # Dropping paid orders from Kitchen.CSV
            df_return.drop(i, inplace=True)

    df_bill.drop(["table", "status"], axis=1, inplace=True)  # Dropping Table number and Order status from final bill

    now = datetime.now()  # datetime object containing current date and time
    df_bill["time"] = now.replace(microsecond=0)  # Adding Timestamp to database

    # Updating KITCHEN and DATABASE CSV FILES
    df_return.to_csv("CSV\\Kitchen.csv",
                     index=False)  # ___________________________________FILENAME
    df_bill.to_csv('CSV\\Database.csv', mode='a', header=False,
                   index=False)  # ____________FILENAME

    if df_bill["amount"].sum() == 0 :  # Checking if table has any orders to charge a bill
        # ___________________Pop-up for no orders
        no_order_frame = Toplevel(relief='ridge', bd=20, bg='grey')
        no_order_frame.title("NO ORDERS")
        no_order_frame.geometry("650x120+550+400")
        no_order_frame.resizable(0, 0)
        no_order_label = Label(no_order_frame, text="===== No Orders Have been placed for this Table!!! =====",
                               font=('Arial', 16, 'bold'), bd=15, relief='groove', pady=20)
        no_order_label.pack()
        return

    df_bill.drop(["time"], axis=1, inplace=True)  # Removing Timestamp from dataframe

    # _______________________________________Final Bill window information
    BillWindow = Toplevel(root)
    BillWindow.title("Table" + table.get())
    BillWindow.geometry("750x350")
    BillWindow.resizable(0, 0)

    # ____________________________________Frame for Treeview
    bill_frame = Frame(BillWindow, width=750, height=350, bd=15, relief='ridge', bg='grey')
    bill_frame.pack()
    bill_frame.pack_propagate(0)

    # ________________________________________style configuration for treeview
    style = ttk.Style()
    style.configure("Treeview", font=('Consolas', 13))
    style.configure("Treeview.Heading", font=('Consolas', 16))

    # _______________________________________Constructing Treeview
    bill = ttk.Treeview(bill_frame, columns=("Order", "Qty", "Price", "Amount"), height=10, selectmode='none')
    bill['show'] = 'headings'
    bill.pack()
    bill.pack_propagate(0)
    bill.column("0", width=300)
    bill.column("1", width=90, anchor='n')
    bill.column("2", width=150, anchor='n')
    bill.column("3", width=200, anchor='n')
    bill.heading("0", text="Order")
    bill.heading("1", text="Qty")
    bill.heading("2", text="Price")
    bill.heading("3", text="Amount")

    # _____________________Printing Bill Amount
    Label(bill_frame, bg='white', anchor="w", font=('Consolas', 12), justify=LEFT, width=300, height=5,
          text="Total Amount = Rs." + str(df_bill["amount"].sum()) +  # Total and GST inclusion
               "\nGST = Rs." + str((df_bill["amount"].sum() * GST).round(2)) + " (" + str(100 * GST) + "%)"
                                                                                                       "\nTo be paid = Rs." + str(
              (df_bill["amount"].sum() * (GST + 1)).round(2)) +
               "\t\t\t\tDate/Time: " + str(now.replace(microsecond=0))).pack(side=BOTTOM)

    # _____________________Inserting Order summary to bill treeview
    df_bill.index = range(0, len(df_bill["order"]))
    for j in range(len(df_bill["order"])) :
        bill.insert(parent='', index=0, values=(
            df_bill["order"][j], df_bill["qty"][j], float(df_bill["price"][j]), float(df_bill["amount"][j])))


# Main Window
root = Tk()
root.title("CHECKOUT")  # ____Header Title
root.resizable(0, 0)  # Disabling Resizing of window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  # Width and height according to users PC
root.geometry("300x300")  # Defining Window Geometry

tab_no = [1, 2, 3, 4]  # __________________LIST OF TABLE NUMBERS

# Bill Window Frame
mainframe = Frame(root, width=300, bd=15, height=300, relief='ridge', bg='grey')
mainframe.pack()
mainframe.pack_propagate(0)
mainframe_label = Label(mainframe, font=('Algerian', 20, 'bold'), bg='white', text="Check Out", justify=CENTER)
mainframe_label.pack(pady=20)

# _____________________________Selected Table number call is "table.get()"__________________________#
table = StringVar(root)

# _____________________Option Menu to select Table number
table.set('Table Number')  # set the default option to 1
popupMenu = OptionMenu(mainframe, table, *tab_no)
popupMenu.configure(bd=3, font=('Arial', 15, 'bold'))
popupMenu.pack(pady=30)

# CHECKOUT Button
button = Button(mainframe, text="Print Bill", command=button_bill, font=('Arial', 12, 'bold'), bd=5)
button.pack(side=BOTTOM,pady=30)
root.mainloop()  # _____________Keeps the root window in loop
