#!/usr/bin/env python
import sys
import os



file_name = os.environ["mapreduce_map_input_file"]
wine_name = file_name.split("winequality-")[1].split(".csv")[0]

for line in sys.stdin:
    line = line.strip()
    words = line.split(";")

    if words[0].strip("\"") != "fixed acidity":
        print '%s\t%s\t%s' % (wine_name, "fixed acidity", words[0])
        print '%s\t%s\t%s' % (wine_name, "volatile acidity", words[1])
        print '%s\t%s\t%s' % (wine_name, "citric acid", words[2])
        print '%s\t%s\t%s' % (wine_name, "residual sugar", words[3])
        print '%s\t%s\t%s' % (wine_name, "chlorides", words[4])
        print '%s\t%s\t%s' % (wine_name, "free sulfur dioxide", words[5])
        print '%s\t%s\t%s' % (wine_name, "total sulfur dioxide", words[6])
        print '%s\t%s\t%s' % (wine_name, "density", words[7])
        print '%s\t%s\t%s' % (wine_name, "pH", words[8])
        print '%s\t%s\t%s' % (wine_name, "sulphates", words[9])
        print '%s\t%s\t%s' % (wine_name, "alcohol", words[10])
        print '%s\t%s\t%s' % (wine_name, "quality", words[11])