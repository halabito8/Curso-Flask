# Se pueden representar con comillas sencillas o dobles
# Si el string se abre con comillas simples se puede imprimir comillas dobles dentro y viceversa

s1 = "Esto es un string"
s2 = 'Esto tambien es un string'
s3 = "Se puede imprimir ' sin ningun error"

# s4 = "Esto si" es un error"

s5 = "Esto \" no"

# Python tien por predeterminado slicing, que funciona con indices

substr1 = s1[1:]

# Esto le va a asignar desde el primer caracter hasta el ultimo a substr1
# "sto es un string"

substr2 = s2[:6]

# Esto va a agarrar desde el principio hasta (no incluyendo) el sexto caracter
# 'Esto t'

substr3 = s3[4:8]

# Esto va a agarrar desde el cuarto (incluyendo) hasta el octavo (no incluyendo)
# 'uede'

# Tambien se le puede indicar la cantidad de 'saltos'

substr1 = s1[::2]

# Va a recorrer desde el principio hasta el final en 'saltos' de 2
# 'Et su tig'

# Todo se puede combinar

substr2 = s2[3:22:3]

# 'oai   r'

# Tambien se puede indexar negativamente siendo el -1 el final

substr1 = s1[-1]

# 'g'

# Tambien se aplica a slicing

substr2 = s2[::-1]

# 'gnirts nu se neibmat otsE'

# Los strings en python son inmutables, una vez creados no se pueden modificar

s1[0] = 'f'

# Esta linea va a dar error, ya que es inmutable y se le puede asignacion asi

# Largo de un string

len(s1)

# Concatenacion

suma = s1 + s2

# 'Esto es un stringEsto tambien es un string'

# Tambien se puede multiplicar si queremos repetir el mismo string varias veces

print(s1*4)

# 'Esto es un stringEsto es un stringEsto es un stringEsto es un string'

# https://www.shortcutfoo.com/app/dojos/python-strings/cheatsheet
# Aqui hay mas metodos como pasar todo a mayusculas, minusculas, split,
# si el str es numerico, alfanumerico y demas

# Pra imprimir variables hay varias formas, la mas sencilla es esta

nombre = "Rodrigo"
color = "Azul"

print(f"Tu nombre es: {nombre} y tu color favorito es {color}")

# Otra forma mas ordenada es

print("Tu nombre es: {} y tu color favorito es {}".format(nombre,color))