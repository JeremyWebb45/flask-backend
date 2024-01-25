import numpy as np

class PathPlanningController:
    def __init__(self):
        self.height = 100;
        self.width = 100;
        self.start_state = (0,0)
        self.goal_state = (0,0)
        self.obstacle_density = .5
        self.grid = np.zeros((self.width, self.height))
    
    def getGrid(self):
        return self.grid
    
    def getGridForClient(self):
        return self.grid.tolist()
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def generateObstacles(self, startState, goalState, density):
        self.start_state = eval(startState)
        self.goal_state = eval(goalState)
        self.obstacle_density = eval(density)
        self.grid = np.random.binomial(1, self.obstacle_density, self.grid.shape) * 3
        self.grid[self.start_state[1]][self.start_state[0]] = 1
        self.grid[self.goal_state[1]][self.goal_state[0]] = 2