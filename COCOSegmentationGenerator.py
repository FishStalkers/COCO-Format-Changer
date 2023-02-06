import math
import json

#to do: fix findCoordinates output negatives
#       test on PP-YOLOE-R

def findCoordinates(x, y, w, h, a):
    #find x1, y1, x2, y2, x3, y3, x4, y4
    rotation = math.radians(a)
    x1 = x + (w/2) * math.cos(rotation) - (h/2) * math.sin(rotation)
    y1 = y + (w/2) * math.sin(rotation) + (h/2) * math.cos(rotation)
    x2 = x - (w/2) * math.cos(rotation) - (h/2) * math.sin(rotation)
    y2 = y - (w/2) * math.sin(rotation) + (h/2) * math.cos(rotation)
    x3 = x - (w/2) * math.cos(rotation) + (h/2) * math.sin(rotation)
    y3 = y - (w/2) * math.sin(rotation) - (h/2) * math.cos(rotation)
    x4 = x + (w/2) * math.cos(rotation) + (h/2) * math.sin(rotation)
    y4 = y + (w/2) * math.sin(rotation) - (h/2) * math.cos(rotation)
    return x1,y1,x2,y2,x3,y3,x4,y4

f = open('annotations.json')
x = json.load(f)

for i in x['annotations']:
    x1,y1,x2,y2,x3,y3,x4,y4 = findCoordinates(i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3], i['attributes']['rotation'])
    print(x1,y1,x2,y2,x3,y3,x4,y4)
    i['segmentation'] = [x1,y1,x2,y2,x3,y3,x4,y4]

nf = open("demofile.json", "a")
nf.write(x)

f.close()