import numpy as np

class PathPlanningController:
    def __init__(self):
        self.startState = (0,0);
        self.goalState = (0,1);
        self.grid = np.zeros((700,500))
    
    def getInfo(self):
        return {
            "startState": self.startState,
            "goalState": self.goalState,
            "grid": self.grid.tolist()
        }