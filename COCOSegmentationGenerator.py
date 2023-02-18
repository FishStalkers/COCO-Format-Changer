import math
import json

#to do: 
#       test on PP-YOLOE-R

def findCoordinates(x, y, w, h, a):
    #find x1, y1, x2, y2, x3, y3, x4, y4
    rotation = math.radians(a)
    #uses linear algebra to compute the rotation about the center of the bbox. 
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

def addSegmentation(fileName):
    f = open(fileName)
    x = json.load(f)
    for i in x['annotations']:
        x1,y1,x2,y2,x3,y3,x4,y4 = findCoordinates(i['bbox'][0], i['bbox'][1], i['bbox'][2], i['bbox'][3], i['attributes']['rotation'])
        i['segmentation'] = [x1,y1,x2,y2,x3,y3,x4,y4]
    with open(fileName, 'w') as newannotations:
        json.dump(x, newannotations, indent=4)
    f.close()    

# Simply put the script in the directory, change fileName and run the method below, and run $ python COCOSegmentationGenerator.py in your terminal.
#addSegmentation(fileName)