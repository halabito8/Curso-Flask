# Las funciones deben de llevar la palabra reservada def antes

def func1():
    print('func1')


# Se le pueden pasar argumentos
def nombre(nomb):
    return f'Tu nombre es {nomb}'

print(nombre('Jose'))

# Tu nombre es Jose

# Los argumentos tambien pueden tener defaults

def color(col='Amarillo'):
    return f"Tu color favorito es {col}"

print(color())
# Tu color favorito es Amarillo

print(color('Verde'))
# Tu color favorito es Verde

# Cuando queremos meter el nombre de una nueva funcion pero no quermos que haga nada
# tomamos la palbra reservada pass

def Nada():
    pass

# Cuando llamemos a Nada no va a hacer nada

#Si queremos asegurarnos de que la asigancion sea correcta se puede hacer lo siguiente
def suma(n1,n2):
    return n1+n2

suma(n1=3,n2=4)

# No se puede hacer parcialmente

def multi(n1,n2,n3,n4):
    return n1*n2*n3*n4

multi(n1=8,4,5,6)
# Tiene que ser todos los parametros o ninguno

