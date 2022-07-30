#getting all JSONs with 'JZR_215_01' or 'KOb_kontenerObudowa' wagon:
JZR214_04 = []
JZR_214_01 = []
JZR_215_01 = []
KOb_kontenerObudowa = []
KZ_kontenerMaterial = []
drzewiarka = []
urobkowy = []


with open('jsw/balance/v3_enriched_1954_training.jsonl') as f:
    for line in f:
        if line.find("/21_4_") != -1:
            JZR214_04.append(line)
        if line.find("/21_4.") != -1:
            JZR214_04.append(line)
        if line.find("/31_06_") != -1:
            JZR_214_01.append(line)
        if line.find("/31_06.") != -1:
            JZR_214_01.append(line)
        if line.find("/30_03_") != -1:
            JZR_214_01.append(line)
        if line.find("/30_03.") != -1:
            JZR_214_01.append(line)
        if line.find("/28_10_") != -1:
            JZR_214_01.append(line)
        if line.find("/28_10.") != -1:
            JZR_214_01.append(line)
        if line.find("/19_10.") != -1:
            JZR_215_01.append(line)
        if line.find("/19_10_.") != -1:
            JZR_215_01.append(line)
        if line.find("/9_03_dg.") != -1:
            drzewiarka.append(line)
print("Loaded {} 'JZR214_04' photos to resample.".format(len(JZR214_04)))
print("Loaded {} 'JZR_214_01' photos to resample.".format(len(JZR_214_01)))
print("Loaded {} 'JZR_215_01' photos to resample.".format(len(JZR_215_01)))
print("Loaded {} 'KOb_kontenerObudowa' photos to resample.".format(len(KOb_kontenerObudowa)))
print("Loaded {} 'KZ_kontenerMaterial' photos to resample.".format(len(KZ_kontenerMaterial)))
print("Loaded {} 'drzewiarka' photos to resample.".format(len(drzewiarka)))
print("Loaded {} 'urobkowy' photos to resample.".format(len(urobkowy)))

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
    JZR214_04_names[i]=JZR214_04_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
for i in range(len(JZR_214_01_names)):
    JZR_214_01_names[i]=JZR_214_01_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
for i in range(len(JZR_215_01_names)):
    JZR_215_01_names[i]=JZR_215_01_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
for i in range(len(KOb_kontenerObudowa_names)):
    KOb_kontenerObudowa_names[i]=KOb_kontenerObudowa_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
for i in range(len(KZ_kontenerMaterial_names)):
    KZ_kontenerMaterial_names[i]=KZ_kontenerMaterial_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
for i in range(len(drzewiarka_names)):
    drzewiarka_names[i]=drzewiarka_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
