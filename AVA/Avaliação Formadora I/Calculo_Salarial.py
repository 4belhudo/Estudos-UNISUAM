salario = float(input("Para calcular o seu novo salário, informe o salário atual: "))
if(salario<=500):
    salario = salario + (salario*0.05)
    print(f"Seu salário terá um aumento de 5%, totalizando em um novo ganho de R$ {salario:.2f}.")
elif((salario>500) and (salario<=1200)):
    salario = salario + (salario*0.12)
    print(f"Seu salário terá um aumento de 12%, totalizando em um novo ganho de R$ {salario:.2f}.")
elif(salario>1200):
    print(f"Seu salário permanecerá R$ {salario:.2f}.")