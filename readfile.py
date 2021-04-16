
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

# DEBUG
#print(data['time'])
print(data['temperature'])




