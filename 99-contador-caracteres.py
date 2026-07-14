enunciado = input("Por favor ingresa el texto a contar:")

if len(enunciado) == 0:
    print(f"El texto no tiene caracter alguno.")

if len(enunciado) == 1:
    print(f"El texto tiene {len(enunciado)} caracter.")

if len(enunciado) > 1:
    print(f"El texto tiene {len(enunciado)} caracteres.")