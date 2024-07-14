import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox #used for testing purposes: the later buttonclick function will go to the real GUI but for now I just want a confirmation message

#Create the main frame of the program
root = Tk()
root.geometry('1050x500')
root.title('Button selection')

style = Style()
style.configure('W.TButton', font='calibri', background='red')

#Define a function to display confirmation message when either button clicked
def confirm_message_view():
    messagebox.showinfo('Message', 'This is a confirmation message for VIEW MODE')

def confirm_message_edit():
    messagebox.showinfo('Message', 'This is a confirmation message for EDIT MODE')

#Create buttons for view and edit mode, then pack them
view_mode = Button(root, text='View Mode', command=confirm_message_view, style='W.TButton')
view_mode.grid(row = 1, column = 1, sticky = W, padx = 50, pady = 50)
edit_mode = Button(root, text='Edit Mode', command=confirm_message_edit, style='W.TButton')
edit_mode.grid(row = 1, column = 2, sticky = E, padx = 50, pady = 50)

root.mainloop()

#adding a line to save the repository
