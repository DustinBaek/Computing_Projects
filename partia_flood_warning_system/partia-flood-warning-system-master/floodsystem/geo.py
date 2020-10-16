# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.haversine import haversine
from floodsystem.utils import sorted_by_key # noqa

#Task1B
def stations_by_distance(stations, p):
    "return the distances of the monitoring stations from p in an ordered list"
    results = []
    for station in stations:
        distance = haversine(station.coord, p)
        results.append((station, distance))
    results = sorted_by_key(results, 1)
    return results
def station_names_and_town(stations):
        "show the name and town for each entry in the stations by distance list"
        results = []
        for a in stations:
            i = (a[0].name, a[0].town, a[1])
            results.append(i)
        return results

#Task1C
def stations_within_radius(stations, center, r):
    x =[]

    """Calculate the distance bewteen the Cambridge city centre and the coordinate of the
        stations. If it is shother than r append to the list x"""
    
    for haha in stations:
        if haversine(haha.coord, center) <= r:
            x.append(haha)

    return x


#Task 1D
def stations_by_river(stations):
    z=[]
    h=[]
    k={}
    for station in stations:
        """Produce lists of coordinate, name of station, 
        for provided list of stations, and make set of rivers"""
        z.append(station.river)
        h.append(station.name)
        s=list(set(z))
    for i in range(len(s)):
        """Produce dictionary of stations for each river in the set"""
        for j in range(len(stations)):
            if s[i] == z[j]:
                if not s[i] in k:
                    k[s[i]]=[h[j]]
                else:
                    k[s[i]].append(h[j])
    return k

def rivers_with_station(stations):
    "Create a set of rivers with monitoring stations"
    a = []
    for i in stations:
        r = i.river
        a.append(r)
    results = set(a)
    return results


#Task1E
def rivers_by_station_number(stations, N):
    
    d=stations_by_river(stations)
    
    """Produce list of (river name, number of stations) tuples"""
    river_list=[]    
    for river,station_list in d.items():
        river_list.append((river,len(station_list)))
    
    """Produce river list sorted by number
    number set of number of stations"""
    river_list_sorted=sorted_by_key(river_list,1,reverse=True)
    
    number_of_stations = river_list_sorted[N-1][1]

    for n in river_list[1]:
        if n == number_of_stations:
            river_list_sorted.append(river_list[1])

    # result = river_list_sorted [:N]
    
    # for n in river_list[1]:
    #     if n == river_list_sorted[N][1]:
    #         result.append()

    return river_list_sorted[:N]

    
