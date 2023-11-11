files = ['salida_data/part-00000','salida_data/part-00001']

max,min = 0,0
max_string = ""
min_string = ""

for file in files: 
    lines = open(file)
    for line in lines: 
        words = line.split()
        if words[2] != 'found' and float(words[2]) > max:
            max = float(words[2])
            max_string = line
        if words[2] != 'found' and float(words[2]) < min: 
            min = float(words[2])
            min_string = line

print(max_string.strip())
print(min_string.strip())
            

