# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
import floodsystem.station as station

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

test_create_monitoring_station()

#Task1F
def test_inconsistent_typical_range_stations():
    #Create stations
    s1 = MonitoringStation('s1', 'm_id', 'label', (0, 0), (1, 2), 'river', 'town')
    s2 = MonitoringStation('s2', 'm_id', 'label', (0, 0), (2, 0), 'river', 'town')
    s3 = MonitoringStation('s3', 'm_id', 'label', (0, 0), 'level', 'river', 'town')
    s = [s1, s2, s3]

    x = station.inconsistent_typical_range_stations(s)
    #print(x)
    assert x == [s2, s3]

test_inconsistent_typical_range_stations()
