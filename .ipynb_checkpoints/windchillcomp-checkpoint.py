# Import packages
from myutils.readdata import read_data
from myutils.printing import print_comparison
from myutils.computation import compute_windchill

# Columns names and columns indices
columns = {'date':0, 'time':1, 'temperature':2, 'windspeed':7, 'windchill':12}

# Data types for each column (only if non-string)
types = {'temperature': float, 'windspeed':float, 'windchill':float}

# Read data from file
data = read_data(columns, types=types)

# Compute wind chill factor
windchill = []
for temperature, windspeed in zip(data['temperature'], data['windspeed']):
    windchill.append(compute_windchill(temperature, windspeed))

# Compute wind chill factor (using comprehension). The 3 lines above could be written.
windchill = [compute_windchill(t, w) for t, w in zip(data['temperature'], data['windspeed'])]


# Print comparison
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)

