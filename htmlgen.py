from os import listdir
from os.path import isfile, join
mypath="img"
onlyfiles = [f for f in listdir("img") if isfile(join(mypath, f))]

with open("index.html", "w") as f:
    tpl = open("index.tpl", "r").read()
    f.write(tpl)

    for fname in onlyfiles:
        f.write("<p><img src=\"img/{}\" /></p>".format(fname))
