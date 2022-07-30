#Using to check how many tags do we have in each class
JZR214_04 = []
JZR_214_01 = []
JZR_215_01 = []
KOb_kontenerObudowa = []
KZ_kontenerMaterial = []
drzewiarka = []
urobkowy = []


# path = "/home/bilibala/Desktop/work/dataset/jsw/wozy_cropped_aug.jsonl"

path = "/export_cropped_3003_org_aug.jsonl"

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