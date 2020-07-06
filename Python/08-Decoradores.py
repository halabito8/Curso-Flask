# Los decoradores nos ayudan a que nuestro codigo este limpio
# Estos son funciones que vamos a hacer repetidamente

# Se pueden pasar funciones como parametros de esta manera
def hello():
    return 'Hola Jose!'

def other(func):
    print('Otro funcionamiento')
    print(func())

other(hello)

# Otro funcionamiento
# Hola Jose!

def new_decorator(func):

    def wrap_func():
        print ("Codigo que se ejecuta antes de la func()")

        func()

        print ("Codigo que se ejecuta despues func()")

    return wrap_func

def necesita_decorador():
    print ("Codigo dentro de func()")

necesita_decorador()
# Si la llamamos solita nos imprime:
# Codigo dentro de func()


# Reasigna a necesita_decorador esta funcionalidad extra 
necesita_decorador = new_decorator(necesita_decorador)

necesita_decorador()

# Codigo que se ejecuta antes de la func()
# Codigo dentro de func()
# Codigo que se ejecuta despues func()

# Una forma mas facil es

def nuevo_decorador(func):

    def wrap_func():
        print ("Hola\nAntes de la func()")

        func()

        print ("Adios\nDespues func()")

    return wrap_func

@nuevo_decorador
def necesita_decorador2():
    print ("Codigo dentro de func()")

necesita_decorador2()

# Puede ejecutar codigo antes, despues o antes y despues