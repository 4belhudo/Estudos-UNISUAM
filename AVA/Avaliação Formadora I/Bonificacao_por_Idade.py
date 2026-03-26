nome = str(input("Informe o nome da pessoa contratada: "))
idade = int(input(f"Informe a idade de {nome}: "))
salario_original = float(input(f"Informe o ganho salarial de {nome}: "))

if((salario_original>=1600) and (idade>=18)):
    salario = salario_original+1000
    print(f"O novo ganho salarial de {nome} será de R$ {salario:.2f}.\nOcorreu um acréscimo de R$ 1000,00 ao ganho salarial original de R$ {salario_original:.2f}.")
else:
    print(f"O ganho salarial de {nome} permanecerá como R$ {salario_original:.2f}, pois não atende os requisitos para uma bonificação.")