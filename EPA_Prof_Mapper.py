#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    cells = line.split(",")
    count = 0
    colnames = ["state_code", "county_code", "site_num", "parameter_code", "poc", "latitude", "longitude", "datum", "parameter_name", "date_local", "time_local", "date_gmt", "time_gmt", "sample_measurement", "units_of_measure", "mdl", "uncertainty", "qualifier", "method_type", "method_code", "method_name", "state_name", "county_name", "date_of_last_change"]

    if cells[count].find(colnames[count]) != -1:
        continue
    else:
        while count < len(colnames):
            print "%s\t%s" % (colnames[count], cells[count])
            count += 1


