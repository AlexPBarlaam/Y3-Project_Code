class Timetable:

    def __init__(self,d ,a):
        """Timetable Constructor (Stores the Timetable for the Simulation)

        Args:
            d (array of dicts); ordered list of departures times
            a (array of dicts); ordered lists of arrival times
        """
        self.departures = d
        self.arrivals = a
    
    def __str__(self) -> str:
        """Timetable ToString Method

        Returns:
            str: text representation of Timetable attributes
        """
        pass
#ordered list of times with ordered list of stations
#would work as program for train driver