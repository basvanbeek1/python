
print("++++++++++++++++++++++++++++++++++++++++++++")
print("+      Sollicitatie Circusdirecteur        +")
print("++++++++++++++++++++++++++++++++++++++++++++")
print("Welkom bij de sollicitatie over of je in    ")
print("aanmerking komt om de nieuwe circusdirecteur")
print("te worden je krijgt zo een paar vragen      ")
print("onze vraag is om deze in alle eerlijkheid te beantwoorden")
print("++++++++++++++++++++++++++++++++++++++++++++")

DierenDressuur= input("Hoeveel jaar praktijkervaring met dieren-dressuur heb je? (type 0 wanneer geen) \n")
Jongleren= input("Hoeveel jaar ervaring met jongleren heb je? (type 0 wanneer geen) \n")
acrobatiek= input("Hoeveel jaar ervaring met acrobatiek heb je? (type 0 wanneer geen) \n")
DiplomaOndernemen = input("Ben je in bezit van een diploma MBO-4 ondernemen? J/N \n")
Rijbewijs= input("Ben je in bezit van een vrachtwagen rijbewijs? J/N \n")
HogeHoed= input("Ben je in bezit van een hoge hoed? J/N \n")
ManOfVrouw= input("Ben je een man of vrouw? M/V \n")
 
if ManOfVrouw.lower() == "m":
    snor = input("Hoe breed is je snoor in cm? \n ")
    haar = 0 
elif ManOfVrouw.lower() == "v":
    Haar = input("Hoelang is je krulhaar? \n")
    snor = 0 


lengte = input("Hoe lang ben je in cm? \n")
gewicht = input("Hoe zwaar ben je in kg? \n")
certificaat = input("Heb je een certificaat in overleven met gevaarlijk personeel? J/N \n")

if int(DierenDressuur) >= 4:
    var1 = True
else: 
    var1 = False

if int(Jongleren) >= 5:
    var2 = True
else: 
    var2 = False

if int(acrobatiek) >= 3:
    var3 = True
else:
    var3 = False

if DiplomaOndernemen.lower() == "j":
    var4 = True
else:
    var4 = False

if Rijbewijs.lower() == "j":
    var5 = True
else:
    var5 = False

if HogeHoed.lower() == "j":
    var6 = True
else:
    var6 = False

if int(snor) >= 10 or int(haar) >= 20:
    var7 = True
else:
    var7 = False

if int(lengte) >= 150:
    var8 = True
else:
    var8 = False

if int(gewicht) >= 90:
    var9 = True
else:
    var9 = False

if certificaat.lower() == "j":
    var10 = True
else:
    var10 = False

if var1 or var2 or var3 and var4 and var5 and var6 and var7 and var8 and var9 and var10:
        print("Gefeliciteerd, U bent aangenomen")
else:
    print("Helaas komt u niet in aanmerking voor de baan")
        

