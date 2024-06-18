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
        self.fact_label.pack(padx=30, pady=30)
        
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

if __name__ == '__main__':
    def Infodisplay(InfoBox, facts):
        
        root = tk.Tk()
        root.title('Information box practice')
        app = InfoBox(root, facts)
        root.mainloop()
    Infodisplay(InfoBox, facts)