import random

from city import City

class GA:

    def __init__(self, cities: dict[str,City], startNode: City, popSize=50):
        self.cities = cities
        self.startNode = startNode
        self.popSize = popSize
        self.population = []
        self.best = None

    def get_top_routes(self, n=5):
        sorted_routes = sorted(self.population, key=self.routeDistance)
        return sorted_routes[:n]
    
    def initSolution(self) -> list[str]:
        lCities = list(self.cities.keys())
        lCities.remove(self.startNode.name)
        random.shuffle(lCities)
        return [self.startNode.name] + lCities

    def initPopulation(self):
        self.population = [self.initSolution() for _ in range(self.popSize)]

    def routeDistance(self, route: list[str]) -> float:
        currentnode = self.startNode
        traveledDistance = 0
        for nextnode in route:
            city = self.cities[nextnode]
            traveledDistance += currentnode.distance(city)
            currentnode = city
        traveledDistance += currentnode.distance(self.startNode)
        return traveledDistance

    def fitness(self, route):
        return  1/self.routeDistance(route)


    def select(self, k=3):
        selected = random.sample(self.population, k)
        selected.sort(key=self.routeDistance)
        return selected[0]


    def crossover(self, p1, p2):
        start = random.randint(1, len(p1) - 2)
        end = random.randint(start, len(p1) - 1)

        child = [None] * len(p1)
        child[0] = p1[0]

        child[start:end] = p1[start:end]

        fill = [city for city in p2 if city not in child]
        idx = 1
        for city in fill:
            while child[idx] is not None:
                idx += 1
            child[idx] = city

        return child


    def mutate(self, route, rate=0.1):
        if random.random() < rate:
            i = random.randint(1, len(route) - 1)
            j = random.randint(1, len(route) - 1)
            route[i], route[j] = route[j], route[i]
        return route

    def evolve(self):
        newPop = []
        for _ in range(self.popSize):
            p1 = self.select()
            p2 = self.select()
            child = self.crossover(p1, p2)
            child = self.mutate(child)
            newPop.append(child)

        self.population = newPop
        current_best = min(self.population, key=self.routeDistance)
        if self.best is None or self.routeDistance(current_best) < self.routeDistance(self.best):
            self.best = current_best
        return self.best
