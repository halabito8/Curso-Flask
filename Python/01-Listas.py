# En python hay tres tipos manejar datos con [] se crea una lista
# Es una estructura facil de manejar a parte de que es mutable
# no esta reservado para solo un tipo de dato (se puede combinar strings y numeros)

mi_lista1 = [1,2,3]
mi_lista2 = ["Hola","estoy",'en',"una",'lista']
mi_lista3 = [12,"teclado",5632.156,'k']

mi_lista1[1] = 'dos'

# Tambien se puede hacer slicing, suma y multiplicacion

mi_lista1[1:]
mi_lista2[:4]
mi_lista3[::2]

# Con al suma hay que tener cuidado ya que al sumar se tiene que reasignar para cambiar la lista
mi_lista1 + 'Esto no se va a agregar'

mi_lista1 = mi_lista1 + 'Esto si'

mi_lista2 * 3

# .append() agrega permanente al final de la lista

mi_lista1.append('final')

# El metodo .pop() elimina, si no hay parametro elimina el ultimo

list1 = ['Fisica', 'Biologia', 'Quimica', 'Mate']
list1.pop()
# ['Fisica', 'Biologia', 'Quimica']


list1.pop(1)
# ['Fisica', 'Quimica']

list1 = ['Fisica', 'Biologia', 'Quimica', 'Mate']
elemento = list1.pop(2)
# elemento = 'Quimica'

# Tambien se puede tener una lista bidimensional

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]

matrix[0]

# Primera lista [1,2,3]

matrix[0][0]

# Primer elemento [1]