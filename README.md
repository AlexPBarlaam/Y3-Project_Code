# Year 3 University Project

This project was completed as part of my Bachelor's degree at the University Of Lincoln and was titled "Determining the viability of a non-stopping railway system on the UK Railway Network using computer-generated simulations"

# Background

The basis for this project was the investigation of a non-stopping railway system against a traditional system using simulations. [This article](https://weburbanist.com/2015/01/15/non-stop-rail-2-future-trains-pick-up-passengers-in-motion/) will give you more insight on the former (I will stress that it is a purely theorical railway concept) whilst the latter is the railway as we know it today. Both systems are simulated to draw a comparison between them and the kind of improvements the concept idea mentioned in the article could offer.

The Dissertation written for this project is also available in the repo to read. 

It is also important to mention that this is a second-based simulation, the speed of the trains are recorded in m/s ,and all distances are in meters. All trains run at 40 m/s which is about 90mph.

Let's get onto the code and how it works. 

# Classes

The Simulation uses an Object-Oriented approach. It centers around Project_Main.py and Simulation.py which instantiate all classes and run the simulation respectively. The other classes hold data used by the simulation. The entity-relationship diagram below details all the classes, their attributes & methods, and how they relate to one another.  

![Entity-Relationship Chart](Chart\ER_Diagram.png)


# Algorithm
As previously stated, Simulation.py runs the simulation and uses 4 methods to do so. These are as follows: 

- SimStart
    - This is the method that starts the simulation which Project_Main.py calls when all the classes are instantiated.
    - A while loop iterates until the attribute "time" reaches 3700 (the time it takes for all 4 trains simulated to run the lenght of the line). Each iteration does the following:
        - Produces a deep copy of the previous state and adds it to histState. This keeps a log of the state of each train at the end of each time tick
        - Increment "time" by 1
        - calls the Step method

- Step
    - checks the state of each train (stored in the class "State") and updates the positions accordingly by calling UpdatePos or UpdateDist (methods from the class Position).
    - additionally, if a train reaches a station, the next rail link is found by calling either NextLinkUp or NextLinkDown depending on the direction of travel

- NextLinkUp & NextLinkDown    
    - These two methods do very similar things. They find the next railway link when a reaches a station so it can be routed further down the line. 
    - Each Link has a direction and a number which in conjunction can be used to find the relevant link for the train to go along.
        - Up and Down are railway terminology meaning towards a major destination and away from a major destination respectively. This is usually London.

# Train states

In the previous paragraph, it was mentioned that trains can be in multiple states. There are two possible states:
- If the distance is 0, the link is None and a station is displayed, this indicates the train is stopped at a station
- If the distance is a number other than 0, a link is displayed and station is set to None, this indicates the train is travelling along a link.

# Operation
If you wish to download and operate this, you will need to download all .py files in the repo. Run Project_Main.py and you should see something like this. 

![Example Compile](Chart\Example_Compile.png)

The information printed on the screen shows when a train has changed state and at which time stamp and which train it was. In the example above, both train 1 and 2 started travelling along links at time stamp 1 and train 1 stopped at cambridge north 94 seconds later and so on.

Before the simulation concludes, It will print the last state of each train.

![Example State](Chart\Example_State.png)

Looking at the first state, the first line under the index (train1) displayed 0, second displayed None and third displayed a station showing that this train was stopped at a station.

