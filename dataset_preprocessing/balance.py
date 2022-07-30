#getting all JSONs with 'JZR_215_01' or 'KOb_kontenerObudowa' wagon:
JZR214_04 = []
JZR_214_01 = []
JZR_215_01 = []
KOb_kontenerObudowa = []
KZ_kontenerMaterial = []
drzewiarka = []
urobkowy = []


# with open('jsw/balance/v3_enriched_1716_training.jsonl') as f:
#     for line in f:
        # if line.find("JZR214_04") != -1:
        #     JZR214_04.append(line)
        # if line.find("JZR_214_01") != -1:
        #     JZR_214_01.append(line)
        # if line.find("JZR_215_01") != -1:
        #     JZR_215_01.append(line)
        # if line.find('KZ_kontenerMaterial') != -1:
        #     KZ_kontenerMaterial.append(line)
        # if line.find('drzewiarka') != -1:
        #     drzewiarka.append(line)
        # if line.find('KOb_kontenerObudowa') != -1:
        #     KOb_kontenerObudowa.append(line)
        # elif line.find('urobkowy') != -1:
        #     urobkowy.append(line)

container = []
with open('jsw/split/v3_enriched_1954_training.jsonl') as f:
    for line in f:
        container.append(line)

KZ_kontenerMaterial = container
import ast
new = {}
len1 = 0
len2 = 0
len3 = 0
len4 = 0
for i in range(len(KZ_kontenerMaterial)):
    new = ast.literal_eval(KZ_kontenerMaterial[i])
    tmp = new['boundingBoxAnnotations']
    # print(tmp)
    if len(tmp) == 1:
        len1 += 1
    if len(tmp) == 2:
        len2 += 1
    if len(tmp) == 3:
        len3 += 1
    if len(tmp) == 4:
        len4 += 1
print(len1)
print(len2)
print(len3)
print(len4)

# count = 0
for i in range(len(KZ_kontenerMaterial)):
    new = ast.literal_eval(KZ_kontenerMaterial[i])
    tmp = new['boundingBoxAnnotations']
    count  = 0
    for i in range(len(tmp)):
        # if tmp[i]['displayName'] == 'drzewiarka' or tmp[i]['displayName'] == 'KZ_kontenerMaterial' \
        #         or tmp[i]['displayName'] == 'KOb_kontenerObudowa' or tmp[i]['displayName'] == 'JZR_214_01':

        # if tmp[i]['displayName'] == 'JZR_214_04' or tmp[i]['displayName'] == 'JZR_215_01' \
        #  or tmp[i]['displayName'] == 'urobkowy':
        # else:
        #     count -= 100
        # if len(tmp) == 3:
        #     if tmp[i]['displayName'] == 'KZ_kontenerMaterial':
        #         count += 1
        #     if tmp[i]['displayName'] == 'JZR_214_04':
        #         count += 1
        if tmp[i]['displayName'] != 'urobkowy':
            count += 1
        else:
            count = -1000
    if count >= 0:
        print(new)
        for i in range(len(tmp)):
            print(f"{tmp[i]['displayName']}")
        print(count)
        print('\n')



