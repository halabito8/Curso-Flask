# Para crear una clase
class Tienda():
    pass

# Para el constructor vamos a utilizar la variable reservada __ini__
# Siempre se tiene que pasar como primer parametro self
class Marca():
    def __init__(self, nombre):
        self.nombre = nombre

ciel = Marca('Ciel')
coca = Marca(nombre='Coca')

print(ciel.nombre)
print(coca.nombre)

# Ciel
# Coca

# Tambien puede tener funciones internas
class Circulo():
    pi = 3.14

    def __init__(self, radio=1):
        self.radio = radio
        # Si no nos dan un radio inicial el default es 1

    def area(self):
        return (self.radio **2) * Circulo.pi
        # El doble asterisco es para potencias

    def setRadio(self, radio):
        self.radio = radio

    def getRadio(self):
        return self.radio


c = Circulo()
c.setRadio(2)
# Lineas 38 y 39 se pueden abreviar c = Circulo(2)

print('Radio: ')
print(c.getRadio())
print('Area: ')
print(c.area())

# Tambien existe la herencia
class Animal():
    def __init__(self):
        print("Animal creado")

    def report(self):
        print("Animal")

    def come(self):
        print("Comiendo")


class Perro(Animal):
    def __init__(self):
        # Animal.__init__(self) se sobreescribe
        print("Perro creado")

    def report(self):
        # Tambien esta funcion se sobreescribe
        print("Perro")

    def ladra(self):
        print("Woof!")

d = Perro()
d.report()
d.come()
d.ladra()

# Perro creado
# Perro
# Comiendo
# Woof!

# Metodos especiales
# Las clases vienen con clases definidas pero estas se pueden sobreescribir
class Libro():
    def __init__(self, titulo, autor, paginas):
        print("Libro creado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        # __repr__ es la representacion del objeto
        # IMPORTANTE no se regresa print, nada mas el puro string
        return f"Titulo:{self.titulo} , autor:{self.autor}, paginas:{self.paginas}"

    def __len__(self):
        return self.paginas


libro = Libro("Torre Oscura!", "Stephen King", 327)

#Metodos especiales
print(libro)
print(len(libro))

# Libro creado
# Titulo:Torre Oscura! , autor:Stephen King, paginas:327
# 327