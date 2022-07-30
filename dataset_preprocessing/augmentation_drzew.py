container = []
with open('jsw/balance/v3_enriched_1954_training.jsonl') as f:
    for line in f:
        container.append(line)

import copy
container_names = copy.deepcopy(container)
for i in range(len(container_names)):
    container_names[i]=container_names[i].strip('{"imageGcsUri":"gs://wozy_test/').split('","',1)[0]
    print(container_names[i])
print("Finish Stripping")

#generating copies with different brightness, sharpness and contrast
from PIL import Image, ImageEnhance
# 4*70= 280

import ast
for i in range(len(container)):
    new = ast.literal_eval(container[i])
    tmp = new['boundingBoxAnnotations']

count = 0
container_new = []
# for i in range(len(container)):
#     new = ast.literal_eval(container[i])
#     tmp = new['boundingBoxAnnotations']
#     if len(tmp) == 1:
#         if tmp[0]['displayName'] == 'drzewiarka':
#             count += 1
# contrast 0-1 brightness 0-1 sharpness 0-2
im = Image.open("jsw/photos/input/9_03.png")
contrast = ImageEnhance.Contrast(im)
contrast.enhance(1.6).save('jsw/photos/drzew_aug/' + '9_03'+'_37.png')
sharpness = ImageEnhance.Sharpness(im)
sharpness.enhance(2.4).save('jsw/photos/drzew_aug/'+ '9_03'+'_38.png')
brightness = ImageEnhance.Brightness(im)
brightness.enhance(1.7).save('jsw/photos/drzew_aug/' + '9_03'+'_39.png')
brightness = ImageEnhance.Brightness(im)
brightness.enhance(1.8).save('jsw/photos/drzew_aug/' + '9_03' + '_40.png')
container_new.append(container[i].split(".png", 1)[0] + "_37.png" + container[i].split(".png", 1)[1])
print(container_new[0])
container_new.append(container[i].split(".png", 1)[0] + "_38.png" + container[i].split(".png", 1)[1])
container_new.append(container[i].split(".png", 1)[0] + "_39.png" + container[i].split(".png", 1)[1])
container_new.append(container[i].split(".png", 1)[0] + "_40.png" + container[i].split(".png", 1)[1])
print("Finished generating copies")
print(count)


with open('jsw/tmp/tmp_new_9_03_37-40.jsonl', 'w') as f:
    for i in range(len(container_new)):
        f.write(container_new[i])
        f.write("\n")

# with open('jsw/balance/v3_enriched_1716_training_drze_aug.jsonl', 'w') as f:
#     with open('jsw/balance/v3_enriched_1716_training.jsonl') as f2:
#         f.write(f2.read())
#     for i in range(len(container_new)):
#         f.write(container_new[i])


