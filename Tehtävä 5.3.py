def onko_alkuluku(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    luku = int(input("Anna kokonaisluku: "))
    if onko_alkuluku(luku):
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")
except ValueError:
    print("Virheellinen syöte. Anna kokonaisluku.")
