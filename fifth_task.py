class UndergroundSystem:

    def __init__(self):
        self.inp = {}
        self.res = {}

    def check_in(self, passenger_id, station, time) -> None:
        if passenger_id in self.inp:
            raise ValueError("passenger has already checked in")
        else:
            self.inp[passenger_id] = (station, time)

    def check_out(self, passenger_id, station, time) -> None:
        if passenger_id not in self.inp:
            raise ValueError("passenger has not checked in")
        else:
            if (self.inp[passenger_id][0], station) in self.res:
                self.res[(self.inp[passenger_id][0], station)][0] += time - self.inp[passenger_id][1]
                self.res[(self.inp[passenger_id][0], station)][1] += 1
            else:
                self.res[(self.inp[passenger_id][0], station)] = [time - self.inp[passenger_id][1], 1]
            del self.inp[passenger_id]

    def get_average_time(self, start_station, end_station) -> float: 
        if (start_station, end_station) in self.res:
            return self.res[(start_station, end_station)][0] / self.res[(start_station, end_station)][1]
        raise ValueError("no completed trips for this route")

    
