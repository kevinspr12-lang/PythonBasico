#tuplas
mi_tuplas =(2,4)
print("mi tupla: ",mi_tuplas)

#lista
mi_lista = [1, 2.1416, "Kevin", mi_tuplas]
print("el primer elemento de mi lista:", mi_lista[0])
print("el cuarto elemento de mi lista:", mi_lista[3])
print("el primer tercer de mi lista:", mi_lista[2])

#diccionario
mi_diccionario = {"mi_lista": mi_lista,
                  "nombre": "Kevin",
                  "pi": 2.1416,
                  "tel": "664-7838419"}
print("llave para accesar a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print("llave para accesar a mi diccionario pi", mi_diccionario["pi"])
print("llave para accesar a mi diccionario tel", mi_diccionario["tel"])