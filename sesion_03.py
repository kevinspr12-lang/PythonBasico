
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
for k in mi_lista:
    print("el numero es:", i)

resultado = 0
for k in mi_lista:
    resultado += k

print(f"el resultado de la suma de mi lista en: {resultado}")

for k in range(2,8):
    print(k)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

k=0

while k<7:
    k+=1
    if k == 3:
        continue
    print(k)
    if k == 5:
        break

else:
    print("k es ahora mayor o igual a 5")
