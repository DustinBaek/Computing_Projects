"""This module contains a collection of functions related to
flood

"""

from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation as MoSt


# Task 2B
def stations_level_over_threshold(stations, tol):
    """return a list of stations which its relavtive water level is higher than 
    'tol' in descending order of relative water level in a format of a tuple 
    (station name, station relative water level)
    """
    z=[]
    for station in stations:
        if MoSt.relative_water_level(station) == None:
            continue
        if MoSt.relative_water_level(station) > tol:
            z.append((station.name,MoSt.relative_water_level(station)))
    return sorted_by_key (z,1,True)

# Task 2C
def stations_highest_rel_level(stations, N):
    """return a list of N stations with highest relative water level in 
    descending order of relative water level
    """
    z=stations_level_over_threshold(stations,0)
    return z[:N]