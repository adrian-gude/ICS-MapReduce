#!/usr/bin/env python
import sys


max_hot_city = None
max_hot_temp = -float('inf')
max_cold_city = None
max_cold_temp = float('inf')

for line in sys.stdin:
    fields = line.strip().split("\t")
    station_id = fields[0]
    temperature = float(fields[1])
    condition = fields[2]

    if condition == "Hot" and temperature > max_hot_temp:
        max_hot_city = station_id
        max_hot_temp = temperature
    elif condition == "Cold" and temperature < max_cold_temp:
        max_cold_city = station_id
        max_cold_temp = temperature

if max_hot_city:
    print '%s\t%s' % ('hotest',max_hot_city)
if max_cold_city:
    print '%s\t%s' % ('coldest',max_cold_city)