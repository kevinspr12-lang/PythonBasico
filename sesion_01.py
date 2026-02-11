#numeros
print(int(7))
print(float(7.7))
print(type(7))
print(type(7.7))
print(int(1+2))
print(int(10*2))
print(int(1 + 4 - 2))
print(float(1 + 2.0))

# operadores matematicos
# +
# -
# *
# /
# **
# % Modulo

print(int(2**2))
print(int(4**8))
print(float(10%3))
print(float(25%4))
print(float(16%2))
print(float(10 / 3))

#variables
print("=====variable======")
x = 100
y = 1
print(x+y)

ventas = 1999991
print("Nuestra ventas fueron ", ventas)

is_active = True
print(is_active)

game_over = False
print(game_over)

some_string = "Hola soy un String"
print(some_string)

print("======condicionale=======")
edad=15
if (edadf >= 18):
    print("si puedes entrar a el bar")
else: 
    print("no puedes entrar a el bar")

mi_numero = int(input{"¿cual es el numero que quieres vereficar?"})
print(f"el numero que deseas vereficar es {mi_numero}")
if mi_numero % 2 == 0:
    print(f"el numero {mi_numero} es par")
else:
    print(f"el numero {mi_numero} es inpar")

def par_inpar(numero):
    if numero % 2 == 0:
        print(f"el numero {mi_numero} es par")
    else:
        print(f"el numero {mi_numero} es inpar")
    
print("=====funcion par_inpar======")
mi_numero = int(input{"¿cual es el numero que deseas verificar?"})
print(f"el numero que desea vereficar es {mi_numero}")
print(par_inpar{mi_numero})