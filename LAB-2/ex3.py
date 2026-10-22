guests = ["Pesho", "Gosho", "Sasho", "Petar", "Maria", "Ivana", "Petya", "Pesho"]

unique_guests = set(guests)

name = input("Name:")
if name in unique_guests:
    print("Guest invited!")
else:
    print("Guest not invited.")

print("Number of unique guests: ", len(unique_guests))