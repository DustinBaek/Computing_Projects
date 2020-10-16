from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
#km

def run():
    # Build list of stations
    stations = build_station_list()
 
 
    # Coordinate of Cambridge city centre
    cam_center_coord = (52.2053, 0.1218)

    # Build a list of stations within 10km of the Cambridge city centre
    result = stations_within_radius(stations, cam_center_coord, 10)

    station_name=[]
    for station in result:
        station_name.append(station.name)
    station_name.sort()
    
    print(station_name)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    
    #run Task 1C
    run()