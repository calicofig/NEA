import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random
import time

import tkinter as tk
import time



class InfoBox:
    def __init__(self, parent, facts, interval = 30000): #defines a function to initialise the info box
        self.parent = parent
        self.parent.title('Info:')
        #Facts to display
        self.facts = facts
        self.interval = interval
        self.current_fact_index = 0
        
        #add a label into the root to display the info on
        self.fact_label = tk.Label(parent, text=self.facts[self.current_fact_index], borderwidth=2, relief='sunken')
        self.fact_label.grid(row = 5, column = 0, sticky = W, pady=30)
        
        print('Initialisation complete')
        self.schedule_next_fact()
         
    def schedule_next_fact(self):
        # Update the fact label
        self.fact_label.config(text=self.facts[self.current_fact_index])
        # Move to the next fact by increasing fact index
        self.current_fact_index = (self.current_fact_index + 1) % len(self.facts)
        # Schedule the next update
        self.parent.after(self.interval, self.schedule_next_fact)

facts = [
    'Did you know? This simulator runs using exponential and logarithmic equations to form strands of hyphae',
    'Did you know? Scientists have found microscopic fungi that hold together plants on a cellular level in over 100 species',
    'Did you know? Each hyphae growth is determined by the hyphae around it, using a "neighbour-sensing" model to simulate growth'
]

# Create main frame of program - should fill entire window
root = Tk()
root.geometry('800x400')
root.title('View Mode')

# Create labels to show what each input box represents
lblMaxHyphae = Label(root, text='Enter maximum hyphae (1-400): ')
lblCritDist = Label(root, text='Enter critical distance between hyphae for turning (1-4): ')
lblBranchSplit = Label(root, text='Enter probability of branch splitting (between 0 and 1): ')
lblThickness = Label(root, text='Enter hyphae thickness (1-10): ')

# Create input boxes
txtMaxHyphae = Entry(root)
txtCritDist = Entry(root)
txtBranchSplit = Entry(root)
txtThickness = Entry(root)

# Geometry of labels and input boxes
lblMaxHyphae.grid(row=0, column=0, sticky=W, pady=2)
lblCritDist.grid(row=1, column=0, sticky=W, pady=2)
lblBranchSplit.grid(row=2, column=0, sticky=W, pady=2)
lblThickness.grid(row=3, column=0, sticky=W, pady=2)

txtMaxHyphae.grid(row=0, column=1, pady=2)
txtCritDist.grid(row=1, column=1, pady=2)
txtBranchSplit.grid(row=2, column=1, pady=2)
txtThickness.grid(row=3, column=1, pady=2)

#Create a frame for error messages to appear in
errorframe = Frame(root)
errorframe.grid(row=5, column=0, columnspan=2, sticky=W)

#Create a label within the frame for error messages to appear on
def errormessage(message, errorrow):
    # Display an error message at the specified row
    error_label = Label(errorframe, text=message, foreground="red")
    error_label.grid(row=errorrow, column=0, sticky=W, pady=2)

# Clear previous error messages    
def clear_errors():
    for widget in errorframe.winfo_children():
        widget.destroy()

def Valid():
    clear_errors()  # Clear any previous error messages
    errorrow = 0
    # Retrieve inputs and validate them
    try:
        max_hyphae = int(txtMaxHyphae.get())
        if not (1 <= max_hyphae <= 400):
            raise ValueError
    except ValueError:
        max_hyphae = 150
        errormessage("Max Hyphae must be an integer between 1 and 400. Defaulting to 150.")
        errorrow += 1

    try:
        crit_dist = float(txtCritDist.get())
        if not (1 <= crit_dist <= 4):
            raise ValueError
    except ValueError:
        crit_dist = 2.5
        errormessage("Critical Distance must be between 1 and 4. Defaulting to 2.5.")
        errorrow += 1

    try:
        branch_split = float(txtBranchSplit.get())
        if not (0 <= branch_split < 1):
            raise ValueError
    except ValueError:
        branch_split = 0.5
        errormessage("Branch Split probability must be between 0 and 1. Defaulting to 0.5.")
        errorrow += 1

    try:
        thickness = int(txtThickness.get())
        if not (1 <= thickness <= 10):
            raise ValueError
    except ValueError:
        thickness = 3
        errormessage("Thickness must be between 1 and 10. Defaulting to 3.")
        errorrow += 1

    print(f"Max Hyphae: {max_hyphae}, Critical Distance: {crit_dist}, Branch Split: {branch_split}, Thickness: {thickness}")

def errormessage(message):
    errorlabel = Label(root, text=message)
    errorlabel.grid(row=4, column=1, sticky=W, pady=2)

# Create a run button for the program
runbutton = Button(root, text='Run', command=Valid)
runbutton.grid(row=4, column=0, sticky=E, pady=2)

#Integrate info box into the main code
app = InfoBox(root, facts)

root.mainloop()
