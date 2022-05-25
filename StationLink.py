class StationLink:

    def __init__(self, oS, dS, lDm, D) -> None:
        """StationLink Constructor (Represents rail links between station)

        Args:
            oS (Station Object): Link Origin Station
            dS (Station Object): Link Destination Station
            lDm (Int): Lenght of Link
            D (Str): Direction of link (Has to be "down" or "up" or "Bi-Dir")
        """
                
        self.originStation = oS
        self.destStation = dS
        self.linkDistanceMeters = lDm
        self.direction = D
    
        
    def __str__(self) -> str:
        """StationLink ToString Method

        Returns:
            str: text representation of StationLink attributes
        """
        string = "this is a "+ str(self.linkDistanceMeters) +" m long link between " + self.originStation.Name + " and " + self.destStation.Name
        return string
