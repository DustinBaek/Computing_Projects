import floodsystem.geo as geo
import floodsystem.stationdata as stationdata
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def run1():
    station_list = stationdata.build_station_list()
    
    river_list = geo.rivers_with_station(station_list)
    river_list = sorted(river_list)

    print('Number of rivers:{}'.format(len(river_list)))
    print(river_list[:10])


def run2():

    station_list = stationdata.build_station_list()
    
    s_by_r_list = geo.stations_by_river(station_list)
    #print(s_by_r_list)
    def choose_river(river_name):
        s = s_by_r_list[river_name]
        s = sorted(s)
        print('The following stations are on {} :'.format(river_name))
        return s

    print(choose_river('River Aire'))
    print(choose_river('River Cam'))
    print(choose_river('River Thames'))


if __name__ == "__main__":
    print("*** Task 1D part 1: CUED Part IA Flood Warning System ***")

    #Run Task1D part 1
    run1()
    print("*** Task 1D part 2: CUED Part IA Flood Warning System ***")
    #Run Task1D part 2
    run2()