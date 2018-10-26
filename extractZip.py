from pygeocoder import Geocoder
import pandas as pd
import numpy as np
import time
import math

#path of csv file with latitude and longitude

epa_latlong = pd.read_csv('epa_lat_long_zipcode.csv')


dft = pd.DataFrame(epa_latlong)

for index,row in dft.iterrows():
    try:
        x = float(dft['postal_code'][index])
        if math.isnan(x):
            try:
                print 'inside try'
                results = Geocoder.reverse_geocode(dft['latitude'][index], dft['longitude'][index])
                dft.loc[index,'postal_code'] = results.postal_code
                print indexdf['latitude'][index], dft['longitude'][index], dft['postal_code'][index]
                time.sleep(2)
            except Exception as e:
                print 'inside except: ' + str(e)
                time.sleep(5)
                counter += 1
                if counter > 100:
                    break
    except Exception as ee:
        print 'inside float except: ' + str(ee)

dft.to_csv('epa_lat_long_zipcode.csv', header='column_names', index=False)
