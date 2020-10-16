# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
#Task1F
    def typical_range_consistent(self):
        s=self.typical_range
        # False if no range
        if s == None:
            return False
        # False if high range lower than low range
        elif s[0] > s[1]:
            return False
        else:
            return True
    
#Task 2B
    def relative_water_level(self):
        # Check Data if it is not available or inconsistent
        if MonitoringStation.typical_range_consistent(self) == False:
            return None
        elif self.latest_level == None:
            return None
        else:
            level = self.latest_level
            low = self.typical_range[0]
            high = self.typical_range[1]
            return (level-low)/(high-low)

#Task 1F
def inconsistent_typical_range_stations(stations):
    results = []
    for a in stations:
        if a.typical_range_consistent():
            pass
        else:
            results.append(a)
    return results
