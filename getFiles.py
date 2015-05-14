import os

with open("textures.txt", "w") as texList:
    for dirpath, dirnames, files in os.walk('textures'):
        if dirpath == 'textures':
            for file in files:
                if file[0] != '.':
                    print('writing ' + file)
                    texList.write(file + '\n')
