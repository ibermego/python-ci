from mathematic import add, multiply, substract, divide

if __name__ == '__main__':
    print('Main program para ayudarle con las mates')

    accion = input("Qué quieres hacer? 's' para sumar, 'm' para multiplicar: ")

    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))

    if accion == 's':
        resultado = add(num1, num2)
        print(f"Resultado de la suma: {resultado}")
    else:
        pass  # Aquí puedes meter más acciones después
    