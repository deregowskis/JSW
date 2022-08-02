#getting all JSONs with 'JZR_215_01' or 'KOb_kontenerObudowa' wagon:
jzr_full = []
kon_full = []

with open('jsw/export') as f:
    for line in f:
        if line.find("JZR_215_01") != -1:
            jzr_full.append(line)
        elif line.find('KOb_kontenerObudowa') != -1:
            kon_full.append(line)
print("Loaded {} 'JZR_215_01' photos to resample.".format(len(jzr_full)))
print("Loaded {} 'KOb_kontenerObudowa' photos to resample.".format(len(kon_full)))

#stripping jsons to file names
import copy
jzr_names = copy.deepcopy(jzr_full)
kon_names = copy.deepcopy(kon_full)
for i in range(len(jzr_names)):
    jzr_names[i]=jzr_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
for i in range(len(kon_names)):
    kon_names[i]=kon_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]

#generating copies with different brightness, sharpness and contrast
from PIL import Image, ImageEnhance
for i in range(len(jzr_names)):
    im = Image.open("jsw/photos/input/" + jzr_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save('jsw/photos/output/'+jzr_names[i].split(".",1)[0]+'_a.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save('jsw/photos/output/'+jzr_names[i].split(".",1)[0]+'_b.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save('jsw/photos/output/'+jzr_names[i].split(".",1)[0]+'_c.png')
for i in range(len(kon_names)):
    im = Image.open("jsw/photos/input/" + kon_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save('jsw/photos/output/'+kon_names[i].split(".",1)[0]+'_a.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save('jsw/photos/output/'+kon_names[i].split(".",1)[0]+'_b.png')

#labeling new samples with label of original images
jzr_full_new = []
kon_full_new = []
for i in range(len(jzr_full)):
    jzr_full_new.append(jzr_full[i].split(".png",1)[0] + "_a.png" + jzr_full[i].split(".png",1)[1])
    jzr_full_new.append(jzr_full[i].split(".png",1)[0] + "_b.png" + jzr_full[i].split(".png",1)[1])
    jzr_full_new.append(jzr_full[i].split(".png",1)[0] + "_c.png" + jzr_full[i].split(".png",1)[1])
for i in range(len(kon_full)):
    kon_full_new.append(kon_full[i].split(".png",1)[0] + "_a.png" + kon_full[i].split(".png",1)[1])
    kon_full_new.append(kon_full[i].split(".png",1)[0] + "_b.png" + kon_full[i].split(".png",1)[1])

with open('jsw/export_enriched','w') as f:
    with open('jsw/export') as f2:
        f.write(f2.read())
    for i in range(len(jzr_full_new)):
        f.write(jzr_full_new[i])
    for i in range(len(kon_full_new)):
        f.write(kon_full_new[i])