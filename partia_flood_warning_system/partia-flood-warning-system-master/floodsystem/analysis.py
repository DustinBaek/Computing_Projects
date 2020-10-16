import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    '''Given the water level time history (dates, levels) 
    for a station computes a least-squares fit of a 
    polynomial of degree p to water level data. 
    Return a tuple of (i) the polynomial object and 
    (ii) any shift of the time (date) axis'''

    t = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(t - t[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, t[0]
    