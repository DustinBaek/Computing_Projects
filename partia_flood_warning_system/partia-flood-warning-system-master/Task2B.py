from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)
    
    # Stations at which the current relative level is over 0.8
    z= stations_level_over_threshold(stations, 0.8)
    for a in z:
        print(a[0],a[1])
    print(".")    
    print(".")
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    
    # Run Task2B
    run()
