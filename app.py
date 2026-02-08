import string
import random

from GAVis import GAVis
import tkinter as tk
from city import City
from geneticAlgorithm import GA

def generate_cities(n):
    cities = {}
    letters = list(string.ascii_uppercase)
    for i in range(n):
        name = letters[i % 26] + (str(i // 26) if i >= 26 else "")
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        cities[name] = City(name, x, y)  
    return cities

class TSPApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TSP Genetic Algorithm")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Number of cities:").pack(side=tk.LEFT)
        self.city_entry = tk.Entry(frame, width=5)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.insert(0, "6")  

        tk.Button(frame, text="Generate & Start", command=self.start_simulation).pack(side=tk.LEFT, padx=10)

        self.root.mainloop()

    def start_simulation(self):
        n = int(self.city_entry.get())

        cities = generate_cities(n)
        start_city = list(cities.values())[0]

        self.ga = GA(cities, start_city, popSize=50)
        self.vis = GAVis(self.ga, master=self.root)

        self.root.withdraw()
        self.vis.start()
