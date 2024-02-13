cim=input("cim   x.x.x.")
maszk=input("maszk:   /")

def atvalttizes(szam):
    vissza=0
    mennyit= [128,64,32,16,8,4,2,1]
    for i in range(0,8):
        if szam[i]=="1":
            vissza+=mennyit[i]
    return vissza

bincim= format(int(cim),"08b")
binmaszk= f"{((int(maszk)-24)*'1')+((8-(int(maszk)-24))*'0')}"
hcim=""

for i in range(0,8):
    if binmaszk[i]=="1":
        if (bincim[i] == binmaszk[i]):
            hcim+="1"
        else:
            hcim+="0"

hcim = f"{hcim + (8-len(hcim))*'0'}"
szorocim = atvalttizes(hcim)+(256-atvalttizes(binmaszk))-1
halozati = atvalttizes(hcim)
decmaszk = atvalttizes(binmaszk)


print("kettes szrendszer cim: ",bincim)
print("kettes szrendszer maszk: ", binmaszk)
print("kettes szrendszer halozatcim: ", hcim)


print("decimal maszk", decmaszk)
print("decimal hcim", halozati)
print(f"decimal szoro cim: {szorocim}")


print(f"tartomany {halozati+1} --> {szorocim-1}")
print(f"elfer rajta {szorocim-halozati-1}")