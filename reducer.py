#!/usr/bin/env python
import sys

max_hot_temp = 0
max_cold_temp = 0



for line in sys.stdin:
    words = line.strip().split("\t")
    
    temperature = float(words[1])
    condition = words[0]
    file_name = words[2]

    if condition == "hot" and temperature > max_hot_temp:
        max_hot_temp = temperature

    elif condition == "cold" and temperature < max_cold_temp:
        max_cold_temp = temperature

print '%s\t%s\t%s' % ('hotest',max_hot_temp,file_name)
print '%s\t%s\t%s' % ('coldest',max_cold_temp,file_name)