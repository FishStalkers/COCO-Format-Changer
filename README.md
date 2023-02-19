# COCO-to-PP-YOLOE-R
computes segmentation using bbox and rotation in COCO annotations

installing PP-YOLOE-R:
https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.5/docs/tutorials/INSTALL.md


Writes to an exsting json, updating its 'segmentation' (four corner cordinates) based on the 'bbox' (x, y, w, h) and 'rotation' (angle). This new json can then be used by PP-YOLOE-R.

Sample json, after script:


![alt text](https://github.com/FishStalkers/COCO-to-PP-YOLOE-R/blob/main/Images/samplefile.PNG)

Sample image:

![alt text](https://github.com/FishStalkers/COCO-to-PP-YOLOE-R/blob/main/Images/Image12.PNG)

![alt text](https://github.com/FishStalkers/COCO-to-PP-YOLOE-R/blob/main/Images/ImageEx.png)

(Oriented bounding boxes drawn by hand, based on script output)

COCO File Structure:

{<br>
  "liscenses": [{...}],<br>
  "info": {...},<br>
  "categories": [{...}],<br>
  "images": [{...}],<br>
  "annotations": [{<br>
      "id": ...,<br>
      "image_id": ...,<br>
      "category_id": ...,<br>
      "segmentation": [...],<br>
      "area": ...,<br>
      "bbox": [...],<br>
      "iscrowd": ...,<br>
      "attributes": {<br>
          "occluded": ...,<br>
          "rotation": ....,<br>
      }<br>
   }]<br>
}<br>
