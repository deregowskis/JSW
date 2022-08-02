u = 0
k = 0
j = 0
o = 0
uk = 0 #
uj = 0
uo = 0 #
kj = 0 #
ko = 0 #
jo = 0  #
ukj = 0 #
uko = 0 #
ujo = 0 #
kjo = 0 #
ukjo = 0 #

with open('/Users/deregowskis/Desktop/work/jsw/export_enriched_new.jsonl') as f:
    for line in f:
        u_present = line.find("urobkowy")
        k_present = line.find("KOb_kontenerObudowa")
        j_present = line.find("JZR_215_01")
        o_present = line.find("other")
        if o_present != -1 and j_present !=-1 and k_present != -1 and u_present != -1:
            ukjo +=1
        elif o_present != -1 and j_present !=-1 and k_present != -1:
            kjo +=1
        elif j_present !=-1 and k_present != -1 and u_present != -1:
            ukj +=1
        elif o_present != -1 and j_present !=-1 and u_present != -1:
            ujo +=1
        elif o_present != -1 and k_present != -1 and u_present != -1:
            uko +=1
        elif o_present != -1 and j_present !=-1:
            jo +=1
        elif k_present != -1 and u_present != -1:
            uk +=1
        elif j_present !=-1 and k_present != -1:
            kj +=1
        elif o_present != -1 and k_present != -1:
            ko +=1
        elif o_present != -1 and u_present != -1:
            uo +=1
        elif j_present !=-1 and u_present != -1:
            uj +=1
        elif j_present != -1:
            j +=1
        elif o_present != -1:
            o +=1
        elif k_present != -1:
            k+=1
        elif u_present != -1:
            u+=1

print("k: {}".format(k))
print("j: {}".format(j))
print("o: {}".format(o))
print("u: {}".format(u))
print("uk: {}".format(uk))
print("uj: {}".format(uj))
print("uo: {}".format(uo))
print("kj: {}".format(kj))
print("ko: {}".format(ko))
print("jo: {}".format(jo))
print("ukj: {}".format(ukj))
print("uko: {}".format(uko))
print("kjo: {}".format(kjo))
print("ujo: {}".format(ujo))
print("ukjo: {}".format(ukjo))