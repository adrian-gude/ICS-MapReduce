
from os import listdir
from os.path import isfile, join

directory = 'salida_data/'
files = [f for f in listdir(directory) if isfile(join(directory, f)) and 'part' in f]

max_files_ps,max_url_visited = 0,0

user_string = ""
url_string = ""

for file in files: 
    lines = open(directory + file)

    for line in lines: 
        words = line.split()
        if "http" in words[0] and int(words[1]) > max_url_visited:
            max_url_visited = int(words[1])
            url_string = line

        if not "http" in words[0] and int(words[1]) > max_files_ps:
            max_files_ps = int(words[1])
            user_string = line

print(user_string.strip())
print(url_string.strip())

