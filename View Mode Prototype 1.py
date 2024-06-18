#this will be within a function in the main program
#the function will run when the 'view mode' button is clicked
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random
import time

#Create main frame of program - should fill entire window
root = Tk()
root.geometry('2000x2000')
root.title('View Mode')

#Create labels to show what each input box represents
lblMaxHyphae = Label(root, text = 'Enter maximum hyphae (1-400): ')
lblCritDist = Label(root, text = 'Enter critical distance between hyphae for turning (1-4): ')
lblBranchSplit = Label(root, text = 'Enter probability of branch splitting (between 0 and 1): ')
lblThickness = Label(root, text = 'Enter hyphae thickness (1-10): ')

#Create input boxes
txtMaxHyphae = Entry(root)
txtCritDist = Entry(root)
txtBranchSplit = Entry(root)
txtThickness = Entry(root)

#Geometry of labels and input boxes
lblMaxHyphae.grid(row = 0, column = 0, sticky = W, pady = 2)
lblCritDist.grid(row = 1, column = 0, sticky = W, pady = 2)
lblBranchSplit.grid(row = 2, column = 0, sticky = W, pady = 2)
lblThickness.grid(row = 3, column = 0, sticky = W, pady = 2)

txtMaxHyphae.grid(row = 0, column = 1, pady = 2)
txtCritDist.grid(row = 1, column = 1, pady = 2)
txtBranchSplit.grid(row = 2, column = 1, pady = 2)
txtThickness.grid(row = 3, column = 1, pady = 2)

#Validation functions for each input variable
def MaxHyphaeValid():
    errorMaxHyphae = False
    errorCritDist = False
    errorBranchSplit = False
    errorThickness = False
    if txtMaxHyphae > 0 and txtMaxHyphae <= 400:
        if txtMaxHyphae == '':
            errorMaxHyphae=True
            errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness)
            txtMaxHyphae = 150
        else:
            txtMaxHyphae = int(txtMaxHyphae)
    else:
        errorMaxHyphae=True
        errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness)
        txtMaxHyphae = 150

def CritDistValid():
    errorMaxHyphae = False
    errorCritDist = False
    errorBranchSplit = False
    errorThickness = False
    if txtCritDist > 0 and txtCritDist <= 4:
        if txtCritDist == '':
            errorCritDist = True
            errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness)
            txtCritDist = 2.5
        elif txtCritDist.len() > 4:
            round(txtCritDist, 3)
    else:
        errorCritDist = True
        errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness)
        txtCritDist = 2.5

def BranchSplitValid():
    errorMaxHyphae = False
    errorCritDist = False
    errorBranchSplit = False
    errorThickness = False
    if txtBranchSplit > 0 and txtBranchSplit < 1:
        if txtBranchSplit == '':
            errorBranchSplit = True
            errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness)
            txtBranchSplit = 0.5
        elif txtBranchSplit.len() > 4:
            round(txtBranchSplit, 3)
    else:
        errormessage(errorBranchSplit=True)
        txtBranchSplit = 0.5
        
def ThicknessValid():
    errorMaxHyphae = False
    errorCritDist = False
    errorBranchSplit = False
    errorThickness = False
    if txtThickness > 0 and txtThickness <= 10:
        if txtThickness == '':
            errorThickness - True
            errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness)
            txtThickness = 3
        else:
            txtThickness = int(txtThickness)
    else:
        errorThickness - True
        errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness)
        txtThickness = 3

def errormessage(errorMaxHyphae, errorCritDist, errorBranchSplit, errorThickness):
    errorlabel = Label(root)
    if errorMaxHyphae==True:
        errorlabel == Label(root, text='Error with maximum hyphae')
        errorlabel.grid(row = 0, column = 3, sticky = W, pady = 2)
    elif errorCritDist==True:
        errorlabel == Label(root, text='Error with critical distance')
        errorlabel.grid(row = 1, column = 3, sticky = W, pady = 2)
    elif errorBranchSplit==True:
        errorlabel == Label(root, text='Error with branch split')
        errorlabel.grid(row = 2, column = 3, sticky = W, pady = 2)
    elif errorThickness==True:
        errorlabel == Label(root, text='Error with thickness')
        errorlabel.grid(row = 3, column = 3, sticky = W, pady = 2)
        
#Create a run button for the program
runbutton = Button(root, text='Run', command=lambda: [MaxHyphaeValid(), CritDistValid(), BranchSplitValid(), ThicknessValid()])
runbutton.grid(row = 4, column = 0, sticky = E, pady = 2)
if runbutton == True:
    MaxHyphaeValid()
    CritDistValid()
    BranchSplitValid()
    ThicknessValid()
    errormessage()

root.mainloop()