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
  <space><space>*<space>"liscenses": [{...}],<br>
  <space><space>*<space>"info": {...},<br>
  <space><space>*<space>"categories": [{...}],<br>
  <space><space>*<space>"images": [{...}],<br>
  <space><space>*<space>"annotations": [{<br>
      <space><space><space><space>*<space>"id": ...,<br>
      <space><space><space><space>*<space>"image_id": ...,<br>
      <space><space><space><space>*<space>"category_id": ...,<br>
      <space><space><space><space>*<space>"segmentation": [...],<br>
      <space><space><space><space>*<space>"area": ...,<br>
      <space><space><space><space>*<space>"bbox": [...],<br>
      <space><space><space><space>*<space>"iscrowd": ...,<br>
      <space><space><space><space>*<space>"attributes": {<br>
          <space><space><space><space><space><space>*<space>"occluded": ...,<br>
          <space><space><space><space><space><space>*<space>"rotation": ....,<br>
       <space><space><space><space>*<space>}<br>
   <space><space>*<space>}]<br>
}<br>
