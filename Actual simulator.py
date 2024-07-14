import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random
import time
import math

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

class Hyphae:
    def __init__(self, x, y, angle, length, thickness): #initialises the class for each individual hyphae strand and their properties
        self.x = x
        self.y = y
        self.angle = angle
        self.length = length
        self.thickness = thickness
        
    def grow(self, math):
        self.x += self.length * math.cos(self.angle)
        self.y += self.length * math.sin(self.angle)
        
class Simulator:
    #initialise the simulator
    def __init__(self, root, width, height, txtMaxHyphae, txtCritDist, txtBranchProbability, Thickness):
        self.root = root
        self.width = width
        self.height = height
        self.txtMaxHyphae = txtMaxHyphae
        self.txtCritDist = txtCritDist
        self.txtBranchProbability = txtBranchProbability
        self.Thickness = Thickness
        
        #Create a canvas for the simulator to appear on
        self.canvas = tk.Canvas(root)
        self.canvas.grid(row = 0, column = 0, sticky = W, padx = 5, pady = 5)

        #The initial coordinates for the hyphae to begin at 
        starting_x = self.width // 2
        starting_y = self.height // 2

#writing a new line to save the repository
