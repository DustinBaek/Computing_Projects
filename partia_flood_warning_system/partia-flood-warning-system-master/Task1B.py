import floodsystem.geo as geo
import floodsystem.stationdata as stationdata
import numpy as np

def run():
    "Requirement for Task1B"
    #define coordinate
    city_centre = (52.2053, 0.1218)

    station_list = stationdata.build_station_list()
    
    #sort by distance
    sorted_list = geo.stations_by_distance(station_list, city_centre)

    #show names
    sorted_name_list = geo.station_names_and_town(sorted_list)

    near_10 = sorted_name_list[:10]
    far_10 = sorted_name_list[-10:]
    print("The nearest 10 stations from Cambridge city centre are:")
    print(near_10)
    print("The furthest 10 stations from Cambridge city centre are:")
    print(far_10)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
