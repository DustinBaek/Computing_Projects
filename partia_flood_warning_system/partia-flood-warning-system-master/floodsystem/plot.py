import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
import numpy as np
import floodsystem.analysis as analysis

def plot_water_levels(station, dates, levels):
  '''plots the water level of a station'''
  c = np.linspace(station.typical_range[0], station.typical_range[0], len(dates))
  d = np.linspace(station.typical_range[1], station.typical_range[1], len(dates))
  plt.plot(dates, levels)
  plt.plot(dates, c)
  plt.plot(dates, d)
  # Add axis labels, rotate date labels and add plot title

  plt.xlabel('date')
  plt.ylabel('water level (m)')
  plt.xticks(rotation=45)
  plt.title(station.name)

  # Display plot
  plt.tight_layout()  # This makes sure plot does not cut off date labels

  return plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
  '''plots the water level data and the best-fit polynomial'''
  t = matplotlib.dates.date2num(dates)
  poly, t0 = analysis.polyfit(dates, levels, p)
    
  c = np.linspace(station.typical_range[0], station.typical_range[0], len(dates))
  d = np.linspace(station.typical_range[1], station.typical_range[1], len(dates))
  plt.plot(dates, c)
  plt.plot(dates, d)
  # Plot original data points
  plt.plot(dates, levels, '.')
  # Plot polynomial fit at 30 points along interval
  t1 = np.linspace(t[0], t[-1], 30)
  plt.plot(t1, poly(t1 - t0))

  plt.xlabel('date')
  plt.ylabel('water level (m)')
  plt.xticks(rotation=45)
  plt.title(station.name)
  # Display plot
  return plt.show()