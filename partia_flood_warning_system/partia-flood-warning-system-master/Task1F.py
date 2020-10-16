import floodsystem.station as station
import floodsystem.stationdata as stationdata

def run():
    "Requirements for Task1F"
    station_list = stationdata.build_station_list()

    inconsistent_list = station.inconsistent_typical_range_stations(station_list)
    inconsistent_names = [a.name for a in inconsistent_list]
    inconsistent_names = sorted(inconsistent_names)

    print(inconsistent_names)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()