import re

all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

patron = '[p]w+'

resultado = re.findall(patron, all_names)

for nombre in resultado:
    print(nombre)




# Syntax: str.startswith(prefix, start, end)