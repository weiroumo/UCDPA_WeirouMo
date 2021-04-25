# Create a dictionary of lists with new data
aircraft_dict = {
  "MSN": ["60154", "0048", "8849"],
  "Type": ["B737-800", "A350", "B787-9"],
  "EIS date": ["2012-04-25", "2014-12-31", "2020-04-24"],
  "Age_yr": [9.0, 6.3, 1.0]
  }
print(aircraft_dict)

# create a list
aircraft_list = [
    {"MSN": "60154", "Type": "B737-800", "EIS Date": "2012-04-25", "Age_yr": 9.0},
    {"MSN": "00448", "Type": "A350", "EIS Date": "2014-12-31", "Age_yr": 6.3},
    {"MSN": "8849", "Type": "B787-9", "EIS Sate": "2020-04-24", "Age_yr": 1.0}
]

print(aircraft_list)


# numpy
aircraft_age = [12.0, 6.8, 4.5, 10.0, 7.3, 2.4, 5.5, 6.2, 15.8, 6.4]

import numpy as np
np_aircraft_age = np.array(aircraft_age)

# convert aircraft age from year into months
np_aircraft_age_mo = 12 * np_aircraft_age

print(np_aircraft_age_mo)



