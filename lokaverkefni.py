#Eyjolfur J Og Stéfán
#24/04/2017
#Lokaverkefni
from random import *

Þyngd=""
Mjolk=""
EinkunnirUllar=""
FjoldiAfkvaema=""
Einkunnlaeris=""
Frjosemi=""
GerdBakvodva=""
EinkunnFyrirMalir=""



teljari_random = 0
random = sample(range(53),52)
teljari3=""
teljari4=""
listi1 = [] #Leikmaður
listi2 = [] #Tölvan
leikmadur_spil = []
tolva_spil = []
Hrutaspil = {1: Þyngd, 2: Mjolk, 3: EinkunnirUllar, 4: FjoldiAfkvaema, 5: Einkunnlaeris, 6: Frjosemi, 7: GerdBakvodva, 8: EinkunnFyrirMalir}




hrutar = {}
with open("Hrutar.txt", "r", encoding="ISO-8859-1") as f:
    hrutur = f.read().split("\n")
hrutur1 = []
for x in hrutur:
    hrutur1 = eval(x)
    print(hrutur1)

#hrutar = eval(hrutur[0])
for key,value in hrutar.items():
    print(key)
    print("Þyngd",value[0] ,"Mjolk",value[1],"EinkunnirUllar",value[2],"FjoldiAfkvaema",value[3],"Einkunnlaeris",value[4],"Frjosemi",value[5],"GerdBakvodva",value[6],"EinkunnFyrirMalir",value[7])


for x in random:
    if teljari_random < 26:
        leikmadur_spil.append(x)
    else:
        tolva_spil.append(x)
    teljari_random = teljari_random + 1
print("Spil tölvunnar:",tolva_spil)
print("Spil Leikmansins:",leikmadur_spil)