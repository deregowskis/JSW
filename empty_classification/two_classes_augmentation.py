from os import listdir
from os.path import isfile, join
import random
from PIL import Image, ImageEnhance

empty = []
loaded = []
path = '/Desktop/work/jsw/empty_full/cropped/'
path_to_copies = '/Desktop/work/jsw/empty_full/full_empty_copies/'
photos = [f for f in listdir(path) if isfile(join(path, f))]

for photo in photos:
    if photo == ".DS_Store":
        continue
    if photo.count("LOADED")>0:
        loaded.append(photo)
    elif photo.count("EMPTY")>0:
        empty.append(photo)

to_augmentation = []


for elem in empty:
    a = random.uniform(0, 1)
    if a>0.7:
        to_augmentation.append(elem)
        empty.remove(elem)
for elem in loaded:
    a = random.uniform(0, 1)
    if a>0.7:
        to_augmentation.append(elem)
        loaded.remove(elem)
    
with open('/Desktop/work/jsw/empty_full/empty_full_not_augmentated.jsonl','w') as f:
     for elem in empty:
         f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem+'","classificationAnnotation": {"displayName": "EMPTY","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
     for elem in loaded:
         f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem+'","classificationAnnotation": {"displayName": "LOADED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')

empty_aug = []
loaded_aug = []

for image in to_augmentation:
    im = Image.open(path+image)
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save(path_to_copies+image.split(".")[0]+'_a.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save(path_to_copies+image.split(".")[0]+'_b.png')
    brightness_a = ImageEnhance.Brightness(im)
    brightness_a.enhance(1.3).save(path_to_copies+image.split(".")[0]+'_c.png')
    if image.count("LOADED")>0:
        loaded_aug.append(image)
    else:
        empty_aug.append(image)

with open('/Users/deregowskis/Desktop/work/jsw/empty_full/empty_full_augmentated.jsonl','w') as f:
    for elem in empty_aug:
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem+'","classificationAnnotation": {"displayName": "EMPTY","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem.split(".")[0]+'_a.png'+'","classificationAnnotation": {"displayName": "EMPTY","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem.split(".")[0]+'_b.png'+'","classificationAnnotation": {"displayName": "EMPTY","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem.split(".")[0]+'_c.png'+'","classificationAnnotation": {"displayName": "EMPTY","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n') 
    for elem in loaded_aug:
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem+'","classificationAnnotation": {"displayName": "LOADED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem.split(".")[0]+'_a.png'+'","classificationAnnotation": {"displayName": "LOADED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem.split(".")[0]+'_b.png'+'","classificationAnnotation": {"displayName": "LOADED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n')
        f.write('{"imageGcsUri": "gs://wozy_jsw_empty_full/'+elem.split(".")[0]+'_c.png'+'","classificationAnnotation": {"displayName": "LOADED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'+'\n') 
    