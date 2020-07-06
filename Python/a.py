def nuevo_decorador(func):

    def wrap_func():
        print ("Hola\nAntes de la func()")

        func()

        print ("Adios\nDespues func()")

    return wrap_func

@nuevo_decorador
def necesita_decorador():
    print ("Codigo dentro de func()")

necesita_decorador()
