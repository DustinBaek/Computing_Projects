import floodsystem.plot as plot
import matplotlib.pyplot as plt
from datetime import datetime
from floodsystem.station import MonitoringStation

def test_plot_water_levels():
    dates = [datetime(2019, 2, 20), datetime(2019, 2, 21), datetime(2019, 2, 22)]
    levels = [2, 6, 5]

    station = MonitoringStation('s1', 'm_id', 'label', (0, 0), (1, 2), 'river', 'town')
    x = plot.plot_water_levels(station, dates, levels)
    assert x == plt.show()

test_plot_water_levels()

def test_plot_water_level_with_fit():
    dates = [datetime(2019, 2, 20), datetime(2019, 2, 21), datetime(2019, 2, 22), datetime(2019, 2, 23)]
    levels = [1, -5, -5, 7]
    station = MonitoringStation('s1', 'm_id', 'label', (0, 0), (1, 2), 'river', 'town')
    
    y = plot.plot_water_level_with_fit(station, dates, levels, 3)
    assert y == plt.show()

test_plot_water_level_with_fit()