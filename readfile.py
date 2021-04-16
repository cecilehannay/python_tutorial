
# data is the whole table
# datum is going to be each line of the table

# Initialize my data variable   
data = []

# read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

# Read the first 3 lines
for _ in range(3):
    datafile.readline()

# read and parse the rest of the file
for iline in datafile:
    datum = iline.split()
    data.append(datum)

datafile.close()



