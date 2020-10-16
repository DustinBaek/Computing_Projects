from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation as MoSt

def risk_flood(station):
    """rate the risk of flooding of a station as four levels: 1(severe), 2(high),
    3(moderate),4(low)'
    When relative water level is higher than 1.2 or higher than 0.9 and in an 
    increasing state it is severe.
    When relative water level is higher than 0.8 or higher than 0.9 and in a
    decreasing state it is high.
    When relative water level is higher than 0.5 it is moderate.
    Else is low.
    """

    if MoSt.relative_water_level(station) == None:
        return 0
    
    t = 2
    _, levels = fetch_measure_levels(station.measure_id, timedelta(days=t))

    if MoSt.relative_water_level(station) > 1.2:
        return 1
    elif MoSt.relative_water_level(station) >0.9:
        if levels[-1] > levels[-2]:
            return 1
        else:
            return 2
    elif MoSt.relative_water_level(station) > 0.8:
        return 2
    elif MoSt.relative_water_level(station) > 0.5:
        return 3
    else:
        return 4