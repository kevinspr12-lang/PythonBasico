from Enemigo import *
from Zombie import *
from Ogro import *

Zombie = Zombie(10, 1)
Ogro = Ogro(20, 3)

print(f"{Zombie.get_tipo_enemigo()} tiene {Zombie.puntos_energia} de energia y ataca con {Zombie.ataque}")
print(f"{Ogro.get_tipo_enemigo()} tiene {Ogro.puntos_energia} de energia y ataca con {Ogro.ataque}")