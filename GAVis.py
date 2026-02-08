import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GAVis:
    def __init__(self, ga, master=None):
        self.ga = ga
        self.ga.initPopulation()
        self.generation = 0

        # Use Toplevel if master is provided, else fallback to Tk
        if master:
            self.root = tk.Toplevel(master)
        else:
            self.root = tk.Tk()
        self.root.title("Genetic Algorithm - TSP")

        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.G = nx.Graph()
        self.pos = {name: (city.x, city.y) for name, city in ga.cities.items()}
        self.G.add_nodes_from(self.pos.keys())

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Restart", command=self.reset, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Next Gen", command=self.next_gen, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Auto x10", command=self.auto_run, width=12).pack(side=tk.LEFT, padx=5)

        self.leaderboard_frame = tk.Frame(self.root)
        self.leaderboard_frame.pack(pady=5)
        self.draw()

        # Bind close event to ensure app exits
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.destroy()
        # If this is the last window, exit the app
        try:
            import sys
            sys.exit(0)
        except Exception:
            pass

    def draw(self, route=None):
        self.ax.clear()
        nx.draw(self.G, self.pos, with_labels=True, node_size=500, ax=self.ax)

        colors = ["red", "blue", "green", "orange", "purple"]
        top_routes = self.ga.get_top_routes(5)
        for idx, r in enumerate(top_routes):
            edges = [(r[i], r[i+1]) for i in range(len(r)-1)]
            edges.append((r[-1], r[0]))
            nx.draw_networkx_edges(self.G, self.pos, edgelist=edges, edge_color=colors[idx], width=2, ax=self.ax, alpha=0.5 if idx > 0 else 1.0)

        best = self.ga.best
        if best:
            dist = self.ga.routeDistance(best)
            self.ax.set_title(f"Generation {self.generation} | Best Distance: {dist:.2f}")
        else:
            self.ax.set_title("Generation 0")

        self.canvas.draw()

        # Update leaderboard
        for widget in self.leaderboard_frame.winfo_children():
            widget.destroy()
        tk.Label(self.leaderboard_frame, text="Leaderboard (Top 5)", font=("Arial", 12, "bold")).pack()
        for idx, r in enumerate(top_routes):
            dist = self.ga.routeDistance(r)
            route_str = " → ".join(r)
            tk.Label(
                self.leaderboard_frame,
                text=f"{idx+1}. {route_str} | Distance: {dist:.2f}",
                fg=colors[idx],
                font=("Arial", 10)
            ).pack(anchor="w")

    def next_gen(self):
        self.generation += 1
        best = self.ga.evolve()
        self.draw(best)

    def auto_run(self):
        for _ in range(10):
            self.next_gen()

    def reset(self):
        self.ga.initPopulation()
        self.ga.best = None
        self.generation = 0
        self.draw()

    def start(self):
        self.root.mainloop()
