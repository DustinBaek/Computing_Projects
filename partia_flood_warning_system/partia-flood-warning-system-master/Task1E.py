from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():

    # Build list of stations
    stations = build_station_list()
    
    # List 9 rivers with the greatest number of moniroting stations
    greatest_rivers = rivers_by_station_number(stations, 7)
    
    #print
    print(greatest_rivers)



if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")

    # Run Task1E
    run()
