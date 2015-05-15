import os

with open("temp.txt", "w") as texList:
    for dirpath, dirnames, files in os.walk('textures'):
        if dirpath == 'textures':
            for file in files:
                if file[0] != '.':
                    print('writing ' + file)
                    texList.write(file + '\n')
os.system('gshuf temp.txt > textures.txt')
os.system('rm temp.txt')

