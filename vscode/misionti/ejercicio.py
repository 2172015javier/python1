# cadena= "hola"
# print (cadena.split(),type(cadena),len(cadena))
# num= '12'
# num= int(num)
# print (num,type(num))

# multiplicacion = 10.55*13.1
# print (round(multiplicacion,3 ))

# edad= int(input('por favor digite su edad \n'))
# if edad >= 18:
#     print ("el usuario es mayor de edad")
# else:
#     print ("el usuario es menor de edad")

# num= int(input('por favor ingrese un numero \n'))
# if num%2 == 0:
#     print ("el numero es par")
# else:
#     print ("el numero es impar")  
# 
#
# name= input('como te llamas \n')
# print (name.lower(),"minusculas") 
# print (name.upper(),'mayusculas') 
# print (name.title(), 'mayusculas y minuscualas')  
#
distancia, velocidadMax, tiempo= input().split()
distancia= float(distancia)
velocidadMax= float(velocidadMax)
tiempo= float(tiempo)
velocidad= (distancia/1000)/(tiempo/3600)
if velocidad<velocidadMax:
    print ('OK')
elif velocidad>velocidadMax and velocidad<(velocidadMax*1.2):
    print ('MULTA')
elif velocidad>velocidadMax and velocidad>(velocidadMax*1.2):
    print ('CURSO SENSIBILIZACION')
elif velocidad<0:
    print ('ERROR')

distancia, velocidadMax, tiempo= input().split()
distancia= float(distancia)
velocidadMax= float(velocidadMax)
tiempo= float(tiempo) 
velocidad= (distancia/1000) / (tiempo/3600)
if (distancia<0 or velocidad <0 or tiempo <0):
     print("ERROR") 
elif (velocidad<= velocidadMax):
     print("OK")
elif (velocidad > velocidadMax and velocidad < velocidadMax*1.2):
     print ("MULTA")
else: print ("CURSO SENSIBILIZACION") 