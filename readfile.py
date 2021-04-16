
# Columns names and columns indices
columns = {'date':0, 'time':1, 'temperature':2, 'windspeed':7}


# Data types for each column (only if non-string)
types = {'temperature': float, 'windspeed':float}

# Initialize my data variable   
data = {}
for column in columns:
    data[column] = []

# read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

# Read the first 3 lines
for _ in range(3):
    datafile.readline()

# read and parse the rest of the file
for line in datafile:
    split_line = line.split()
    for column in columns:
        icol = columns[column]
        itype = types.get(column, str)
        value = itype(split_line[icol])
        data[column].append(value)

datafile.close()

# Compute the wind chill temperature
def compute_windchill(t, v):
   a = 35.74
   b = 0.6215
   c = 35.75
   d = 0.4275

   v2 = v ** 2
   wci = a + (b * t) - (c * v2) + (d * t * v2)
   return wci


# Compute wind chill factor
windchill = []
for temperature, windspeed in zip(data['temperature'], data['windspeed']):
    windchill.append(compute_windchill(temperature, windspeed))


# Debug
print(windchill)


