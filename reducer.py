#!/usr/bin/env python
import sys


current_wine = None

fixed_acidity = 0
n_fixed_acidity = 0

volatile_acidity = 0
n_volatile_acidity = 0

citric_acid = 0
n_citric_acid = 0

residual_sugar = 0
n_residual_sugar = 0

chlorides = 0 
n_chlorides = 0 

free_sulfur_dioxide = 0
n_free_sulfur_dioxide = 0

total_sulfur_dioxide = 0
n_total_sulfur_dioxide = 0

density = 0
n_density = 0

pH = 0
n_pH = 0

sulphates = 0
n_sulphates = 0

alcohol = 0
n_alcohol = 0

quality = 0
n_quality = 0

for line in sys.stdin:
    words = line.strip().split("\t")

    wine = words[0]
    if not current_wine:
        current_wine = wine

    if wine != current_wine:
        if n_fixed_acidity:
            print '%s\t%s\t%s' % (current_wine, "fixed acidity", fixed_acidity / n_fixed_acidity)
        else:
            print '%s\t%s\t%s' % (current_wine, "fixed acidity", 0)  

        if n_volatile_acidity:
            print '%s\t%s\t%s' % (current_wine, "volatile acidity", volatile_acidity / n_volatile_acidity)
        else:
            print '%s\t%s\t%s' % (current_wine, "volatile acidity", 0)

        if n_citric_acid:
            print '%s\t%s\t%s' % (current_wine, "citric acid", citric_acid / n_citric_acid)
        else:
            print '%s\t%s\t%s' % (current_wine, "citric acid", 0)

        if n_residual_sugar:
            print '%s\t%s\t%s' % (current_wine, "residual sugar", residual_sugar / n_residual_sugar)
        else:
            print '%s\t%s\t%s' % (current_wine, "residual sugar", 0)

        if n_chlorides:
            print '%s\t%s\t%s' % (current_wine, "chlorides", chlorides / n_chlorides)
        else:
            print '%s\t%s\t%s' % (current_wine, "chlorides", 0)

        if n_free_sulfur_dioxide:
            print '%s\t%s\t%s' % (current_wine, "free sulfur dioxide", free_sulfur_dioxide / n_free_sulfur_dioxide)
        else:
            print '%s\t%s\t%s' % (current_wine, "free sulfur dioxide", free_sulfur_dioxide / n_free_sulfur_dioxide)

        if n_total_sulfur_dioxide:
            print '%s\t%s\t%s' % (current_wine, "total sulfur dioxide", total_sulfur_dioxide / n_total_sulfur_dioxide)
        else:
            print '%s\t%s\t%s' % (current_wine, "total sulfur dioxide", 0)

        if n_density:
            print '%s\t%s\t%s' % (current_wine, "density", density / n_density)
        else:
           print '%s\t%s\t%s' % (current_wine, "density", 0)

        if n_pH:
            print '%s\t%s\t%s' % (current_wine, "pH", pH / n_pH)
        else:
           print '%s\t%s\t%s' % (current_wine, "pH", 0)

        if n_sulphates: 
            print '%s\t%s\t%s' % (current_wine, "sulphates", sulphates / n_sulphates)
        else:
            print '%s\t%s\t%s' % (current_wine, "sulphates", 0)

        if n_alcohol:
            print '%s\t%s\t%s' % (current_wine, "alcohol", alcohol / n_alcohol)
        else:
            print '%s\t%s\t%s' % (current_wine, "alcohol", 0)

        if n_quality:
            print '%s\t%s\t%s' % (current_wine, "quality", quality / n_quality)
        else:
            print '%s\t%s\t%s' % (current_wine, "quality", 0)

        current_wine = wine

        fixed_acidity = 0
        n_fixed_acidity = 0

        volatile_acidity = 0
        n_volatile_acidity = 0

        citric_acid = 0
        n_citric_acid = 0

        residual_sugar = 0
        n_residual_sugar = 0

        chlorides = 0 
        n_chlorides = 0 

        free_sulfur_dioxide = 0
        n_free_sulfur_dioxide = 0

        total_sulfur_dioxide = 0
        n_total_sulfur_dioxide = 0

        density = 0
        n_density = 0

        pH = 0
        n_pH = 0

        sulphates = 0
        n_sulphates = 0

        alcohol = 0
        n_alcohol = 0

        quality = 0
        n_quality = 0

    attribute = words[1]
    attribute_value = words[2]

    if attribute == "fixed acidity":
        fixed_acidity += float(attribute_value)
        n_fixed_acidity += 1

    if attribute == "volatile acidity":
        volatile_acidity += float(attribute_value)
        n_fixed_acidity += 1

    if attribute == "citric acid":
        fixed_acidity += float(attribute_value)
        n_volatile_acidity += 1

    if attribute == "residual sugar":
        residual_sugar += float(attribute_value)
        n_residual_sugar += 1

    if attribute == "chlorides":
        chlorides += float(attribute_value)
        n_chlorides += 1

    if attribute == "free sulfur dioxide":
        free_sulfur_dioxide += float(attribute_value)
        n_free_sulfur_dioxide += 1

    if attribute == "total sulfur dioxide":
        total_sulfur_dioxide += float(attribute_value)
        n_total_sulfur_dioxide += 1

    if attribute == "density":
        density += float(attribute_value)
        n_density += 1

    if attribute == "pH":
        pH += float(attribute_value)
        n_pH += 1

    if attribute == "sulphates":
        sulphates += float(attribute_value)
        n_sulphates += 1

    if attribute == "alcohol":
        alcohol += float(attribute_value)
        n_alcohol += 1

    if attribute == "quality":
        quality += float(attribute_value)
        n_quality += 1




