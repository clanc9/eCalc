#!/usr/bin/env python

import tkinter as tk
import guicalc

def main():
    calcWindow = tk.Tk()
    calcWindow.title("Calculatrice")
    calcWindow.geometry("400x300")
    app = guicalc.GuiCalculator(parent=calcWindow)
    calcWindow.mainloop()

main()
