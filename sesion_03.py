#loops

mi_lista= [1,2,3,4,5]

for i in mi_lista:
    print("el numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i

print(f"el resultado de la suma de mi lista en: {resultado}")

for i in range(2,8):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz {i}!")

#while loop
i=0

while i<5:
    i+=1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break

else:
    print("i es ahora mayor o igual a s")

#pratica 2
#dada la lista mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]
#imprimer cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
#pista: usa los dos tipos loops while y for en el mismo programa para lograrlo
#resultado:
#martes
#miercoles
#jueves
#viernes
#martes
#miercoles
#jueves
#viernes
#martes
#miercoles
#jueves
#viernes
#martes
#miercoles
#jueves 
#viernes
mi_lista= [1,2,3,4,5]

for i in mi_lista:
    print("el numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i


for i in range(0,0):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz {i}!")

resultado = 0
for i in mi_lista:
    resultado += i


for i in range(2,0):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz {i}!")
        
for i in range(2,0):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz {i}!")
        
#while loop
i=0

while i<0:
    i+=1
    if i == 0:
        continue
    print(i)
    if i == 1:
        break
        
else:
    print("i es ahora mayor o igual a s")

