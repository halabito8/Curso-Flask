def func():
    return print('Funcion dentro de uno')

print("Afuera de todo en uno.py")

if __name__ == "__main__":
    print("uno.py se corrio")
else:
    print("uno.py esta siendo importado desde dos.py")
    