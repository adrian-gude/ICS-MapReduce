'''#!/usr/bin/env python
import sys
current_word = None
current_count = 0
word = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
    # count was not a number, so silently. Ignore/discard this line continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word
# do not forget to output the last word if needed!
if current_word == word:
print '%s\t%s' % (current_word, current_count)
'''
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