import json

propz = open("propz.txt", "a")

bear_sample = {
    "name": False,
    "background": 0,
    "hat": 1,
    "brow/eye": 2,
    "eyes accessory":3,
    "mouth": 4,
    "clothing": 5,
    "clothing accessory": 6
}

bear_attributes = ['name', 'background', 'clothes', 'mouth',
'brows/eyes', 'eyes-accessory', 'hat']

propz = open("propz.txt","a")

def props_maker(paths, color, name):
    difference = len(paths) - len(bear_attributes)
    this_bear = {}
    this_bear['name'] = name
    this_bear['background'] = color
    skip_some = [False]
    for i in range(2,len(bear_attributes)):
        p = i + (difference if skip_some[0] else 0)
        if not "TRANSPARENT" in paths[p]:
            if bear_attributes[i] == 'clothes':
                this_bear['clothes-1'] = path_formatter(paths[p], bear_attributes[i])
                for b in range(1,difference+1):
                    if not "TRANSPARENT" in paths[p+b]:
                        this_bear[f'clothes-{b+1}'] = path_formatter(paths[p+b], bear_attributes[i])
                skip_some[0] = True
            else:
                this_bear[bear_attributes[i]] = path_formatter(paths[p], bear_attributes[i])  
    return this_bear

def path_formatter(now_path, now_attribute):
    counter = [0]
    if now_attribute != 'clothes': 
        while now_path[counter[0]] != '-':
            counter[0]+=1
        counter[0]+=1
    return now_path[counter[0]:]

def text_maker(path_list, color, name):
    propz.write(json.dumps(props_maker(path_list, color, name), indent=4))
    propz.write(',\n')