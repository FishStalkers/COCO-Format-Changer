import math
import json

#to do: write to file
#       test on PP-YOLOE-R

def findCoordinates(x, y, w, h, a):
    #find x1, y1, x2, y2, x3, y3, x4, y4
    rotation = math.radians(a)
    cx = x + w / 2
    cy = y + h / 2
    x1 = cx + (w / 2) * math.cos(rotation) - (h / 2) * math.sin(rotation)
    y1 = cy + (w / 2) * math.sin(rotation) + (h / 2) * math.cos(rotation)
    x2 = cx - (w / 2) * math.cos(rotation) - (h / 2) * math.sin(rotation)
    y2 = cy - (w / 2) * math.sin(rotation) + (h / 2) * math.cos(rotation)
    x3 = cx - (w / 2) * math.cos(rotation) + (h / 2) * math.sin(rotation)
    y3 = cy - (w / 2) * math.sin(rotation) - (h / 2) * math.cos(rotation)
    x4 = cx + (w / 2) * math.cos(rotation) + (h / 2) * math.sin(rotation)
    y4 = cy + (w / 2) * math.sin(rotation) - (h / 2) * math.cos(rotation)
    return x1,y1,x2,y2,x3,y3,x4,y4


f = open('annotations.json')
x = json.load(f)

for i in x['annotations']:
    x1,y1,x2,y2,x3,y3,x4,y4 = findCoordinates(i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3], i['attributes']['rotation'])
    i['segmentation'] = [x1,y1,x2,y2,x3,y3,x4,y4]
    print(i['segmentation'])
    #with open('annotations.json', 'w') as jsonFile:
    #    json.dump(i, jsonFile)


f.close()