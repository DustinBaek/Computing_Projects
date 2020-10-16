from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    s1 = MonitoringStation("test", "test", "a",(1.0, 0.0),(0,1),"River X","t")
    s2 = MonitoringStation("test", "test", "b",(2.0, 0.0),(0,1),"River Y","t")
    s3 = MonitoringStation("test", "test", "c",(3.0, 0.0),(0,3),"River X","t")
    
    s1.latest_level=0.5
    s2.latest_level=0.7
    s3.latest_level=0.1
    
    z=[s1,s2,s3]
    y=stations_level_over_threshold(z,0.6)
    
    assert y==[("b",0.7)]
     
def test_stations_highest_rel_level():
    s1 = MonitoringStation("test", "test", "a",(1.0, 0.0),(0,1),"River X","t")
    s2 = MonitoringStation("test", "test", "b",(2.0, 0.0),(0,1),"River Y","t")
    s3 = MonitoringStation("test", "test", "c",(3.0, 0.0),(0,3),"River X","t")
    
    s1.latest_level=0.5
    s2.latest_level=0.7
    s3.latest_level=0.1
    
    z=[s1,s2,s3]
    y=stations_highest_rel_level(z,2)
    
    assert y==[("b",0.7),("a",0.5)]