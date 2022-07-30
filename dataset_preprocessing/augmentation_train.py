#getting all JSONs with 'JZR_215_01' or 'KOb_kontenerObudowa' wagon:
JZR214_04 = []
JZR_214_01 = []
JZR_215_01 = []
KOb_kontenerObudowa = []
KZ_kontenerMaterial = []
drzewiarka = []
urobkowy = []



path = "/home/bilibala/Desktop/work/wozy/jsw/split_v4/v4_enriched_3003_training.jsonl"
output_json_path = "/home/bilibala/Desktop/work/wozy/jsw/split_v4/v4_additional_enriched_3003_training.jsonl"
img_output_path = "/home/bilibala/Desktop/work/dataset/jsw/wozy_cropped_3003_aug_v4/"
img_input_path = "/home/bilibala/Desktop/work/dataset/jsw/wozy_cropped_3003/"

with open(path) as f:
    for line in f:
        if line.find("JZR214_04") != -1:
            JZR214_04.append(line)
        if line.find("JZR_214_01") != -1:
            JZR_214_01.append(line)
        if line.find("JZR_215_01") != -1:
            JZR_215_01.append(line)
        if line.find('KZ_kontenerMater') != -1:
            KZ_kontenerMaterial.append(line)
        if line.find('rzewiark') != -1:
            drzewiarka.append(line)
        if line.find('KOb_kontenerObudow') != -1:
            KOb_kontenerObudowa.append(line)
        if line.find('urobkow') != -1:
            urobkowy.append(line)

print("Loaded {} 'JZR214_04' photos to resample.".format(len(JZR214_04)))
print("Loaded {} 'JZR_214_01' photos to resample.".format(len(JZR_214_01)))
print("Loaded {} 'JZR_215_01' photos to resample.".format(len(JZR_215_01)))
print("Loaded {} 'KOb_kontenerObudow' photos to resample.".format(len(KOb_kontenerObudowa)))
print("Loaded {} 'KZ_kontenerMater' photos to resample.".format(len(KZ_kontenerMaterial)))
print("Loaded {} 'rzewiark' photos to resample.".format(len(drzewiarka)))
print("Loaded {} 'urobkow' photos to resample.".format(len(urobkowy)))

#stripping jsons to file names
import copy
JZR214_04_names = copy.deepcopy(JZR214_04)
JZR_214_01_names = copy.deepcopy(JZR_214_01)
JZR_215_01_names = copy.deepcopy(JZR_215_01)
KOb_kontenerObudowa_names = copy.deepcopy(KOb_kontenerObudowa)
KZ_kontenerMaterial_names = copy.deepcopy(KZ_kontenerMaterial)
drzewiarka_names = copy.deepcopy(drzewiarka)
urobkowy_names = copy.deepcopy(urobkowy)

