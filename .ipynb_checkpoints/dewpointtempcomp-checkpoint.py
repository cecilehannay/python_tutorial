# Import packages
from myutils.readdata import read_data
from myutils.printing import print_comparison
from myutils.computation import compute_dewpoint

# Columns names and columns indices
columns = {'date':0, 'time':1, 'temperature':2, 'humidity':5, 'dewpt':6}

# Data types for each column (only if non-string)
types = {'temperature': float, 'humidity':float, 'dewpt':float}

# Read data from file
data = read_data(columns, types=types)

# Compute dewpoint(using comprehension). 
dewpointtemp = [compute_dewpoint(t, h) for t, h in zip(data['temperature'], data['humidity'])]

# Print comparison
print_comparison('DEW PT', data['date'], data['time'], data['dewpt'], dewpointtemp)

