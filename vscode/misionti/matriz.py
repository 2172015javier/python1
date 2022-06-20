# z = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# # print (z)
# # print (z[0])
# # print (z[1])
# # print (z[2][2])

# # columna = []
# # for fila in z:
# #     columna.append(fila[0])

# # print (columna)
# for i in z:
#     print (min(i))
#### suma de matrices

# a = [[2,4,6],[8,9,10],[10,20,30]]
# b= [[1,1,1],[2,2,2],[3,3,3]]
# retultado = [[0,0,0],[0,0,0],[0,0,0]]

# print (len(a))
# print (len(a[0]))

# for i in range(len(a)):
#     for j in range(len(a[0])):
#         retultado[i][j] = a[i][j] + b[i][j]

# for i in retultado:
#     print(i)

## MULTIPLICACION


# a = [[2,4,6],[8,9,10],[10,20,30]]
# b= [[1,1,1],[2,2,2],[3,3,3]]
# retultado = [[0,0,0],[0,0,0],[0,0,0]]

# print (len(a))
# print (len(a[0]))

# for i in range(len(a)):
#     for j in range(len(a[0])):
#         retultado[i][j] = a[i][j] * b[i][j]

# for i in retultado:
#     print(i)
lista = []
for i in range(4):
    c = input("")
    lista.append(c.split())

print(lista)