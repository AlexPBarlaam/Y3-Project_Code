class State:
    #represents the state of the world at a point in time            
    # could be dicts of each train 
    #pos =  instance of position class 
    

    def __init__(self,t,p,v) -> None:
        """State Constructor (Represents the state of the world at a point in time)

        Args:
            t (Int): Time of the State
            p (Dictionary of Position Objects): Positions of the trains
            v (Dictionary of Ints): Velocity of the trains
        """

        self.time = t
        self.pos = p #dict of the pos of the trains
        self.velocity = v #dict of the velocity of each trains
    
    def ProtoPrinting(self):
        """Temporary Method to test printing of the class
        """
        
        print(self.pos)
        print(self.velocity)
    
    def __str__(self) -> str:
        """State toString Method

        Returns:
            str: text representation of State attributes
        """
        pass    
