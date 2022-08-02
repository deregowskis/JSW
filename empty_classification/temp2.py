from os import listdir
from os.path import isfile, join
from PIL import Image, ImageEnhance
import random
path_to_original = '/Desktop/work/jsw/empty_full/undefined_not_augmentated/'
files = [f for f in listdir(path_to_original) if isfile(join(path_to_original, f))]
test = []
val = []
for f in files:
    if f =='.DS_Store':
        continue
    a = random.uniform(0,1)
    if a>0.5:
        test.append(f)
    else:
        val.append(f)

with open('/Desktop/work/jsw/empty_full/undefined_test.jsonl','w') as f:
    for t in test:
        line = '{"imageGcsUri": "gs://wozy_jsw_empty_full/'+t+'","classificationAnnotation": {"displayName": "UNDEFINED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'
        f.write(line+'\n')

with open('/Desktop/work/jsw/empty_full/undefined_validation.jsonl','w') as f:
    for v in val:
        line = '{"imageGcsUri": "gs://wozy_jsw_empty_full/'+v+'","classificationAnnotation": {"displayName": "UNDEFINED","annotationResourceLabels": {}},"dataItemResourceLabels": {}}'
        f.write(line+'\n')