def main():
    #escribe tu código abajo de esta línea
    nacimiento= int(input("Dame el año de nacimiento: "))
    anoAct= int(input("Dame el año actual: "))
    lustros= (anoAct - nacimiento) / 5
    print("Los lustros que has vivido son:", lustros)



if __name__ == '__main__':
    main()
