# Para crear paquetes en python aparte del directorio se necesita 
# que la carpeta tenga un archivo llamado __init__.py
# este archivo no debe de tener nada escrito, nada mas python lo necesita para saber que es un paquete

# Para importar todo el archivo
from Paquete import Pqt_pral
from Paquete.sub_Paquete import sub_Pqt

# Si se importa todo el archivo las funciones se tienen que llamar con .
Pqt_pral.func1()
Pqt_pral.func2()

sub_Pqt.func4()


# Para importar solo funciones
from Paquete.Pqt_pral import func1
from Paquete.sub_Paquete.sub_Pqt import func3

func1()
func3()
