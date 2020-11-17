from tkinter import *
from tkinter import font

class CurrencyConverter(object):
    """
    docstring
    """
    def __init__(self) -> None:
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg = "yellow")
        Label(window, font="Helvetica 12 bold", bg = "yellow" , text = "Amount to convert").grid(row = 1, column= 1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg = "yellow" , text = "Conversion rate").grid(row= 2, column=1, sticky=W)
        Label(window, font= "Helvetica 12 bold" , bg = "yellow", text = "Converted amout").grid(row=3, column=1, sticky=W)
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable= self.amounttoConvertVar, justify=RIGHT).grid(row=1, column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable= self.conversionRateVar, justify=RIGHT).grid(row=2, column=2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmout = Label(window, font= "Helvetica 12 bold", bg = "yellow", textvariable= self.convertedAmountVar).grid(row=3, column=2, sticky=E)
        