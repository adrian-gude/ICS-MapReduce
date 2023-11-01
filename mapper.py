#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Dividir la linea en campos
    fields = line.strip().split()
    
    if len(fields) == 24:
        station_id = fields[0]
        date = fields[1]
        temperature = float(fields[2])
        
        if date.startswith("2017") and temperature != -9999.0:
            if temperature > 27.0:
                print '%s\t%s' % (station_id,temperature)
            elif temperature < -10.0:
                print '%s\t%s' % (station_id,temperature)