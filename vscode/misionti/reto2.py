distancia, velocidadMax, tiempo= input().split()
distancia= float(distancia)
velocidadMax= float(velocidadMax)
tiempo= float(tiempo) 
velocidad= (distancia/1000) / (tiempo/3600)
if (distancia<0 or velocidadMax <0 or tiempo <0):
     print("ERROR") 
elif (velocidad<= velocidadMax):
     print("OK")
elif (velocidad > velocidadMax and velocidad < velocidadMax*1.2):
     print ("MULTA")
else: print ("CURSO SENSIBILIZACION") 