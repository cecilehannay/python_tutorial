from readdata import read_data

# Columns names and columns indices
columns = {'date':0, 'time':1, 'temperature':2, 'windspeed':7, 'windchill':12}

# Data types for each column (only if non-string)
types = {'temperature': float, 'windspeed':float, 'windchill':float}

# Read data from file
data = read_data(columns, types=types)

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



# Output comparison of data
print('                ORIGINAL  COMPUTED')
print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')

