try:
    num1 = float(input("Informe o 1o Número: "))
    num2 = float(input("Informe o 2o Número: "))
    num3 = float(input("Informe o 3o Número: "))
except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")
print(f"Os números informados são: {num1}, {num2} e {num3}")
soma = num1 + num2 + num3
print(f"A soma é: {soma:.2f}")
print(f"A média é: {soma/3:.2f}")