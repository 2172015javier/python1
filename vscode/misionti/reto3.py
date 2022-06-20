N = int(input(""))
db = []
for i in range(N):
    c = input("")
    db.append(c.split(" ")) 
print(db)

# for i in range(N):
#     for j in range(len(db[0])):
#         db[i][j]= int (db[i][j])
# resultado = []
# cont = 0
# for i in range(N):
#     if (db[i][0] >= 240) and (db[i][0] <= 300) and\
#          (db[i][1] >= 160) and (db[i][1] <= 180) and \
#          (db[i][2] >= 240) and (db[i][2] <= 275) and \
#         (db[i][3] >= 0) and (db[i][3] <= 50):
#         resultado.append(db[i][4])
#     else:
#         cont += 1
 

# if cont == N:
#     print ("NO DISPONIBLE")
# else:
#     print (resultado)

