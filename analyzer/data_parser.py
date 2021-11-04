
# %%
import os
import json

from igc_parser import igc_lib

# %%
data_folder = os.path.realpath('../data/')
flight_file = 'flights.txt'

print(os.path.join(data_folder, flight_file))

with open(os.path.join(data_folder, flight_file), 'r') as f:
    line = f.readline()
    flight_data = json.loads(line)
    # print(flight_data['node'])
    igc_file = flight_data["igc_path"]




# %%
