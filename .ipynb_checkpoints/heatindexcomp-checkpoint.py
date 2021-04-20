# Import packages
from myutils.readdata import read_data
from myutils.printing import print_comparison
from myutils.computation import compute_heatindex

# Columns names and columns indices
columns = {'date':0, 'time':1, 'temperature':2, 'humidity':5, 'heatindex':13}

# Data types for each column (only if non-string)
types = {'temperature': float, 'humidity':float, 'heatindex':float}

# Read data from file
data = read_data(columns, types=types)

# Compute heat index
heatindex = []
for temperature, humidity in zip(data['temperature'], data['humidity']):
    heatindex.append(compute_heatindex(temperature, humidity))

# Print comparison
print_comparison('HEATINDEX', data['date'], data['time'], data['heatindex'], heatindex)

