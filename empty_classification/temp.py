# images = ['29_16','39_05','27_06','28_08','28_10','5_13','22_04','14_7','28_20','17_06','45_07','28_02','28_16','28_14','5_14','41_02','44_01','1_01','28_15']
# new_json = []
# with open('/Desktop/work/jsw/empty_full/export_new.jsonl') as f:
#     for line in f:
#         for im in images:
#             if line.count("/"+im+".png")>0:
#                 new_json.append(line)
#                 continue

# with open('/Desktop/work/jsw/empty_full/export_new_images_to_crop.jsonl','w') as f:
#     for line in new_json:
#         f.write(line)
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageEnhance
path_to_original = '/Desktop/work/jsw/empty_full/undefined_augmenatated/'
path_to_copies = '/Desktop/work/jsw/empty_full/undefined_new_copies/'
files = [f for f in listdir(path_to_original) if isfile(join(path_to_original, f))]

for image in files:
    if image == ".DS_Store":
        continue
    im = Image.open(path_to_original+image)
    contrast_a = ImageEnhance.Contrast(im)
    contrast_a.enhance(1.2).save(path_to_copies+image.split(".")[0]+'_f.png')
    contrast_b = ImageEnhance.Contrast(im)
    contrast_b.enhance(1.4).save(path_to_copies+image.split(".")[0]+'_g.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(0.7).save(path_to_copies+image.split(".")[0]+'_h.png')
    brightness_a = ImageEnhance.Brightness(im)
    brightness_a.enhance(1.1).save(path_to_copies+image.split(".")[0]+'_i.png')
    brightness_b = ImageEnhance.Brightness(im)
    brightness_b.enhance(0.9).save(path_to_copies+image.split(".")[0]+'_j.png')