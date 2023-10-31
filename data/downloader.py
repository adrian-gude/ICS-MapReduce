import os

with open("index.html", 'r') as f:
    line = "jeje"
    while line:
        line = f.readline()
        try:
            r_line = line.split('href="')[1]
            url = r_line.split('">')[0]
            os.system("wget " + url)
        except:
            pass
