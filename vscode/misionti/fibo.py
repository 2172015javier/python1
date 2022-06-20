# n = int(input("ingrese la serie que desea calcular"))
n = int(input("engrese la cantidad que numeros de la serie de fibonashi que desea calcular \n"))
x=1
anterior = 0
resultado = 0
print (anterior, end = " ")
print (x, end = " ")
for i in range(n-2):
    resultado = anterior + x   
    print (resultado, end= " ") 
    anterior = x
    x = resultado 
  

