import random

i = 0
ganadas = 0
corrida = 1
promedio_billetera = 0
promedio_victorias = 0
promedio_ganadas = 0

for i in range (100):
  print(" ") 
  print("+++++",corrida,"+++++")
  j = 0
  billetera = 200
  contador_apuestas = 0
  corrida += 1
  
  while j < 100 and billetera > 0:
    j += 1
    contador_apuestas += 1
    apuesta = random.randint(1,6)
    
    if apuesta %2 == 0:
      billetera = billetera + 10
      ganadas += 1
    else:
      billetera = billetera - 10

  print("Apuestas realizadas: ",contador_apuestas)
  print("Monto en Billetera: ",billetera)   

  if billetera > 200:
   promedio_victorias += 1
  
  promedio_billetera = promedio_billetera + billetera 
    
promedio_billetera = promedio_billetera // 100
promedio_ganadas = ganadas // 100

print(" ")
print('El promedio donde el usiario salio ganando dinero por corrida fue: ', promedio_victorias,'%')

print('El promedio en la billetera del usuario fue: ', promedio_billetera)

print('El promedio de apuestas ganadas fue: ', promedio_ganadas,'%')

print('Total de apuestas ganadas: ', ganadas)