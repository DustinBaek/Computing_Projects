import floodsystem.datafetcher as datafetcher
import floodsystem.stationdata as stationdata
from floodsystem.flood import stations_level_over_threshold
from floodsystem.risk_level import risk_flood
import datetime

def run():
# Build list of stations
    stations = stationdata.build_station_list()

# Update latest level data for all stations
    stationdata.update_water_levels(stations)

    at_risk = []    
   # high_risk = []
    for a in stations_level_over_threshold(stations,0.9):
        at_risk.append(a[0])
        
    risk ={}
    for station in stations:
        if station.name in at_risk:
            risk[station.name]=risk_flood(station)

    severe_risk = []
    for station in risk:
        if risk[station] == 1:
            severe_risk.append(station)

    print("Stations that are in severe risk of flood:")
    print(severe_risk)
    #print("Stations that are in high risk of flood:")
    #print(high_risk)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
