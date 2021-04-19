from readdata import read_data

# Columns names and columns indices
columns = {'date':0, 'time':1, 'temperature':2, 'humidity':5, 'heatindex':13}

# Data types for each column (only if non-string)
types = {'temperature': float, 'humidity':float, 'heatindex':float}

# Read data from file
data = read_data(columns, types=types)

# Compute the heat index
def compute_heatindex(t, rh_pct):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = -0.22475541
    e = -0.00683783
    f = -0.05481717
    g = 0.00122874
    h = 0.00085282
    i = -0.00000199

    rh = rh_pct / 100

    hi = a + (b * t) + (c * rh) + (d * t * rh)
    + (e * t**2) + (f * rh**2) + (g * t**2 * rh)
    + (h * t * rh**2) + (i * t**2 * rh**2)
    return hi


# Compute heat index
heatindex = []
for temperature, humidity in zip(data['temperature'], data['humidity']):
    heatindex.append(compute_heatindex(temperature, humidity))



# Output comparison of data
print('                ORIGINAL  COMPUTED')
print(' DATE    TIME  HEATINDEX HEATINDEX DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, hi_obs, hi_comp in zip_data:
    hi_diff = hi_obs - hi_comp
    print(f'{date} {time:>6} {hi_obs:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')

