class Train:
    
    def __init__(self, p, v, Mv, d, sI) -> None:        
        """Train Constructor

        Args:
            p (Position Object): Instance of postition class for the train
            v (int): current speed of the train
            Mv (int): max speed of the train 
            d (str): direction of train (Has to be "up" or "down")
            SI (int): Index to find stations 
        """         
        self.pos = p
        self.velocity = v
        self.maxVelocity = Mv 
        self.direction = d
        self.stationListIndex = sI