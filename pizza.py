print("---------------------------")
print("pizza small kost      5$")
print("pizza medium kost     8$")
print("pizza large kost     13$")
print("---------------------------")
1
pizzasmall=int(input("Hoeveel pizza small wil je ")) 
pizzamedium=int(input("Hoeveel pizza medium wil je ")) 
pizzalarge=int(input("Hoeveel pizza large wil je "))
pricesmall= (pizzasmall * 5)
pricemedium= (pizzamedium * 8)
pricelarge= (pizzalarge * 13)

print("de prijs van uw pizza is dan " + str(pricesmall + pricemedium + pricelarge) + " euro")
