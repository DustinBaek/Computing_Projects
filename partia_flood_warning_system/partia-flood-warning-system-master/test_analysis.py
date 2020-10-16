import floodsystem.analysis as analysis
from datetime import datetime
import numpy as np
import matplotlib.dates
from floodsystem.analysis import polyfit

def test_polyfit():
    dates = [datetime(2019, 2, 20), datetime(2019, 2, 21), datetime(2019, 2, 22), datetime(2019, 2, 23)]
    levels = [7, 1, -5, -5]
    polynomial = np.poly1d((1., -3., -4., 7.))
    poly, t0 = analysis.polyfit(dates, levels, 3)
    print(poly)
    print(polynomial)
    assert poly == polynomial
    assert t0 == matplotlib.dates.date2num(datetime(2019, 2, 20))

test_polyfit()