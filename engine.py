from PIL import Image
import os
from os import listdir
import random
from makemeta import *

paths = []
#select one from this folder (choose your own)
select_one = ['b-clothes']
background_colors = [
    (255, 95, 118, 255), (156, 208, 52, 255), (206, 140, 85, 255), (112, 220, 230, 255),(190, 255, 211, 255), (90, 154, 100, 255),
    (255, 200, 78, 255), (207, 94, 68, 255), (206, 131, 211, 255), (196, 196, 196, 255)
]
#name for colors specified above
background_names = ["pinkish", "lime", "coffee", "sky", "warm-shower", "swamp", "sunflower", "lava", "20min", "gray"]

existing = []

def image_maker(main_path='./test'):
    while check_exist((now := search_png(main_path))):
        continue
    return now

#REGION searching logic
def search_png(main_path='./test'):
    result_paths = get_png(main_path)
    return result_paths

def get_png(current_path):
    files = sorted(get_files(current_path))
    result_paths = []
    if files[0].endswith('.png'):
        img_path = current_path + f'/{files[random.randint(0,len(files)-1)]}'
        result_paths.append(img_path)
    else: 
        for file in files:
            if file in select_one:
                cl_files = get_files(current_path + f'/{file}')
                result_paths += get_png(f'{current_path}/{file}/{cl_files[random.randint(0,len(cl_files)-1)]}')
            else:
                result_paths += get_png(current_path + f'/{file}')
    return result_paths

def check_exist(now_paths):
    now = now_paths
    for i in existing:
        if now == i:
            print('This image already exists,\nSearch redo...')
            return True
    existing.append(now)
    return False

def get_files(path_name):
    return [f for f in listdir(path_name) if f[0] != '.']

def color_returner():
    num = random.randint(0, len(background_colors) - 1)
    return [background_names[num], background_colors[num]]

def paste_img(path_list, name='test2', test=True):
    base = Image.new('RGBA', (1650, 1650), (color := color_returner())[1])
    #REGION Layer Print
    bear_attr = []
    print("-" * 30)
    print("Name:", name)
    print("color:", color[0])
    for path_img in path_list:
        counter = len(path_img)-1
        while True:
            counter -= 1
            if path_img[counter] == '/':
                break
        print(path_img[counter+1:-7])
        bear_attr.append(path_img[counter+1:-7])
    print("-" * 30)
    text_maker(bear_attr, color[0], name)
    #ENDREGION
    for i in path_list:
        img = Image.open(i).convert('RGBA')
        base.paste(img,(75, 0), mask=img)
    newbase = base.resize((825, 825), Image.ANTIALIAS)
    newbase.putalpha(255)
    if test:
        newbase.save(f'./{name}.png', format='png')
    else:
        newbase.save(f'./collection/{name}.png', format='png')
#ENDREGION

def createCollection(number):
    bear_num = 0
    while bear_num < number:
        paste_img(image_maker(), str(bear_num+1), False)
        bear_num += 1


paste_img(search_png())
# createCollection(400)