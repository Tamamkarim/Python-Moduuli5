luvut = []

while True:
    syote = input("Anna luku (tai paina Enter lopettaaksesi): ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte. Anna kelvollinen luku.")

luvut.sort(reverse=True)
viisi_suurinta = luvut[:5]

print("Viisi suurinta lukua ovat:")
for luku in viisi_suurinta:
    print(luku)
