#!/usr/bin/env python
import sys


current_user = None
number_entries = 0
most_entries_user = None
number_most_entries = 0

current_file = None
number_entries_file = 0
most_entries_file = None
number_most_entries_file = 0

for line in sys.stdin:
    words = line.strip().split("\t")

    data_type = words[1]
    data = words[0]
    if data_type == "user":
        if current_user != data:
            number_entries = 0
            current_user = data

        number_entries = number_entries + 1
        if number_entries > number_most_entries:
            most_entries_user = data
            number_most_entries = number_entries

    if data_type == "file":
        if current_file != data:
            number_entries_file = 0
            current_file = data

        number_entries_file = number_entries_file + 1
        if number_entries_file > number_most_entries_file:
            most_entries_file = data
            number_most_entries_file = number_entries_file


print '%s\t%s' % (most_entries_user, number_most_entries)
print '%s\t%s' % (most_entries_file, number_most_entries_file)