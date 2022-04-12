# coco2yolo_flir_dataset
Convert the FLIR thermal dataset from coco format to yolo-v4 format

## Dataset information
* Numbers of data:
  A total of 26,442 fully annotated frames with 520,000 bounding box annotations across 15 different object categories.

* Label Categories :
  Person, Bike, Car, Motorcycle, Bus, Train, Truck, Traffic light, Fire Hydrant, Street Sign, Dog, Skateboard, Stroller, Scooter, Other Vehicle

* Other info or spec: https://www.flir.com/oem/adas/adas-dataset-form/

## Usage:
After you download the dataset, you need to defined the parameter of following
* path: Directory of json files containing annotations
* output_path: Output directory for image.txt files
* num_class: Numbers of class of all file, default is 3.

e.g.
```
python cocoJson2yoloTxt.py ./FLIR_ADAS_v2/images_thermal_vel/ ./data/test/ 3
```
And the results of yolo format .txt file will save to  "./data/test/".
