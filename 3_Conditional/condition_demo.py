"""
age = 2

if age >= 18:
    print("Allow for Vaccine")
else:
    print("Not allowed for Vaccine")

purchase = int(input("Purchase: "))

if purchase < 50:
    print("No Discount")
elif 50 <= purchase <= 100:
    print("5% Discount")
elif 100 < purchase <= 200:
    print("10% Discount")
else:
    print("20% Discount")
"""

temperate = int(input("Temperate: "))
is_raining = False

if temperate < 4 or is_raining == True:
    print("Play Football")
else:
    print("Play Cricket")