for i in range(len(urobkowy_names)):
    urobkowy_names[i]=urobkowy_names[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","',1)[0]
print("Finish Stripping")

#generating copies with different brightness, sharpness and contrast
from PIL import Image, ImageEnhance
# 4*70= 280
for i in range(len(JZR214_04_names)):
    print(i)
    im = Image.open("jsw/photos/combine/" + JZR214_04_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save('jsw/photos/output2/'+JZR214_04_names[i].split(".",1)[0]+'_pa.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save('jsw/photos/output2/'+JZR214_04_names[i].split(".",1)[0]+'_pb.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save('jsw/photos/output2/'+JZR214_04_names[i].split(".",1)[0]+'_pc.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(0.7).save('jsw/photos/output2/' + JZR214_04_names[i].split(".",1)[0] + '_pd.png')
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.9).save('jsw/photos/output2/'+JZR214_04_names[i].split(".",1)[0]+'_pe.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.2).save('jsw/photos/output2/'+JZR214_04_names[i].split(".",1)[0]+'_pf.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.6).save('jsw/photos/output2/'+JZR214_04_names[i].split(".",1)[0]+'_pg.png')
# 3*90=270
for i in range(len(JZR_214_01_names)):
    print(i)
    im = Image.open("jsw/photos/combine/" + JZR_214_01_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.8).save('jsw/photos/output2/'+JZR_214_01_names[i].split(".",1)[0]+'_pa.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.3).save('jsw/photos/output2/'+JZR_214_01_names[i].split(".",1)[0]+'_pb.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.7).save('jsw/photos/output2/'+JZR_214_01_names[i].split(".",1)[0]+'_pc.png')
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.3).save('jsw/photos/output2/' + JZR_214_01_names[i].split(".", 1)[0] + '_pd.png')
# 3*100=300
for i in range(len(JZR_215_01_names)):
    print(i)
    im = Image.open("jsw/photos/combine/" + JZR_215_01_names[i])
    for j in range(20):
        contrast = ImageEnhance.Contrast(im)
        tmp = JZR_215_01_names[i].split(".", 1)[0]
        contrast.enhance(0.1+0.05*j).save(f"jsw/photos/output2/{tmp}_5a_{i}{j}.png")
        tmp =JZR_215_01_names[i].split(".",1)[0]
        # print(f"jsw/photos/output2/{tmp}_5_{i}{j}.png")
        tmp = JZR_215_01_names[i].split(".", 1)[0]
        sharpness = ImageEnhance.Sharpness(im)
        sharpness.enhance(1.0+0.05*j).save(f"jsw/photos/output2/{tmp}_5b_{i}{j}.png")
        tmp = JZR_215_01_names[i].split(".", 1)[0]
        brightness = ImageEnhance.Brightness(im)
        brightness.enhance(1.0+0.05*j).save(f"jsw/photos/output2/{tmp}_5c_{i}{j}.png")
# 2*177=344
for i in range(len(KOb_kontenerObudowa_names)):
    print(f"KOb_kontenerObudowa_names{i}")
    im = Image.open("jsw/photos/combine/" + KOb_kontenerObudowa_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save('jsw/photos/output2/'+KOb_kontenerObudowa_names[i].split(".",1)[0]+'_oa.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save('jsw/photos/output2/'+KOb_kontenerObudowa_names[i].split(".",1)[0]+'_ob.png')
#6*55=330
for i in range(len(KZ_kontenerMaterial_names)):
    print(i)
    im = Image.open("jsw/photos/combine/" + KZ_kontenerMaterial_names[i])
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save('jsw/photos/output2/'+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_ma.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(1.5).save('jsw/photos/output2/'+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mb.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(1.5).save('jsw/photos/output2/'+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mc.png')
    brightness = ImageEnhance.Brightness(im)
    brightness.enhance(0.7).save('jsw/photos/output2/' + KZ_kontenerMaterial_names[i].split(".", 1)[0] + '_md.png')
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(0.5).save('jsw/photos/output2/'+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_me.png')
    sharpness = ImageEnhance.Sharpness(im)
    sharpness.enhance(0.7).save('jsw/photos/output2/'+KZ_kontenerMaterial_names[i].split(".",1)[0]+'_mf.png')
#7*41=287
for i in range(len(drzewiarka_names)):
    print(i)
    im = Image.open("jsw/photos/combine/" + drzewiarka_names[i])
    for j in range(10):
        tmp = drzewiarka_names[i].split(".",1)[0]
        contrast = ImageEnhance.Contrast(im)
        # contrast.enhance(0.5).save('jsw/photos/output2/'+drzewiarka_names[i].split(".",1)[0]+'_'+i+j+'_da.png')
        contrast.enhance(0.5).save(f"jsw/photos/output2/{tmp}_{i}{j}_da.png")
        sharpness = ImageEnhance.Sharpness(im)
        sharpness.enhance(1.5).save(f"jsw/photos/output2/{tmp}_{i}{j}_db.png")
        brightness = ImageEnhance.Brightness(im)
        brightness.enhance(1.5).save(f"jsw/photos/output2/{tmp}_{i}{j}_dc.png")
        brightness = ImageEnhance.Brightness(im)
        brightness.enhance(0.7).save(f"jsw/photos/output2/{tmp}_{i}{j}_dd.png")
        contrast = ImageEnhance.Contrast(im)
        contrast.enhance(0.5).save(f"jsw/photos/output2/{tmp}_{i}{j}_de.png")
        sharpness = ImageEnhance.Sharpness(im)
        sharpness.enhance(1.5).save(f"jsw/photos/output2/{tmp}_{i}{j}_df.png")
        contrast = ImageEnhance.Contrast(im)
        contrast.enhance(0.8).save(f"jsw/photos/output2/{tmp}_{i}{j}_dg.png")
print("Finished generating copies")

#labeling new samples with label of original images
JZR214_04_new = []
JZR_214_01_new = []
JZR_215_01_new = []
KOb_kontenerObudowa_new = []
KZ_kontenerMaterial_new = []
drzewiarka_new = []

for i in range(len(JZR214_04)):
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_pa.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_pb.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_pc.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png", 1)[0] + "_pd.png" + JZR214_04[i].split(".png", 1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_pe.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_pf.png" + JZR214_04[i].split(".png",1)[1])
    JZR214_04_new.append(JZR214_04[i].split(".png",1)[0] + "_pg.png" + JZR214_04[i].split(".png",1)[1])
for i in range(len(JZR_214_01)):
    JZR_214_01_new.append(JZR_214_01[i].split(".png",1)[0] + "_pa.png" + JZR_214_01[i].split(".png",1)[1])
    JZR_214_01_new.append(JZR_214_01[i].split(".png",1)[0] + "_pb.png" + JZR_214_01[i].split(".png",1)[1])
    JZR_214_01_new.append(JZR_214_01[i].split(".png",1)[0] + "_pc.png" + JZR_214_01[i].split(".png",1)[1])
    JZR_214_01_new.append(JZR_214_01[i].split(".png", 1)[0] + "_pd.png" + JZR_214_01[i].split(".png", 1)[1])
for i in range(len(JZR_215_01)):
    tmp1 = JZR_215_01[i].split(".png", 1)[0]
    tmp2 = JZR_215_01[i].split(".png", 1)[1]
    for j in range(20):
        JZR_215_01_new.append(f"{tmp1}_5a.png{i}{j}{tmp2}")
        JZR_215_01_new.append(f"{tmp1}_5b.png{i}{j}{tmp2}")
        JZR_215_01_new.append(f"{tmp1}_5c.png{i}{j}{tmp2}")
        # JZR_215_01_new.append(JZR_215_01[i].split(".png", 1)[0] + "_5a"+i+j+".png" + JZR_215_01[i].split(".png", 1)[1])
        # JZR_215_01_new.append(JZR_215_01[i].split(".png", 1)[0] + "_5b"+i+j+".png" + JZR_215_01[i].split(".png", 1)[1])
        # JZR_215_01_new.append(JZR_215_01[i].split(".png", 1)[0] + "_5c"+i+j+".png" + JZR_215_01[i].split(".png", 1)[1])

for i in range(len(KOb_kontenerObudowa)):
    KOb_kontenerObudowa_new.append(KOb_kontenerObudowa[i].split(".png",1)[0] + "_oa.png" + KOb_kontenerObudowa[i].split(".png",1)[1])
    KOb_kontenerObudowa_new.append(KOb_kontenerObudowa[i].split(".png",1)[0] + "_ob.png" + KOb_kontenerObudowa[i].split(".png",1)[1])
for i in range(len(KZ_kontenerMaterial)):
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_ma.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mb.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mc.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_md.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_me.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
    KZ_kontenerMaterial_new.append(KZ_kontenerMaterial[i].split(".png",1)[0] + "_mf.png" + KZ_kontenerMaterial[i].split(".png",1)[1])
for i in range(len(drzewiarka)):
    tmp1 = drzewiarka[i].split(".png",1)[0]
    tmp2 = drzewiarka[i].split(".png",1)[1]
    for j in range(10):
        drzewiarka_new.append(f"{tmp1}_{i}{j}_da.png{tmp2}")
        drzewiarka_new.append(f"{tmp1}_{i}{j}_db.png{tmp2}")
        drzewiarka_new.append(f"{tmp1}_{i}{j}_dc.png{tmp2}")
        drzewiarka_new.append(f"{tmp1}_{i}{j}_dd.png{tmp2}")
        drzewiarka_new.append(f"{tmp1}_{i}{j}_de.png{tmp2}")
        drzewiarka_new.append(f"{tmp1}_{i}{j}_df.png{tmp2}")
        drzewiarka_new.append(f"{tmp1}_{i}{j}_dg.png{tmp2}")
        # drzewiarka_new.append(drzewiarka[i].split(".png",1)[0] + '_'+i+j+"_da.png" + drzewiarka[i].split(".png",1)[1])
        # drzewiarka_new.append(drzewiarka[i].split(".png",1)[0] + '_'+i+j+"_db.png" + drzewiarka[i].split(".png",1)[1])
        # drzewiarka_new.append(drzewiarka[i].split(".png",1)[0] + '_'+i+j+"_dc.png" + drzewiarka[i].split(".png",1)[1])
        # drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + '_'+i+j+"_dd.png" + drzewiarka[i].split(".png", 1)[1])
        # drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + '_'+i+j+"_de.png" + drzewiarka[i].split(".png", 1)[1])
        # drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + '_'+i+j+"_df.png" + drzewiarka[i].split(".png", 1)[1])
        # drzewiarka_new.append(drzewiarka[i].split(".png", 1)[0] + '_'+i+j+"_dg.png" + drzewiarka[i].split(".png", 1)[1])
print("Finished labeling")

with open('jsw/balance/v3_balanced_1954_training.jsonl','w') as f:
    print("Start open export_enriched")
    with open('jsw/balance/v3_enriched_1954_training.jsonl') as f2:
        f.write(f2.read())
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