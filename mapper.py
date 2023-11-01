#!/usr/bin/env python
import sys
import os

file_name=os.environ['mapreduce_map_input_file']

for line in sys.stdin:
    

    line = line.strip()
    words = line.split()

    if len(words) >= 4 or words[11] != 'U':

        max_temperature = float(words[5])
        min_temperature = float(words[6])
        
        if max_temperature > 27.0:
            print '%s\t%s\t%s' % ("hot",max_temperature,file_name)

        elif min_temperature < -10.0:
            print '%s\t%s\t%s' % ("cold",min_temperature,file_name)