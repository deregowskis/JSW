from PIL import Image
import random, string

crop_list = []

# First we take every line of our JSONL file and extract all bounding boxes from it.
# Every bounding box is appended to a list in format [image_name,xMin,xMax,yMin,yMax].

# (replace the path below with a path to JSONL file)
with open('/Users/bilibala/Desktop/work/dataset/wozy/export.jsonl') as f:
    lines = f.readlines()
    line = lines[1]
    # for line in f:
    image_name = line.strip('{"imageGcsUri":"gs://wozy_jsw/').split('","', 1)[0]
    truck_json = \
        line.strip('{"imageGcsUri":"gs://wozy_jsw/' + image_name + '","boundingBoxAnnotations":').split("]", 1)[0] + ']'
    truck_json = truck_json.split("}" + "}")
    for i in range(len(truck_json)):
        if truck_json[i][0] == ",":
            truck_json[i] = truck_json[i][1:]
        truck_json[i] = truck_json[i].split(',')
        for element in truck_json[i]:
            if element.count("xMin") == 1:
                xMin = element.strip('"xMin": ')
            elif element.count("xMax") == 1:
                xMax = element.strip('"xMax": ')
            elif element.count("yMin") == 1:
                yMin = element.strip('"yMin": ')
            elif element.count("yMax") == 1:
                yMax = element.strip('"yMax: ')
        # Fixed bug
        if truck_json[i] != [']']:
            crop_list.append([image_name, xMin, xMax, yMin, yMax])

print(f"length of crop_list: {crop_list}")
# NExt we generate cropped pictures of trucks based on their coordinates.

for truck in crop_list:
    # (replace the path below with a path to folder with all images. You can get all images from:
    #   https://drive.google.com/file/d/1Jy0eV0Rll7kwPEIyGJ9PV73z22ZylPlK/view?usp=sharing)
    im = Image.open('/Users/bilibala/Desktop/work/dataset/wozy/input/' + truck[0])
    width, height = im.size
    left = width * float(truck[1])
    right = width * float(truck[2])
    top = height * float(truck[3])
    bottom = height * float(truck[4])
    cropped_im = im.crop((left, top, right, bottom))
    # (replace the path below with a path to folder where all cropped images will be stored)
    cropped_im.save('/Users/bilibala/Desktop/work/dataset/wozy/cropped/' + truck[0].strip('.png') + '_' + \
                    ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                            range(5)) + '.png')
