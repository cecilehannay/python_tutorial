
# data is the whole table
# datum is going to be each line of the table

# Initialize my data variable   
data = {'date':[],
    'time':[],
    'temp':[]}

# read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

# Read the first 3 lines
for _ in range(3):
    datafile.readline()

# read and parse the rest of the file
for line in datafile:
    split_line = line.split()
    data['date'].append(split_line[0])
    data['time'].append(split_line[1])
    data['temp'].append(float(split_line[2]))

datafile.close()

# DEBUG
print(data['time'])
print(data['temp'])




