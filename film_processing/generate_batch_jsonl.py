import os
version = 2
root_path = '/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1_cropped_vertex/'
image_input_folder_path = f"/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1_cropped_vertex/"
jsonl_path = f"{root_path}batch_vertex.jsonl"

#
# {"content": "gs://wozy_cropped_3003_org_aug/7_14.png", "mimeType": "image/png"}
#
if os.path.exists(f"{jsonl_path}"):
  os.remove(f"{jsonl_path}")
for images in os.listdir(image_input_folder_path):
    # check if the image ends with png
    if images.endswith(".png"):
        with open(f"{jsonl_path}", 'a+') as f:
            # string1 + newName
            string1 = '{"content": "gs://wozy_wagon_object_detection/vertex/'
            string2 = '", "mimeType": "image/png"}'
            f.write(
                f'''{string1}{images}{string2}''')
            f.write("\n")