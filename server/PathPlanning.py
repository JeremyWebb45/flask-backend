import numpy as np


class PathPlanningController:
    def __init__(self):
        self.height = 100
        self.width = 100
        self.start_state = (0, 0)
        self.goal_state = (0, 0)
        self.obstacle_density = .5
        self.grid_world = np.zeros((self.width, self.height))
        self.graph = {}

    def getGrid(self):
        return self.grid_world

    def getGridForClient(self):
        return self.grid_world.tolist()

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getPossibleNearest(self, vertex):
        keys_array = np.array([x for x in self.graph.keys()])
        euclidean_distances = np.sqrt(
            np.sum((keys_array - vertex)**2, axis=1))
        nearest_vertex = keys_array[np.argmin(euclidean_distances), :]
        return nearest_vertex

    def naiveRRT(self) -> bool:
        isSolvable = True
        # self.graph = {self.start_state: []}

        self.graph = {(np.random.choice(99), np.random.choice(99)): [], (np.random.choice(99), np.random.choice(99)): [], (np.random.choice(
            99), np.random.choice(99)): [], (np.random.choice(99), np.random.choice(99)): [], (np.random.choice(99), np.random.choice(99)): []}
        available_states = np.where(self.grid_world != 3)
        available_states = np.c_[available_states[0], available_states[1]]
        iterations = 1
        while iterations < 10:
            random_available_state = available_states[np.random.choice(
                available_states.shape[0]), :]
            nearest_vertex = self.getPossibleNearest(random_available_state)
            iterations += 1
        return isSolvable

    def generateObstacles(self, startState, goalState, density):
        self.start_state = eval(startState)
        self.goal_state = eval(goalState)
        self.obstacle_density = eval(density)
        isSolved = False
        while not isSolved:
            self.grid_world = np.random.binomial(
                1, self.obstacle_density, self.grid_world.shape) * 3
            self.grid_world[self.start_state[1]][self.start_state[0]] = 1
            self.grid_world[self.goal_state[1]][self.goal_state[0]] = 2
            isSolved = self.naiveRRT()
