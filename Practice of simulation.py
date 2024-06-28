import tkinter as tk
import random
import math

class Hyphae:
    def __init__(self, x, y, angle, length=10, thickness=2):
        self.x = x
        self.y = y
        self.angle = angle
        self.length = length
        self.thickness = thickness

    def grow(self):
        self.x += self.length * math.cos(self.angle)
        self.y += self.length * math.sin(self.angle)

class HyphaeSimulator:
    def __init__(self, root, width=800, height=600, max_hyphae=100, crit_dist=20, branch_prob=0.5, thickness=2):
        self.root = root
        self.width = width
        self.height = height
        self.max_hyphae = max_hyphae
        self.crit_dist = crit_dist
        self.branch_prob = branch_prob
        self.thickness = thickness
        
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        
        start_x, start_y = self.width // 2, self.height // 2
        self.hyphae = [Hyphae(start_x, start_y, random.uniform(0, 2 * math.pi), thickness=thickness)]
        self.running = False
        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()

    def start(self):
        if not self.running:
            self.running = True
            self.grow_hyphae()

    def stop(self):
        self.running = False

    def grow_hyphae(self):
        if not self.running:
            return
        
        new_hyphae = []
        for hypha in self.hyphae:
            x, y = hypha.x, hypha.y
            hypha.grow()
            nx, ny = hypha.x, hypha.y

            if 0 <= nx < self.width and 0 <= ny < self.height:
                self.canvas.create_line(x, y, nx, ny, width=hypha.thickness, fill='brown')
                
                if random.random() < self.branch_prob and len(self.hyphae) + len(new_hyphae) < self.max_hyphae:
                    new_angle = hypha.angle + random.uniform(-math.pi/4, math.pi/4)
                    new_hyphae.append(Hyphae(nx, ny, new_angle, hypha.length, hypha.thickness))
                    
                hypha.angle += random.uniform(-math.pi/16, math.pi/16)  # Small turn for the hypha

        self.hyphae.extend(new_hyphae)
        self.hyphae = self.hyphae[-self.max_hyphae:]
        
        self.root.after(100, self.grow_hyphae)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mushroom Hyphae Growth Simulator")
    
    simulator = HyphaeSimulator(root)
    
    root.mainloop()