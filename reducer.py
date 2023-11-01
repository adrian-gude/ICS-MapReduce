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

    user = words[0]
    if current_user != user:
        number_entries = 0
        current_user = user

    number_entries = number_entries + 1
    if number_entries > most_entries_user:
        most_entries_user = user
        number_most_entries = number_entries

    file = words[1]
    if current_file != file:
        number_entries_file = 0
        current_file = file

    number_entries_file = number_entries_file + 1
    if number_entries_file > most_entries_file:
        most_entries_file = file
        number_most_entries_file = number_entries_file


if number_entries_file > most_entries_file:
    most_entries_file = file
    number_most_entries_file = number_entries_file

if most_entries_user:
    print '%s\t%s' % (most_entries_user, number_most_entries)

if most_entries_file:
    print '%s\t%s' % (most_entries_file, number_most_entries_file)