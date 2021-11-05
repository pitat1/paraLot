
# %%
from __future__ import print_function
import os, sys
import json

from igc_parser import igc_lib

# %%
xcportal = "https://xcportal.pl"
data_folder = os.path.realpath('data/')
flight_file = 'flights.txt'

# print(os.path.join(data_folder, flight_file))
pg = 0
ppg = 0
takeoff_file_pg = open('takeoff_pg.csv', 'w')
landing_file_pg = open('landing_pg.csv', 'w')

takeoff_file_ppg = open('takeoff_pg.csv', 'w')
landing_file_ppg = open('landing_pg.csv', 'w')

missing_files = open('missing.csv', 'w')
flight_errors = open('errors.csv', 'w')


with open(os.path.join(data_folder, flight_file), 'r') as f:
    for i, line in enumerate(f):
        flight_data = json.loads(line)
        igc_file = os.path.join(data_folder,flight_data["igc_path"])
        try:
            flight = igc_lib.Flight.create_from_file(igc_file)
        except FileNotFoundError:
            missing_files.write('{}, {}/n'.format(igc_file, xcportal + flight_data['node']))

        if not flight.valid:
            flight_errors.write('{}, {}'.format(xcportal + flight_data['node'], flight.notes))
            print("Provided flight id:{} is invalid node: {} \t error:{}".format(i, xcportal + flight_data['node'], flight.notes))
        else:
            takeoff_line = "{}, {}, {}, Flight duration: {} Flight date: {} URL: {}\n".format(flight.takeoff_fix.lat, flight.takeoff_fix.lon, flight.takeoff_fix.alt, flight_data['flight_duration'], flight_data['launch_time'][:10], xcportal + flight_data['node'])
            landing_line = "{}, {}, {}, Flight duration: {} Flight date: {} URL: {}\n".format(flight.landing_fix.lat, flight.landing_fix.lon, flight.landing_fix.alt, flight_data['flight_duration'], flight_data['launch_time'][:10], xcportal + flight_data['node'])
            if flight_data['isPg'] == True:
                pg+=1
                takeoff_file_pg.write(takeoff_line)
                landing_file_pg.write(landing_line)
            else:
                ppg+=1
                takeoff_file_ppg.write(takeoff_line)
                landing_file_ppg.write(landing_line)
    sum = i + 1
    takeoff_file_pg.close()
    landing_file_pg.close()
    takeoff_file_ppg.close()
    landing_file_ppg.close()

    missing_files.close()
    flight_errors.close()
    
    print("PPG = {} and PG = {}".format(ppg,pg))
    print("DONE")

# %%
