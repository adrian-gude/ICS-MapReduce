#!/usr/bin/env python
import sys

max_hot_temp = 0
max_cold_temp = 0

city_max = "not found"
city_min = "not found"


for line in sys.stdin:
    words = line.strip().split("\t")
    temperature = float(words[1])
    condition = words[0]
    city = words[2]

    if condition == "hot" and temperature > max_hot_temp:
        max_hot_temp = temperature
        city_max = city

    elif condition == "cold" and temperature < max_cold_temp:
        max_cold_temp = temperature
        city_min = city

print '%s\t%s\t%s' % ('hotest', city_max, max_hot_temp)
print '%s\t%s\t%s' % ('coldest', city_min, max_cold_temp)