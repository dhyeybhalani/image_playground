import sys
import os
from PIL import  Image
argument1 = sys.argv[1]
argument2 = sys.argv[2]
if os.path.exists(argument2):
    print('Ok file is available')
else:
    parent_dir = '.'
    dir = argument2
    path = os.path.join(parent_dir,dir)
    os.mkdir(path)
for filename in os.listdir(argument1):
    img = Image.open(f'{argument1}{filename}')
    clean_img = os.path.splitext(filename)[0]
    filtered_img = img.convert('L')
    filtered_img.save(f'{argument2}{clean_img}.png','png')
    print('all done')
