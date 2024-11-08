def division(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero no permitida."

try:
    numero1 = float(input("Ingresa un número: "))
    numero2 = float(input("Ingresa otro número: "))
    resultado = division(numero1, numero2)
    print("El resultado es:", resultado)
except ValueError:
    print("Error: Por favor ingresa valores numéricos.")

    # try git conexion
