#!/usr/bin/env python

import sys
from datetime import datetime
import re

(current_key, current_value) = (None, None)
for line in sys.stdin:
    try:
        (key,value) = line.strip().split("\t")
    except ValueError:
        continue
#        (key,value) = (line, " ")
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    if current_key != key:
        if current_key:
            print ("%s\t%s" % (current_key, current_value))
        (current_key, current_value) = (key, value)
        maxint = -sys.maxsize - 1
        minint = sys.maxsize
        maxfloat = -sys.maxsize - 1
        minfloat = sys.maxsize
        maxyear = -sys.maxsize - 1
        minyear = sys.maxsize
        maxtime = -sys.maxsize - 1
        mintime = sys.maxsize
        maxdate = -sys.maxsize - 1
        mindate = sys.maxsize
        strlen = 0
    if value.isdigit():
        value = int(value)
        if maxint < value:
            maxint = value
        if minint > value:
            minint = value
        current_value = "int ;\t" + "range: " + str(minint) + " to " + str(maxint)
    elif isfloat(value):
        value = float(value)
        if maxfloat < value:
            maxfloat = value
        if minfloat > value:
            minfloat = value
        current_value = "float ;\t" + "range: " + str(minfloat) + " to " + str(maxfloat)
    elif re.search('\d+/\d+/\d+',value):
        date = datetime.strptime(value,'%m/%d/%y').date()
        date_year = date.year
        if maxyear < date_year:
            maxyear = date_year
            maxdate = date
        if minyear > date_year:
            minyear = date_year
            mindate = date
        current_value = "Date :" + str(mindate) + " to " + str(maxdate)
    elif re.search('\d+:\d+', value):
        date_time = datetime.strptime(value, '%H:%M').hour
        if maxtime < date_time:
            maxtime = date_time
        if mintime > date_time:
            mintime = date_time
        current_value = "Time :" + str(mintime) + " to " + str(maxtime)
    elif isinstance(value,str):
        if strlen < len(value):
            strlen = len(value)
        current_value = "string ;\t" + "length: " + str(strlen)
if current_key:
    print ("%s\t%s" % (current_key, current_value))






