#Python va a buscar las variables de la siguiente manera
# **LEGB Rule.**
#
# L: Local — En la funcion, dentro de def
#
# E: Enclosing function locals — De donde se invoco la funcion
#
# G: Global (module) — En todo el documento
#
# B: Built-in (Python) — Pre-asigandos, construidas directamente desde python
# Si no encuentra Syntax Error...

# Ejemplo de variables locales
x = 50

def func(x):
    print('x es', x)
    x = 2
    print('Cambiamos x localmente a ', x)

func(x)
print('x sigue siendo', x)

# x es 50
# Cambiamos x localmente a  2
# x sigue siendo 50

# Ejemplo funciones que encierran a otras
name = 'Nombre global'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()

# Hello Sammy