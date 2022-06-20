# print (len ("hola python python"))
# lista = ["pythons","es" ]
# print (" ".join(lista))

a = ("hola mundo, esto  sera, una lista")
lista2  = a.split(",")
print (lista2)

# texto = "manuel es mi amigo"
# print (texto.replace("manuel es","javier era",))

# texto = "manuel es mi amigo"
# print (texto.upper())

# texto = "MANUEL ES MI amiGo"
# print (texto.lower())

# x = range(7)
# print (list(x))

# x = [2, 3, 4, 5, 6, 7]
# print (max(x))

# x = [4, 5, 6, 7]
# print (min(x)) 

# x = [1,0,9,10,11,12,13,14,15,16,17]
# print (sum(x)) 

# x = range(8)
# print (list(x))
# print (tuple(x))

with open("hola.txt", "w") as variables:
    variables.writelines(["Eje"])

# with open("editable.txt","w") as variables: #ingresa a un tipo de archivo y lo edita 
#     variables.writelines("Hola mundo Hola") 

# print(ord("\\"))
# print(round(19.9416))