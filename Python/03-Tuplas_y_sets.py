# Las tuplas se representan con ()
# Al igual que con las listas y dicts pueden haber variables combinadas
# Las tuplas son inmutables, normalmente son utilizados para dias de la semana, un calendario, etc

t = (1,2,3)

t = ('one',2)

# Los indices y slicing tambien funciona

t[0]

t[-1]

# .index() busca el valor y retorna el indice donde se encuentra

t = (1, 3, 7, 10, 7, 5, 4, 6, 8, 5)

x = t.index(10)

# x = 3 ya que el numero 10 se encuentra en el indice tres

# .count() cuantas veces se encontro el valor

x = t.count(5)

# x = 2, ya que hay dos 5 en la tupla

# Al ser inmutables no pueden cambiar y tampoco crecer
# Reasigancion de valor o agregar un elemento va a causar un error

t[0]= 'cambia'

t.append('nope')

# Las tuplas no se usan a menudo, solo se usan cuando se quiere que un elemento reciba los mismos parametros siempre


##############################################
# Sets

# Los sets son una coleccion elementos UNICOS

x = set()

x.add(1)

x.add(2)

print(x)

# {1, 2}

# Si se intenta agragar el mismo elemento no va a dar error 

x.add(2)

print(x)

# {1, 2}

# Los sets no se pueden inicializar con valores, se tienen que ir agregando con .add()

y = set(1,2)

# Los sets son usados comunmente para obtener los valores unicos de alguna lista o dict
# Los sets solo se pueden incializar con un obejto iterable

mylist = [1,1,2,2,3,4,5,6,1,1]

print(set(mylist))

# {1, 2, 3, 4, 5, 6}

# Los sets se pueden restar y traernos la diferencia entre los dos

mylist = [1,1,2,2,3,4,5,6,1,1]

x = set(mylist)

mylist2 = [3,4,4,4,3,5]

y = set(mylist2)

print(x-y)

# {1, 2, 6}

