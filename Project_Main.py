
from Position import Position
from SimulationSnapshot import SimulationSnapshot
from Station import Station
from StationLink import StationLink
from Network import Network
from Timetable import Timetable
from Simulation import Simulation
from State import State
from Train import Train


Cambridge = Station("Cambridge")
Cambridge_N = Station("Cambridge North")
Waterbeach = Station("Waterbeach")
Ely = Station("Ely")
Littleport = Station ("Littleport")
Downham_Mkt = Station("Downham Market")
Watlington = Station("Watlington")
Lynn = Station ("King's Lynn")
FenLine_Stations = [Cambridge, Cambridge_N, Waterbeach, Ely, Littleport, Downham_Mkt, Watlington, Lynn]

Camb_CambN = StationLink(Cambridge, Cambridge_N, 3700,"Down")
CambN_Camb = StationLink(Cambridge_N, Cambridge, 3700,"Up")
CambN_Wtbch = StationLink(Cambridge_N, Waterbeach, 4930,"Down")
Wtbch_CambN = StationLink(Waterbeach, Cambridge_N, 4930,"Up")
Wtbch_Ely = StationLink(Waterbeach, Ely, 15070,"Down") 
Ely_Wtbch = StationLink(Ely, Waterbeach, 15070,"Up")
Ely_Ltpt = StationLink(Ely, Littleport, 9050,"Down")
Ltpt_Ely = StationLink(Littleport, Ely, 9050,"Up")
Ltpt_DnMkt = StationLink(Littleport, Downham_Mkt, 16250, "Bi-Dir")
DnMkt_Watl =  StationLink(Downham_Mkt, Watlington, 7690,"Down")
Watl_DnMkt = StationLink(Watlington, Downham_Mkt, 7690, "Up")
Watl_Lynn = StationLink(Watlington, Lynn, 9760, "Bi-Dir")
FenLine_Links = [Camb_CambN, CambN_Camb, CambN_Wtbch, Wtbch_CambN, Wtbch_Ely, Ely_Wtbch, Ely_Ltpt, Ltpt_Ely, Ltpt_DnMkt, DnMkt_Watl, Watl_DnMkt, Watl_Lynn]

FenLine = Network("Fen Line", FenLine_Stations, FenLine_Links)

#Might be unnecesary. Could do this inside the Link Object rather than via a method. See Charles' Notes
Cambridge.SetLink([Camb_CambN])
Cambridge_N.SetLink([CambN_Wtbch, CambN_Camb])
Waterbeach.SetLink([Wtbch_Ely, Wtbch_CambN])
Ely.SetLink([Ely_Ltpt, Ely_Wtbch])
Littleport.SetLink([Ltpt_DnMkt, Ltpt_Ely])
Downham_Mkt.SetLink([DnMkt_Watl, Ltpt_DnMkt])
Watlington.SetLink([Watl_Lynn, Watl_DnMkt])
Lynn.SetLink([Watl_Lynn])

#print(FenLine)
#print(Cambridge)
#print(Camb_CambN)

TrainTimesDep = [
    {"Cambridge": 1, "Cambridge North":154, "Waterbeach":338, "Ely":775, "Littleport":1062, "Downham Market":1529, "Watlington":1782},
    {"King's Lynn":1, "Watlington":305, "Downham Market":558, "Littleport":1025, "Ely":1312, "Waterbeach":1749,"Cambridge North":1933},
    {"Cambridge": 2028, "Cambridge North":2122, "Waterbeach":2247, "Ely":2625, "Littleport":2853, "Downham Market":3261, "Watlington":3455},
    {"King's Lynn":2028, "Watlington":2273, "Downham Market":2467, "Littleport":2875, "Ely":3103, "Waterbeach":3481,"Cambridge North":3606}
]
TrainTimesArr = [    
    {"Cambridge North":94, "Waterbeach":278, "Ely":715, "Littleport":1002, "Downham Market":1469, "Watlington":1722,"King's Lynn":2026},
    {"Watlington":245, "Downham Market":498, "Littleport":965, "Ely":1252, "Waterbeach":1689,"Cambridge North":1873, "Cambridge":2026},
    {"Cambridge North":2121, "Waterbeach":2246, "Ely":2624, "Littleport":2852, "Downham Market":3260, "Watlington":3454,"King's Lynn":3699},
    {"Watlington":2272, "Downham Market":2466, "Littleport":2874, "Ely":3102, "Waterbeach":3480,"Cambridge North":3605, "Cambridge":3699},
]

FenTimes = Timetable(TrainTimesDep, TrainTimesArr)

train1Pos = Position(Cambridge, None, 0)
train2Pos = Position(Lynn, None, 0)
train3Pos = Position(Cambridge, None, 0)
train4Pos = Position(Lynn, None, 0)

train1 = Train(train1Pos, 0, 40, "down", 0)
train2 = Train(train2Pos, 0, 40, "up", 6)
train3 = Train(train3Pos, 0, 40, "down", 0)
train4 = Train(train4Pos, 0, 40, "up", 6)

Pos = {"train1":train1Pos, "train2":train2Pos, "train3":train3Pos, "train4":train4Pos}
Vel = {"train1":train1.velocity, "train2":train2.velocity, "train3":train3.velocity, "train4":train4.velocity}
Trains = {"train1":train1, "train2":train2, "train3":train3, "train4": train4}

FenState = State(0,Pos,Vel)

FenSim = Simulation(FenLine, FenTimes, FenState, Trains)

FenSim.simStart()

print("Sim Ended")
#print(FenSim.histState)

FenSnapshot = SimulationSnapshot(FenSim.GetHistState)
print(FenSnapshot.stateDict) 

FenState.ProtoPrinting()

print(train1Pos.distance)
print(train1Pos.link)
print(train1Pos.station)

print(train2Pos.distance)
print(train2Pos.link)
print(train2Pos.station)

print(train3Pos.distance)
print(train3Pos.link)
print(train3Pos.station)

print(train4Pos.distance)
print(train4Pos.link)
print(train4Pos.station)

#DONE
#   Edited Position as stated in notebook 
#   finish nextLink method
#   finish step method (details on how in notebook)
#   fix timetable to work with updated position object
#   fix bug when trains are stopped and error is thrown bc link is none (either if statement or try except statement) 
#       ^Fixed but testing required when timetable done. EDIT: looks like it works
#   work out what to do when a train reaches the end of its journey - fixed? requires testing when timetable is done. EDIT: looks to be working
#   Making stopping timetable (see book) 
#   EDIT: almost done, needs troubleshooting to fix issue with trains getting stuck at second to last station. 
#   EDIT 2: timetable issue. use breakpoints and debbuger to investigate FIXED
#   Issues with train 2 needs to be investigated. - Bug found in next link method - see book 
#   
#IN PROGRESS
#   create simulation snapshot class and instantiate it - also fix toString in state for pretty printing
#   GUI - needs to be done

#TO_DO
#   Basic Link signalling - wont be done, NO TIME 


# OPT:  modify the link setting as a part of the constructor like charles showed. might be easier to do that the method way
#       Clean up and make tostring methods work

#NOTES:
#   USe overleaf to write diss so charles can access it
