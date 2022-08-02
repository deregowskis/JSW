from os import listdir
from os.path import isfile, join
import random
#from PIL import Image, ImageEnhance

path_to_original = '/Desktop/work/jsw/empty_full/undefined_augmenatated/'
path_to_copies ='/Desktop/work/jsw/empty_full/augmentated_copies/'
original_files = [f for f in listdir(path_to_original) if isfile(join(path_to_original, f))]
copy_files = [f for f in listdir(path_to_copies) if isfile(join(path_to_copies, f))]

emptys = []
loaded = []

with open('/Desktop/work/jsw/empty_full/two_classes_cropped_labels.jsonl') as f:
    for line in f:
        if line.count("LOADED")>0:
            loaded.append(line)
        else:
            emptys.append(line)

train = []
test = []
validation =[]

for item in emptys:
    a = random.uniform(0, 1)
    if a<0.8:
        train.append(item)
    elif a>=0.8 and a<0.9:
        test.append(item)
    else:
        validation.append(item)
for item in loaded:
    a = random.uniform(0, 1)
    if a<0.8:
        train.append(item)
    elif a>=0.8 and a<0.9:
        test.append(item)
    else:
        validation.append(item)

with open('/Desktop/work/jsw/empty_full/empty_full_train.jsonl','w') as f:
    for element in train:
        f.write(element)
with open('/Desktop/work/jsw/empty_full/empty_full_test.jsonl','w') as f:
    for element in test:
        f.write(element)
with open('/Desktop/work/jsw/empty_full/empty_full_validation.jsonl','w') as f:
    for element in validation:
        f.write(element)

# with open('/Desktop/work/jsw/empty_full/augmentated_labels.jsonl','w') as f:
#     for file in original_files:
#         print(file)
#         if file == ".DS_Store":
#             continue
#         f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+file+'","classificationAnnotation": {"displayName": "UNDEFINED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
#     for file in copy_files:
#         if file == ".DS_Store":
#             continue
#         f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+file+'","classificationAnnotation": {"displayName": "UNDEFINED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')

# for image in files:
#     if image == ".DS_Store":
#         continue
#     im = Image.open(path_to_original+image)
#     contrast_a = ImageEnhance.Contrast(im)
#     contrast_a.enhance(0.5).save(path_to_copies+image.split(".")[0]+'_a.png')
#     contrast_b = ImageEnhance.Contrast(im)
#     contrast_b.enhance(0.9).save(path_to_copies+image.split(".")[0]+'_b.png')
#     sharpness = ImageEnhance.Sharpness(im)
#     sharpness.enhance(1.5).save(path_to_copies+image.split(".")[0]+'_c.png')
#     brightness_a = ImageEnhance.Brightness(im)
#     brightness_a.enhance(1.3).save(path_to_copies+image.split(".")[0]+'_d.png')
#     brightness_b = ImageEnhance.Brightness(im)
#     brightness_b.enhance(0.7).save(path_to_copies+image.split(".")[0]+'_e.png')