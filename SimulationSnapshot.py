class SimulationSnapshot():

    def __init__(self,SD) -> None:
        """SimulationSnapshot Constructor

        Args:
            SD (Dict of states): States from the simulation after it has concluded
        """
        
        self.stateDict = SD
        

    def getState(self,timeIndex):
        """Method to print a state at time x

        Args:
            timeIndex (int): timekey to access a state from the dict
        """

        print(self.stateDict[timeIndex])

        
