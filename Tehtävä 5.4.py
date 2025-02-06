LS = []

for i in range(5):
    kaupunki = input(f"Anna {i+1}. kaupungin nimi: ")
    LS.append(kaupunki)

print("\nSyöttämäsi kaupungit ovat:")
for kaupunki in LS:
    print(kaupunki)
