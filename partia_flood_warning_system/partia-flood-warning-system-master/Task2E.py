import floodsystem.plot as plot
import floodsystem.datafetcher as datafetcher
import floodsystem.stationdata as stationdata
import floodsystem.flood as flood
import datetime

def run():
    "Requirement for Task2E"
    station_list = stationdata.build_station_list()
    stationdata.update_water_levels(station_list)
    risk_stations = flood.stations_highest_rel_level(station_list, 5)
    dt = datetime.timedelta(days = 10)
    
    to_plot = []
    for a in risk_stations:
        for st in station_list:
            if a[0] == st.name:
                to_plot.append(st)

    for b in to_plot:
        dates, levels = datafetcher.fetch_measure_levels(b.measure_id, dt)
        plot.plot_water_levels(b, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
