from prettytable import PrettyTable
from prettytable import TableStyle

print("Welkom in de vernieuwde Uber app!")

table = PrettyTable()
table.field_names = ["Uber Type","Prijs per KM","Max aantal passagiers"]
table.add_row(["Uber Black", "€2.00", 4])
table.add_row(["Uber Van", "€3.50", 7])
table.add_row(["Uber X", "€1.50", 3])
table.set_style(TableStyle.DOUBLE_BORDER )
print(table)

keuze=input("Kies de Uber die u wilt boeken uit bovenstaande tabel: ")
dienst={"Uber Black":2.00,"Uber Van":3.50,"Uber X":1.50}
Uber_keuze=("Uber Black","Uber Van","Uber X")
while keuze not in Uber_keuze:
        keuze = input("Maak een keuze uit de tabel. ")
else:
    try :
        aantal_km = int(input("Hoeveel kilometer reist u? "))
        prijs = dienst[keuze] * aantal_km
        print(f"De totale prijs van uw reis is €", prijs, "euro.")
    except ValueError: print("Dit is geen geldige invoer. Voer het aantal kilometers in. ")

