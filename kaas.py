kleur= input("Is de kaas geel? \n")
gaten= input("zitten er gaten in? \n")
schimmels= input("heeft de kaas blauwe schimmels? \n")
korst= input("heeft de kaas een korst? \n")
prijs= input("is de kaas belachelijk duur? \n")
hard= input("is de kaas hard als steen? \n")

if kleur == "ja":
    if gaten == "ja":
        if prijs == "ja":
            print("emmenthaler")
        else:
            print("leerdammer")
    elif hard == "ja":
        print("pamigiano reggianno")
    else:
        print("goudse kaas")
elif kleur == "nee":
    if schimmels == "ja":
        if korst == "ja":
            print("blue de rochbaron")
        else:
            print("foume d'ambert")
    elif schimmels == "nee":
        if korst == "ja":
            print("camembert")
        else:
            print("mozarella")



