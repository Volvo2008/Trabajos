# Programa para calcular el IMC
peso=float(input("Peso (Kg): "))
altura=float(input("Altura (M): "))
imc = peso / (altura ** 2)
print("Su IMC es: ", imc)