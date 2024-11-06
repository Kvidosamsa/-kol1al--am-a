# 1. vytvoreni pole s 5 stringy
pole = ["jmeno", "prijmeni", "vek", "pohlavi", "bydliste"]  
print("puvodni pole:", pole)  
# 2. pridani jendoho prvku  
pole.append("vitr")  
print("Pole po pridani 'vitr':", pole)  
# 3. odstraneni 2. prvku 
pole.remove("prijmeni")   
print("Pole po odstraneni 'prijmeni':", pole)  
# 4. zmeneni 5. hodnoty na neco jineho 
pole[4] = "slunce"  
print("Pole po zmeneni 5. hodnoty za 'slunce':", pole)  
# 5. pridani 2 dalsich stringu
pole.extend(["barva vlasu", "oblibena barva"])  
print("Pole po pridani 'barva vlasu' a 'oblibena barva':", pole) 
