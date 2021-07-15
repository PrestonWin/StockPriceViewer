#! /usr/bin/env python3
from tkinter import *
from yahoo_fin import stock_info as si

root = Tk()
root.title("Simple Stock/Coin Price Viewer")

# getPrice(): gets user input from input field and trys to get
#             price of stock, returns price of stock/coin or
#             outputs error if stock/coin cannot be found
def getPrice(event=None):
    try:
        data = si.get_live_price(input.get())
        price.config(text="$" + str(round(data, 6)))
    except:
        price.config(text="Invalid Stock/Couldn't find")


# clear(): Clears input field and label containing price
def clear(event=None):
    price.config(text="")
    input.delete(0, END)


# Button to get and place "Get Price" button
get = Button(root, text="Get Price", command=getPrice)
get.bind("<Return>", getPrice)
get.grid(row=0, column=0)

# Input field to get input from user
input = Entry(0, width=20)
input.bind("<Return>", getPrice)
input.grid(row=0, column=1)


# Clear button that clears input and label
clear = Button(root, text="Clear", command=clear, padx=12)
clear.grid(row=2, column=0)

# Label to dispaly price of stock
price = Label(root, text="")
price.grid(row=2, column=1, columnspan=1)


root.mainloop()
