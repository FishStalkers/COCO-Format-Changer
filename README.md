# COCO-to-PP-YOLOE-R
computes segmentation using bbox and rotation in COCO annotations

installing PP-YOLOE-R:
https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.5/docs/tutorials/INSTALL.md

generate a image that shows the angle calculation works for this script. 

Writes to an exsting json, updating its 'segmentation' (four corner cordinates) based on the 'bbox' (x, y, w, h) and 'rotation' (angle). This new json can then be used by PP-YOLOE-R.

Sample json, after script:


![alt text](https://github.com/FishStalkers/COCO-to-PP-YOLOE-R/blob/main/Images/samplefile.PNG)

Describe the structure of the coco-json file. 
