import random

dice_count = int(input("Anna arpakuutioiden lukumäärä: "))
total = 0

for _ in range(dice_count):
    total += random.randint(1, 6)

print(total)