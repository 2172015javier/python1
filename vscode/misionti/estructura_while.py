# i = 1
# while i <=8:
#     print (i)
#     i += 1
#acumulador con ciclo while

# n = int(input("digite el numero que al que le desea calcular la suma de los anteriores \n"))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1
#     print (sum, end=' ')

# print (f"la suma de cero a  {n} es: {sum}")

# n= int(input("digite un numero mayor de 10 \n"))
# n
# while n<10:
    

# print (f"el numero es {n}")

# n= int(input("digite un numero  \n"))
# con = 0

# while n != 0:
#     con += n
#     n= int(input("digite un numero \n"))

# print (f"la sumatoria de los numero digitados es {con}")

# print (f"el numero es {n}")

n= int(input("digite el valor de la compra  \n"))
con = 0
while n != 0 :
    
    if n>0:
        con += n
        n = int(input("digite el precio de otro producto \n"))
        
    else:
        while n < 0:
            n = int(input("debe ingresar un valor positivo \n"))
    
if con > 1000:
    print(f"valor a pagar {con-con*0.1}")
else:
    print(f"valor a pagar {con}")

