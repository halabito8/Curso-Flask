# Como ya se comento Python mantiene sus bloques con identacion
# Los if funcionan igual

if 1 == 2:
    print('primero')
elif 3 == 3:
    print('medio')
else:
    print('ultimo')

##################################
# For
# Los loops no necesitan una condicion en un objeto iterable solo se va a iterar sobre el elemento

seq = [1,2,3,4,5]

for item in seq:
    print(item)

# 1
# 2
# 3
# 4
# 5

# La variable se puede llamar como sea, no hay palabra reservada

for hola in seq:
    print('Yep')

# Yep
# Yep
# Yep
# Yep
# Yep

# Tambien funciona con dicts

edades = {"Sam":3,"Frank":4,"Dan":29}

for i in edades:
    print(f"Esta es la llave {i}")
    print(f"El valor {edades[i]}")

# Esta es la llave Sam
# El valor 3
# Esta es la llave Frank
# El valor 4
# Esta es la llave Dan
# El valor 29

# Tambien se puede usar en objetos anidados

mypairs = [(1,10),(3,30),(5,50)]

# Normal
for tup in mypairs:
    print(tup)

# (1, 10)
# (3, 30)
# (5, 50)

# Tuple un-packing
for item1,item2 in mypairs:
    print(item1)
    print(item2)

# 1
# 10
# 3
# 30
# 5
# 50

# Para un for que se quiere iterar cierta cantidad de veces se usa range

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

# Range funciona igual que slicing

for i in range(2,5):
    print(i)

# 2
# 3
# 4

for i in range(3,10,2):
    print(i)

# 3
# 5
# 7
# 9

##################################
# While
# Los while funcionan igual

i = 1
while i < 5:
    print(f'i = {i}')
    i += 1

##################################
# Do-While
# Los do-while no existen en python pero se puede hacer una trampa

i = 1

while True:
    if i > 5:
        break
    print(f'i = {i}')
    i += 1