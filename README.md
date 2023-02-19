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

{
  "liscenses": [{...}],
  "info": {...},
  "categories": [{...}],
  "images": [{...}],
  "annotations": [{
      "id": ...,
      "image_id": ...,
      "category_id": ...,
      "segmentation": [...],
      "area": ...,
      "bbox": [...],
      "iscrowd": ...,
      "attributes": {
          "occluded": ...,
          "rotation": ....,
      }
   }]
}
