def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
   
    """
    Read data from CU Boulder Weather Station data file

    Parameters:
      columns: A dictionary of column names mapping to column indices
      types: A dictionary of column names mapping to types to which
         to convert each column of data
      filename: The string path pointing to the CU Boulder Weather
            Station data file
    """

    # Initialize my data variable   
    data = {}
    for column in columns:
        data[column] = []

    # read the data file
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

    return data


