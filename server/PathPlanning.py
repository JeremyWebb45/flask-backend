import numpy as np

class PathPlanningController:
    def __init__(self):
        self.height = 100;
        self.width = 100;
        self.grid = np.zeros((self.width, self.height)).tolist()
    
    def getGrid(self):
        return self.grid
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width