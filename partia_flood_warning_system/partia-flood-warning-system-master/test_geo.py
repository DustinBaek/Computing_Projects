from floodsystem.haversine import haversine
import floodsystem.geo as geo
from floodsystem.geo import stations_within_radius, rivers_by_station_number, stations_by_river
from floodsystem.station import MonitoringStation

#Task 1B
def test_stations_by_distance():
    #Create stations
    s1 = MonitoringStation('test', 'm id', 'name1', (3.0, 4.0), (1, 2), 'river', 'town')
    s2 = MonitoringStation('test', 'm id', 'name2', (0.0, 0.0), (1, 2), 'river', 'town')
    s3 = MonitoringStation('test', 'm id', 'name3', (5.0, 12.0), (1, 2), 'river', 'town')
    s = [s1, s2, s3]
    #Centre coordinate
    p = (0, 0)
    #Calculate distances
    d1 = haversine(s1.coord, p)
    d2 = haversine(s2.coord, p)
    d3 = haversine(s3.coord, p)

    x = geo.stations_by_distance(s, p)
    y = geo.station_names_and_town(x)
    #print(y)
    assert y == [('name2', 'town', d2), ('name1', 'town', d1), ('name3', 'town', d3)]

test_stations_by_distance()

#Task 1C
def test_stations_within_radius():
    #Create station
    s = MonitoringStation("test", "test", "test",(-2.0, 4.0),(0,0),"t","t")
    x= stations_within_radius([s],(0.0,0.0),1)
    assert len(x)==0

test_stations_within_radius()

#Task 1D
def test_stations_by_river():
    # Create two stations with same river
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_ID = "test-s-id 1"
    m_ID = "test-m-id 1"
    Label = "some station 1"
    Coord = (-21.0, 4.20)
    Trange = (-3.3, 2.4445)
    river = "River X"
    Town = "Your Town"
    y = MonitoringStation(s_ID, m_ID, Label, Coord, Trange, river, Town)
    z=[s, y]
    x=stations_by_river(z)
    assert len(x["River X"])==2
    
def test_rivers_with_station():
    # Create three stations
    s1 = MonitoringStation("name1", "test", "a",(1.0, 0.0),(0,0),"River X","t")
    s2 = MonitoringStation("name2", "test", "b",(2.0, 0.0),(0,0),"River Y","t")
    s3 = MonitoringStation("name3", "test", "c",(3.0, 0.0),(0,0),"River X","t")
    s = [s1, s2, s3]
    a = geo.rivers_with_station(s)
    assert a == set(['River X', 'River Y'])

test_rivers_with_station()

#Task 1E
def test_rivers_by_station_number():
    # Create three stations
    s1 = MonitoringStation("test", "test", "a",(1.0, 0.0),(0,0),"River X","t")
    s2 = MonitoringStation("test", "test", "b",(2.0, 0.0),(0,0),"River Y","t")
    s3 = MonitoringStation("test", "test", "c",(3.0, 0.0),(0,0),"River X","t")
    z=[s1,s2,s3]
    r=rivers_by_station_number(z,1)
    assert r[0][0]=="River X"

test_rivers_by_station_number()