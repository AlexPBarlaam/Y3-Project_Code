import copy as C

class Simulation:
       
    def __init__(self, n, t, SI, tr) -> None:
        """Simulation Constructor (Runs the Simulation)

        Args:
            n (Network Object): Network to host Simulation
            t (Timetable Object): Simulation Timetable
            SI (State Object): Represent Simulation State at a point in time
            tr (list of Train Objects): Trains used by the simulation
        """

        self.simRun = True
        self.network = n
        self.timetable = t
        self.trains = tr
        self.time = 0; 
        self.state = SI #this has to be an instance of the state class
        self.histState = {} #dictionary of previous states 

    def simStart(self) -> None:
        """Starts and Runs the Simulation
        """
        
        '''loop
            historical state = state.copy HAS TO BE DEEP COPY 
            append historical state to historical states array
            time = time + 1 
            calls step to update the state of simulation
        starts the step '''
        
        while self.simRun == True:
            self.histState.update({self.time : C.deepcopy(self.state)}) 
            self.time += 1
            #print("time = " + str(self.time))
            self.step()
            

    def step(self) -> None: 
        """updates the positions
        """

        timesIndex = 0 #index for timetable
        
        for key in self.state.pos:
            pos = self.state.pos[key]
            velocity = self.state.velocity[key]
            times = self.timetable.departures[timesIndex]

            #(Used for testing)
            #if self.time == 1062 and key == "train1": 
            #   print("breakpoint here")


            try:
                if velocity == 0 and pos.link == None and times[pos.station.Name] == self.time:
                    if self.trains[key].direction == "down":
                        nextLink = self.nextLinkDown(pos.station)
                    elif self.trains[key].direction == "up":
                        nextLink = self.nextLinkUp(pos.station)
                    print(nextLink) 
                    print(key + " @ " + str(self.time))               
                    pos.UpdatePos(None, nextLink, 0)
                    self.state.velocity[key] = self.trains[key].maxVelocity
            except KeyError:
                pass        

            if velocity != 0 and pos.station == None:
                newDist = pos.distance + velocity
                #print("newdist = " + str(newDist))
                pos.UpdateDist(newDist)
           

            if pos.link != None:                
                if pos.link.linkDistanceMeters <= pos.distance:
                    #print("should go to next link") 
                                
                    if self.trains[key].direction == "down":
                        self.trains[key].stationListIndex += 1
                        station = self.network.stationsArray[self.trains[key].stationListIndex]
                        print(station)
                        print(key + " @ " + str(self.time))
                        pos.UpdatePos(station, None, 0)
                        self.state.velocity[key] = 0

                    elif self.trains[key].direction == "up":
                        self.trains[key].stationListIndex -= 1
                        station = self.network.stationsArray[self.trains[key].stationListIndex]
                        print(station) 
                        print(key + " @ " + str(self.time))
                        pos.UpdatePos(station, None, 0)
                        self.state.velocity[key] = 0

            if self.time == 3700:
                self.simEnd()
            
            timesIndex += 1
            #print("step ended")
            

    def simEnd(self) -> None:
        """Terminates the Simulation
        """

        self.simRun = False
    
    def nextLinkDown(self, station):
        for link in station.links:
            if link.originStation.Name == station.Name:
                return link
    
    def nextLinkUp(self, station):
        for link in station.links:
            if link.originStation.Name == station.Name and link.direction == "Up":
                return link
            elif link.destStation.Name == station.Name and link.direction == "Bi-Dir":
                return link 

    def GetHistState(self):
        return self.histState