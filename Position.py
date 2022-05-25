class Position: 

    def __init__(self, s, l, d) -> None:        
        """Position Constructor (Stores the position of a single train)
        Args:
            s (Station Object): Station train is at if stopped
            l (StationLink Object): Link train is travelling on 
            d (int): distance of train along the link 
        """

        self.station = s
        self.link = l
        self.distance = d

    def UpdatePos(self, s, l, d) -> None:
        """Updates the position of the train

        Args:
            s (Station Object): Station train is at if stopped
            l (StationLink Object): Link train is travelling on 
            d (int): distance of train along the link 
        """

        self.station = s
        self.link = l
        self.distance = d

    def UpdateDist(self, d) -> None:
        """Updates the distance of a train along a link
        
        Args:
            d (int): distance of train along the link             
        """
        self.distance = d