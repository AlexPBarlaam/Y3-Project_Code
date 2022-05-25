class Network:
    
    def __init__(self, nN, sA, sL) -> None:        
        """Network Constructor (Represents Railway Network)

        Args:
            nN (string): Name of network
            sA (Station objects Array): Stations on the network
            sL (StationLink objects Array): Station links on the network
        """

        self.netName = nN
        self.stationsArray = sA #List of objects of type Station
        self.stationsLinks = sL #List of objects of type StationLinks

    def __str__(self) -> str:       
        """Network ToString Method 

        Returns:
            string: text representation of Network attributes
        """
        
        string = "the " + self.netName + " is a railway line between " + self.stationsArray[0].Name + " and " + self.stationsArray[-1].Name
        return string

    
        


        
