import os

for dirpath, dirnames, files in os.walk('textures'):
    for file in files:
        name = file[(file.find('-')+1):]
        if not os.path.isfile('urlLists/'+name[:(-4)]+'.txt'):
            print('oh ' + name)


