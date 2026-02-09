import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from generation import Generation


class GAVis:
    def __init__(self, ga, master=None):
        self.generation = Generation.firstGeneration()
        self.generationNum = 0

        if master:
            self.root = tk.Toplevel(master)
        else:
            self.root = tk.Tk()
        self.root.title("Genetic Algorithm - TSP")

        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.G = nx.Graph()
        self.pos = {name: (city.coords[0], city.coords[1]) for name, city in ga.items()}
        self.G.add_nodes_from(self.pos.keys())

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Restart", command=self.reset, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Next Gen", command=self.next_gen, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Auto x10", command=self.auto_run, width=12).pack(side=tk.LEFT, padx=5)

        self.leaderboard_frame = tk.Frame(self.root)
        self.leaderboard_frame.pack(pady=5)
        self.draw()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.destroy()
        try:
            import sys
            sys.exit(0)
        except Exception:
            pass

    def draw(self, route=None):
        self.ax.clear()
        nx.draw(self.G, self.pos, with_labels=True, node_size=500, ax=self.ax)

        colors = ["red", "blue", "green", "orange", "purple"]
        top_routes = self.generation.get_top_routes(5)
        for i, solution in enumerate(top_routes):
            r = ["A"]+solution.route
            edges = [(r[i], r[i+1]) for i in range(len(r)-1)]
            edges.append((r[-1], r[0]))
            nx.draw_networkx_edges(self.G, self.pos, edgelist=edges, edge_color=colors[i], width=2, ax=self.ax, alpha=0.5 if i > 0 else 1.0)

        best = top_routes[0]
        if best:
            self.ax.set_title(f"Generation {self.generationNum}")
        else:
            self.ax.set_title("Generation 0")

        self.canvas.draw()

        for widget in self.leaderboard_frame.winfo_children():
            widget.destroy()
        tk.Label(self.leaderboard_frame, text="Leaderboard (Top 5)", font=("Arial", 12, "bold")).pack()
        for i, r in enumerate(top_routes):
            dist = r.testSolution()
            route_str = " → ".join(r.route)
            tk.Label(
                self.leaderboard_frame,
                text=f"{i+1}. {route_str}",
                fg=colors[i],
                font=("Arial", 10)
            ).pack(anchor="w")

    def next_gen(self):
        self.generationNum += 1
        self.generation = self.generation.nextGeneration()

        self.draw()

    def auto_run(self):
        for _ in range(10):
            self.next_gen()

    def reset(self):
        self.generation= Generation.firstGeneration()
        self.generationNum = 0
        self.draw()

    def start(self):
        self.root.mainloop()