if current_wine:
    if n_fixed_acidity:
        print '%s\t%s\t%s' % (current_wine, "fixed acidity", fixed_acidity / n_fixed_acidity)
    else:
        print '%s\t%s\t%s' % (current_wine, "fixed acidity", 0)  

    if n_volatile_acidity:
        print '%s\t%s\t%s' % (current_wine, "volatile acidity", volatile_acidity / n_volatile_acidity)
    else:
        print '%s\t%s\t%s' % (current_wine, "volatile acidity", 0)

    if n_citric_acid:
        print '%s\t%s\t%s' % (current_wine, "citric acid", citric_acid / n_citric_acid)
    else:
        print '%s\t%s\t%s' % (current_wine, "citric acid", 0)

    if n_residual_sugar:
        print '%s\t%s\t%s' % (current_wine, "residual sugar", residual_sugar / n_residual_sugar)
    else:
        print '%s\t%s\t%s' % (current_wine, "residual sugar", 0)

    if n_chlorides:
        print '%s\t%s\t%s' % (current_wine, "chlorides", chlorides / n_chlorides)
    else:
        print '%s\t%s\t%s' % (current_wine, "chlorides", 0)

    if n_free_sulfur_dioxide:
        print '%s\t%s\t%s' % (current_wine, "free sulfur dioxide", free_sulfur_dioxide / n_free_sulfur_dioxide)
    else:
        print '%s\t%s\t%s' % (current_wine, "free sulfur dioxide", free_sulfur_dioxide / n_free_sulfur_dioxide)

    if n_total_sulfur_dioxide:
        print '%s\t%s\t%s' % (current_wine, "total sulfur dioxide", total_sulfur_dioxide / n_total_sulfur_dioxide)
    else:
        print '%s\t%s\t%s' % (current_wine, "total sulfur dioxide", 0)

    if n_density:
        print '%s\t%s\t%s' % (current_wine, "density", density / n_density)
    else:
        print '%s\t%s\t%s' % (current_wine, "density", 0)

    if n_pH:
        print '%s\t%s\t%s' % (current_wine, "pH", pH / n_pH)
    else:
        print '%s\t%s\t%s' % (current_wine, "pH", 0)

    if n_sulphates: 
        print '%s\t%s\t%s' % (current_wine, "sulphates", sulphates / n_sulphates)
    else:
        print '%s\t%s\t%s' % (current_wine, "sulphates", 0)

    if n_alcohol:
        print '%s\t%s\t%s' % (current_wine, "alcohol", alcohol / n_alcohol)
    else:
        print '%s\t%s\t%s' % (current_wine, "alcohol", 0)

    if n_quality:
        print '%s\t%s\t%s' % (current_wine, "quality", quality / n_quality)
    else:
        print '%s\t%s\t%s' % (current_wine, "quality", 0)