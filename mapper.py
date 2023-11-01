#!/usr/bin/env python
import sys
import os

file_name = os.environ["mapreduce_map_input_file"]
user = file_name.split(".")[0].split("con")[1]

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    file = words[3].strip("\"")
    extension = file[-3:]

    if extension == ".ps":
        print '%s\t%s' % (user, file)