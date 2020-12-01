import statistics

class UndergroundSystem:

    def __init__(self):

        self.customers = {}
        self.station_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            self.customers[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.customers[id]
        del self.customers[id]
        if start_station in self.station_time:
            if stationName in self.station_time[start_station]:
                self.station_time[start_station][stationName].append(t - start_time)
            else:
                self.station_time[start_station][stationName] = [t - start_time]
        else:
            self.station_time[start_station] = {}
            self.station_time[start_station][stationName] = [t - start_time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation in self.station_time:
            if endStation in self.station_time[startStation]:
                return statistics.mean(self.station_time[startStation][endStation])