for i in range(len(JZR214_04_names)):
    JZR214_04_names[i]=JZR214_04_names[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","',1)[0]
for i in range(len(JZR_214_01_names)):
    JZR_214_01_names[i]=JZR_214_01_names[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","',1)[0]
for i in range(len(JZR_215_01_names)):
    JZR_215_01_names[i]=JZR_215_01_names[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","',1)[0]
for i in range(len(KOb_kontenerObudowa_names)):
    KOb_kontenerObudowa_names[i]=KOb_kontenerObudowa_names[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","',1)[0]
for i in range(len(KZ_kontenerMaterial_names)):
    KZ_kontenerMaterial_names[i]=KZ_kontenerMaterial_names[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","',1)[0]
for i in range(len(drzewiarka_names)):
    drzewiarka_names[i]=drzewiarka_names[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","',1)[0]
for i in range(len(urobkowy_names)):
    urobkowy_names[i]=urobkowy_names[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","',1)[0]
print("Finish Stripping")

#generating copies with different brightness, sharpness and contrast
from PIL import Image, ImageEnhance
for i in range(len(JZR214_04_names)):
    print(i)
    im = Image.open(f"{img_input_path}" + JZR214_04_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save(f"{img_output_path}"+JZR214_04_names[i].split(".",1)[0]+'_4a.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save(f"{img_output_path}"+JZR214_04_names[i].split(".",1)[0]+'_4b.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save(f"{img_output_path}"+JZR214_04_names[i].split(".",1)[0]+'_4c.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(0.7).save(f"{img_output_path}" + JZR214_04_names[i].split(".", 1)[0] + '_4d.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.4).save(f"{img_output_path}"+JZR214_04_names[i].split(".",1)[0]+'_4e.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.3).save(f"{img_output_path}"+JZR214_04_names[i].split(".",1)[0]+'_4f.png')

for i in range(len(JZR_214_01_names)):
    print(i)
    im = Image.open(f"{img_input_path}" + JZR_214_01_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save(f"{img_output_path}"+JZR_214_01_names[i].split(".",1)[0]+'_1a.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save(f"{img_output_path}"+JZR_214_01_names[i].split(".",1)[0]+'_1b.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save(f"{img_output_path}" + JZR_214_01_names[i].split(".", 1)[0] + '_1c.png')

for i in range(len(JZR_215_01_names)):
    print(i)
    im = Image.open(f"{img_input_path}" + JZR_215_01_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save(f"{img_output_path}"+JZR_215_01_names[i].split(".",1)[0]+'_5a.png')
    # sharpness = ImageEnhance.Sharpness(im)
    # sharpness.enhance(1.5).save(f"{img_output_path}"+JZR_215_01_names[i].split(".",1)[0]+'_5b.png')


for i in range(len(KOb_kontenerObudowa_names)):
    print(f"KOb_kontenerObudowa_names{i}")
    im = Image.open(f"{img_input_path}" + KOb_kontenerObudowa_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save(f"{img_output_path}"+KOb_kontenerObudowa_names[i].split(".",1)[0]+'_oa.png')
    # sharpness = ImageEnhance.Sharpness(im)
    # sharpness.enhance(1.5).save(f"{img_output_path}"+KOb_kontenerObudowa_names[i].split(".",1)[0]+'_ob.png')
# (5+1)*25 = 150
# (7+1)*25 = 200
for i in range(len(KZ_kontenerMaterial_names)):
    print(i)
    im = Image.open(f"{img_input_path}" + KZ_kontenerMaterial_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.8).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_ma.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mb.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mc.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(0.7).save(f"{img_output_path}" + KZ_kontenerMaterial_names[i].split(".", 1)[0] + '_md.png')
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.6).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_me.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.2).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mf.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.4).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mg.png')
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.7).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mh.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.3).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mi.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.3).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mj.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.1).save(f"{img_output_path}"+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mk.png')
    brightness = ImageEnhance.Brightness(im)
# (5+1)*26 = 156
# (7+1)*26 = 208
for i in range(len(drzewiarka_names)):
    print(i)
    im = Image.open(f"{img_input_path}" + drzewiarka_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.6).save(f"{img_output_path}"+drzewiarka_names[i].split(".",1)[0]+'_da.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save(f"{img_output_path}"+drzewiarka_names[i].split(".",1)[0]+'_db.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save(f"{img_output_path}"+drzewiarka_names[i].split(".",1)[0]+'_dc.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(0.7).save(f"{img_output_path}" + drzewiarka_names[i].split(".", 1)[0] + '_dd.png')
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.4).save(f"{img_output_path}"+drzewiarka_names[i].split(".",1)[0]+'_de.png')
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.7).save(f"{img_output_path}"+drzewiarka_names[i].split(".",1)[0]+'_df.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.4).save(f"{img_output_path}"+drzewiarka_names[i].split(".",1)[0]+'_dg.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.3).save(f"{img_output_path}"+drzewiarka_names[i].split(".",1)[0]+'_dh.png')
print("Finished generating copies")

#labeling new samples with label of original images
JZR214_04_new = []
JZR_214_01_new = []
JZR_215_01_new = []
KOb_kontenerObudowa_new = []
KZ_kontenerMaterial_new = []
drzewiarka_new = []

for i in range(len(JZR214_04)):
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_4a.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_4b.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_4c.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png", 1)[0] + "_4d.png" + JZR214_04[i].split(".png", 1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png", 1)[0] + "_4e.png" + JZR214_04[i].split(".png", 1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png", 1)[0] + "_4f.png" + JZR214_04[i].split(".png", 1)[1])
for i in range(len(JZR_214_01)):
    JZR_214_01_new.append(JZR_214_01[i].split(".png",1)[0] + "_1a.png" + JZR_214_01[i].split(".png",1)[1])
    JZR_214_01_new.append(JZR_214_01[i].split(".png",1)[0] + "_1b.png" + JZR_214_01[i].split(".png",1)[1])
    JZR_214_01_new.append(JZR_214_01[i].split(".png", 1)[0] + "_1c.png" + JZR_214_01[i].split(".png", 1)[1])
for i in range(len(JZR_215_01)):
    JZR_215_01_new.append(JZR_215_01[i].split(".png",1)[0] + "_5a.png" + JZR_215_01[i].split(".png",1)[1])
    # JZR_215_01_new.append(JZR_215_01[i].split(".png", 1)[0] + "_5b.png" + JZR_215_01[i].split(".png", 1)[1])
for i in range(len(KOb_kontenerObudowa)):
    KOb_kontenerObudowa_new.append(KOb_kontenerObudowa[i].split(".png",1)[0] + "_oa.png" + KOb_kontenerObudowa[i].split(".png",1)[1])
    # KOb_kontenerObudowa_new.append(KOb_kontenerObudowa[i].split(".png",1)[0] + "_ob.png" + KOb_kontenerObudowa[i].split(".png", 1)[1])
for i in range(len(KZ_kontenerMaterial)):
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_ma.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mb.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mc.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_md.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_me.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mf.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mg.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mh.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mi.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mj.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mk.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
for i in range(len(drzewiarka)):
    drzewiarka_new.append(drzewiarka[i].split(".png",1)[0] + "_da.png" + drzewiarka[i].split(".png",1)[1])
    drzewiarka_new.append(drzewiarka[i].split(".png",1)[0] + "_db.png" + drzewiarka[i].split(".png",1)[1])
    drzewiarka_new.append(drzewiarka[i].split(".png",1)[0] + "_dc.png" + drzewiarka[i].split(".png",1)[1])
    drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + "_dd.png" + drzewiarka[i].split(".png", 1)[1])
    drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + "_de.png" + drzewiarka[i].split(".png", 1)[1])
    drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + "_df.png" + drzewiarka[i].split(".png", 1)[1])
    drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + "_dg.png" + drzewiarka[i].split(".png", 1)[1])
    drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + "_dh.png" + drzewiarka[i].split(".png", 1)[1])
print("Finished labeling")

with open(f"{output_json_path}",'w') as f:
    for i in range(len(JZR214_04_new)):
        f.write(JZR214_04_new[i])
    for i in range(len(JZR_214_01_new)):
        f.write(JZR_214_01_new[i])
    for i in range(len(JZR_215_01_new)):
        f.write(JZR_215_01_new[i])
    for i in range(len(KOb_kontenerObudowa_new)):
        f.write(KOb_kontenerObudowa_new[i])
    for i in range(len(KZ_kontenerMaterial_new)):
        f.write(KZ_kontenerMaterial_new[i])
    for i in range(len(drzewiarka_new)):
        f.write(drzewiarka_new[i])
print("Finished - export_enriched")
# with open(f"{output_json_path}",'w') as f:
#     print("Start open export_enriched")
#     with open(f"{path}") as f2:
#         f.write(f2.read())
#     for i in range(len(JZR214_04_new)):
#         f.write(JZR214_04_new[i])
#     for i in range(len(JZR_214_01_new)):
#         f.write(JZR_214_01_new[i])
#     for i in range(len(JZR_215_01_new)):
#         f.write(JZR_215_01_new[i])
#     for i in range(len(KOb_kontenerObudowa_new)):
#         f.write(KOb_kontenerObudowa_new[i])
#     for i in range(len(KZ_kontenerMaterial_new)):
#         f.write(KZ_kontenerMaterial_new[i])
#     for i in range(len(drzewiarka_new)):
#         f.write(drzewiarka_new[i])
#     print("Finished - export_enriched")