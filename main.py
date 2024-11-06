import random

# Vytvoreni pole 9 nahodnych cisel v rozsahu 0-100.
pole1 = random.sample(range(101), 9)

# Vypis puvodniho pole
print("Puvodni pole 1:", pole1)

# Vypis prvni prostredni a posledni hodnoty
print("Prvni hodnota v poli 1:", pole1[0])
print("Prostredni hodnota v poli 1:", pole1[4])  # Prostredni hodnota ma index 4
print("Posledni hodnota v poli 1:", pole1[-1])   
print("7. hodnota v poli 1:", pole1[6])         

# Zameneni hodnoty za cislo 34
pole1[5] = 34

# Vypis pole po zmene
print("Pole 1 po zamene hodnoty na 5. indexu:", pole1)

# Delka pole
print("Delka pole 1:", len(pole1))

# MAX a MIN hodnoty
print("Minimalni hodnota v poli 1:", min(pole1))
print("Maximalni hodnota v poli 1:", max(pole1))

# Vytvoreni druheho pole s libovolnymi cisly
pole2 = random.sample(range(154, 541), 5)

# Vypis druheho pole
print("Druhe pole 2:", pole2)

# Secteni hodnot v obou polich
soucet_pole1 = sum(pole1)
soucet_pole2 = sum(pole2)

# Vypis souctu
print("Soucet hodnot v poli 1:", soucet_pole1)
print("Soucet hodnot v poli 2:", soucet_pole2)

soucet = pole2[1] + pole2[4]

# Vypis souctu hodnot na indexech 1 a 4 z pole c. 2
print("Soucet hodnot na indexech 1 a 4 v poli 2:", soucet)
