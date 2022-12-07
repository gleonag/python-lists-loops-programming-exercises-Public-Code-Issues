
tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]


#Your code go here:

newTaks = dict(filter(lambda e: e['done'] == True) in e, tasks.items())
print(newTaks)

# newDict = { key:value for (key,value) in dictOfNames.items() if key % 2 == 0}

# print('Filtered Dictionary : ')
# print(newDict)
# Producción:

# Filtered Dictionary : 
# {8: 'john', 10: 'riti', 12: 'sachin'}

	# print(i["done"])


# newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.items()))

# Cómo obtener valores de un diccionario (muy similar a las listas):
# person = { "name": "Juan", "lastname": "Contreras" }
# print(person["name"]) # Salida: "Juan"
# Cómo añadirle un nuevo valor a un diccionario:
# person["age"] = 22
# print(person) # Salida: { "name": "Juan", "lastname": "Contreras", "age": 22 }
# Para hacerle un bucle en una lista, puedes hacer lo siguiente:
# spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

# for key in spanish_translations:
#     print(key) # <- salida: "dog",  "house", "cat"
#     print(spanish_translations[key]) # <- salida: "perro",  "casa", "gato"