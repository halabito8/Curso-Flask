import uno

print("Afuera de todo en dos.py")

if __name__ == "__main__":
    print("dos.py se corrio")
    uno.func()
else:
    print("dos.py esta siendo importado desde uno.py")