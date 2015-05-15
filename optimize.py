from tinypng import shrink_file
import os

KEY = 'Gh3YVrSCirWGAktujziNq_ZV_tfCZxI4'
for dirpath, dirnames, files in os.walk('textures'):
    for file in files:
        if file[0] != '.':
            name = file[(file.find('-')+1):]
            shrink_info = shrink_file("./textures/"+file, api_key=KEY,out_filepath="./optimized/"+file)
            

            

