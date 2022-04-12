from __future__ import print_function
import argparse
import glob
import os
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", help='Directory of json files containing annotations')
    parser.add_argument(
        "output_path", help='Output directory for image.txt files')
    parser.add_argument(
        "num_class", help='Numbers of class of all file, default is 3.',
                     nargs='?', const=3, type=int)
    args = parser.parse_args()
    json_files = sorted(glob.glob(os.path.join(args.path, 'coco.json')))
    file_name_list = []
    
    for json_file in json_files:
        print('Processing',json_file,)
        with open(json_file) as f:
            data = json.load(f)
            images = data['images']
            annotations = data['annotations']

            width = 640.0
            height = 512.0
            tmp = []
            file_names = dict()
            for i in range(0, len(images)):
                # print(images[i]['id'], images[i]['file_name'])
                file_names[images[i]['id']] = images[i]['file_name']
                if images[i]['id'] not in tmp:
                    tmp.append(images[i]['id'])
            
            for idx, idx_of_img in enumerate(tmp):
                converted_results = []
                for ann in annotations:
                    if ann['image_id'] == idx_of_img and \
                        ann['category_id'] <= int(args.num_class):
                        cat_id = int(ann['category_id'])
                        # if cat_id <= num_class:
                        left, top, bbox_width, bbox_height = map(float, 
                                                                 ann['bbox'])

                        # Yolo classes are starting from zero index
                        cat_id -= 1
                        x_center, y_center = (
                            left + bbox_width / 2, top + bbox_height / 2)

                        # darknet expects relative values wrt image width&height
                        x_rel, y_rel = (x_center / width, y_center / height)
                        w_rel, h_rel = (bbox_width / width, bbox_height / height)
                        converted_results.append(
                            (cat_id, x_rel, y_rel, w_rel, h_rel))
                image_name = file_names[idx_of_img]
                # print(converted_results)
                image_name = image_name[5:-4]
                file = open(args.output_path + str(image_name) + '.txt', 'w+')
                file.write('\n'.join(
                    '%d %.6f %.6f %.6f %.6f' % res for res in converted_results
                    ))
                file.close()
                file_name_list.append(
                    './data/test/'+str(image_name) + '.txt\n'
                    )
