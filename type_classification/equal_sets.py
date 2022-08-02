
jzr = 0
urobkowy = 0
kontener = 0
other = 0

export_list = []

with open('Desktop/work/jsw/export_enriched_new.jsonl') as f:
    u_count = 0
    for line in f:
        #jk
        if line.find("JZR_215_01") != -1 and line.find("KOb_kontenerObudowa") != -1 \
            and line.find("urobkowy") == -1 and line.find("other") == -1:
            export_list.append(line)
        #j
        if line.find("JZR_215_01") != -1 and line.find("KOb_kontenerObudowa") == -1 \
            and line.find("urobkowy") == -1 and line.find("other") == -1:
            export_list.append(line)
        #k
        if line.find("JZR_215_01") == -1 and line.find("KOb_kontenerObudowa") != -1 \
            and line.find("urobkowy") == -1 and line.find("other") == -1:
            export_list.append(line)
        #uk
        if line.find("JZR_215_01") == -1 and line.find("KOb_kontenerObudowa") != -1 \
            and line.find("urobkowy") != -1 and line.find("other") == -1:
            export_list.append(line)
        #jo
        if line.find("JZR_215_01") != -1 and line.find("KOb_kontenerObudowa") == -1 \
            and line.find("urobkowy") == -1 and line.find("other") != -1:
            export_list.append(line)
        #o 
        if line.find("JZR_215_01") == -1 and line.find("KOb_kontenerObudowa") == -1 \
            and line.find("urobkowy") == -1 and line.find("other") != -1:
            export_list.append(line)
        #u not full
        if line.find("JZR_215_01") == -1 and line.find("KOb_kontenerObudowa") == -1 \
            and line.find("urobkowy") != -1 and line.find("other") == -1 and u_count<25:
            u_count+=1
            export_list.append(line)

with open('Desktop/work/jsw/export_equal_sets.jsonl','w') as f:
    for element in export_list:
        f.write(element)
