import random

# Vytvoření pole 9 náhodných čísel v rozsahu 0-100
pole1 = random.sample(range(101), 9)

# Výpis původního pole
print("Původní pole 1:", pole1)

# Výpis první prostřední a poslední hodnoty
print("První hodnota v poli 1:", pole1[0])
print("Prostřední hodnota v poli 1:", pole1[4])  # Prostřední hodnota má index 4
print("Poslední hodnota v poli 1:", pole1[-1])   
print("7. hodnota v poli 1:", pole1[6])         

# Zaměnění hodnoty za číslo 34
pole1[5] = 34

# Výpis pole po změně
print("Pole 1 po zaměnění hodnoty na 5. indexu:", pole1)

# Délka pole
print("Délka pole 1:", len(pole1))

# MAX a MIN hodnoty
print("Minimální hodnota v poli 1:", min(pole1))
print("Maximální hodnota v poli 1:", max(pole1))

# Vytvoření druhého pole s libovolnými čísly
pole2 = random.sample(range(154, 541), 5)

# Výpis druhého pole
print("Druhé pole 2:", pole2)

# Sečtení hodnot v obou polích
soucet_pole1 = sum(pole1)
soucet_pole2 = sum(pole2)

# Výpis součtů
print("Součet hodnot v poli 1:", soucet_pole1)
print("Součet hodnot v poli 2:", soucet_pole2)

soucet= pole2[1] + pole2[4]

# Výpis součtu hodnot na indexech 1 a 4 z pole č. 2
print("Součet hodnot na indexech 1 a 4 v poli 2:", soucet)