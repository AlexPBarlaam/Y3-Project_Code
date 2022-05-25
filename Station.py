class Station:
    
    def __init__(self, sN) -> None:
        """Station Constructor (Represents the station on the network)

        Args:
            sN (str): Station Name
            I (int): Station Index for simulation
        """
        self.Name = sN
        self.NetName = "Fen Line"
        self.links = []

    
    def __str__(self) -> str:
        """Station ToString Method

        Returns:
            str: text representation of Station attributes
        """
        string = self.Name + " is a station on the " + self.NetName
        return string

    def SetLink(self, l) -> None:
        """Sets the links after the StationLink objects are instanciated 
        
        Args:
            l (StationLink Object List) : Links available at station
        """
        self.links = l