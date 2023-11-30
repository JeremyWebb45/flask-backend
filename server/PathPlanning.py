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
        np.put(self.grid, self.start_state, 1)
        np.put(self.grid, self.goal_state, 2)
        print(self.grid[np.where(self.grid == 0)].shape, np.random.choice(a=[0, 3], size=((self.width, self.height)), p=[self.obstacle_density, 1 - self.obstacle_density]).shape)
        self.grid[np.where(self.grid == 0)] = np.random.choice(a=[0, 3], size=((self.width, self.height)), p=[self.obstacle_density, 1 - self.obstacle_density])
        print(self.grid)
        print(np.count_nonzero(self.grid == 3))
        return "<div></div>"