from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)
    
    # Stations at whch the current relative level is over 0.8
    z= stations_highest_rel_level(stations, 10)
    
    for a in z:
        print(a[0],a[1])

    
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    
    # Run Task2C
    run()