import yaml

print("Welkom in de vernieuwde Uber app!")
print("Beschikbare Ubers: ")
type_uber = ["1 Uber Black","2 Uber Van","3 Uber X"]
print(yaml.dump(type_uber))
keuze = int(input("Kies het type Uber dat je wilt bestellen : "))


