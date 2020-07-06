# Los diccionarios se representan con {}
# Los diccionarios tienen por llave una palabra en vez de un numero
# Los diccionarios NO son ordenados por lo que si los imprimimos dos veces 
# podremos llegar a tener dos resultados diferentes

mi_dic = {"llave1":'valor1','llave2':"valor2"}

print(mi_dic['llave2'])

# Tambien se puede tener un diccionario con diferentes valores dentro como listas, ints, str

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Para llamar toda la lista en la llave 3

my_dict['key3']

# Para un valor en especifico

my_dict['key3'][0]

# Tambien se le puede dar asiganacion al dict

d = {}

d['animal'] = 'Perro'
d['respuesta'] = 42

# {'animal': 'Perro', 'respuesta': 42}

# Tambien se puede tener un dict nested

d = {'key1':{'nestkey':{'subnestkey':'value'}}}

d['key1']['nestkey']['subnestkey']

# En la linea 33 se esta teniendo tres diccionarios uno dentro del otro

##################################
# Metodos de los dict

d = {'key1':1,'key2':2,'key3':3}

# .keys() retorna solo las llaves usadas 
print(d.keys())

# dict_keys(['key1', 'key2', 'key3'])

# .values() retorna solo los valores 
print(d.values())

# dict_values([1, 2, 3])

# .items() retorna ambos
print(d.items())

# dict_items([('key1', 1), ('key2', 2), ('key3', 3)])