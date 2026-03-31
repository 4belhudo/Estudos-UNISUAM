'''
Programa: Pedágio Inteligente
Por: Ana Lívia, Paulo Cezar, Sérgio
Requisitos de Projeto
    1. Variáveis: Definir nomes claros para o tipo de veículo, valor da base,
    hora da passagem e valor final.
    2. Tabelha de Preços Base:
        1. Carro de Passeio: R$ 10,00.
        2. Caminhão (por eixo): R$ 15,00.
        3. Motocicleta: R$ 5,00.
    3. Lógica de Negócio (Estruturas Condicionais):
        1. Regra de Pico: Passagem entre 6h e 9h ou 17h e 20h, adicionar taxa de 20%.
        2. Regra de Isenção: Veículos governamentais são isentos.
    4. Saída: Exibir tipo de véiculo e valor total calculado.
'''

# Tabelha informacional para o usuário:
print(
"\n| Nº de ID | Tipo de Veículo  |"
"\n| 01       | Carro de passeio |"
"\n| 02       | Motocicleta      |"
"\n| 03       | Caminhão         |"
"\n| 04       | Veículo oficial* |"
"\n* Veículos oficiais são: veículos pertencentes a hospitais, veículos do corpo de bombeiros, veículos pertencentes à PM, PRF, PF e PC."
)

tipo_veiculo = int(input("Informe o Nº de ID do tipo de veículo: "))
while tipo_veiculo not in [1, 2, 3, 4]:
    tipo_veiculo = int(input(
        "Nº de ID inválido, por favor insira um Nº de ID válido."
        "\nInforme o Nº de ID do tipo de veículo: "
        ))

'''
Entre as linhas 27 e 32, um usuário informa o tipo de veículo e
o programa obriga que a resposta seja um valor INTEIRO num raio de 1 à 4.
'''

# VEÍCULO OFICIAL - Impede processamento desnecessário
if tipo_veiculo == 4:
    print(
    "Tipo de Veículo: Veículo Oficial."
    "\nValor à cobrar: Isento de cobranças."
    )
else:
    horario = input("Insira o horário atual (0-23): ")
    while not ((horario>=0) and (horario<=23)):
        horario = int(input(
                "Horário inválido, por favor insira um horário válido."
                "\nInsira o horário atual (0-23): "
                ))
    
    '''
    Entre as linhas 45 e 51, um usuário informa a hora atual, porém, o programa
    aceita apenas a hora total e não os minutos. Qualquer valor que não seja um
    valor inteiro ou não esteja num raio de 0 à 23 será recusado.
    '''

    # HORÁRIO DE PICO
    if (horario>=6 and horario<=9) or (horario>=17 and horario<=20):
            
        # CARRO DE PASSEIO
        if tipo_veiculo == 1:
            print(
                "Tipo de Veículo: Carro de Passeio."
                f"\nValor à cobrar: R$ {10+(10*0.2):.2f}."
            )
            
        # MOTOCICLETA
        elif tipo_veiculo == 2:
            print(
                "Tipo de Veículo: Motocicleta"
                f"\nValor à cobrar: R$ {5+(5*0.2):.2f}."
            )
            
        # CAMINHÃO
        elif tipo_veiculo == 3:
            eixos = int(input("Informe o número de eixos deste caminhão: "))
            print(
                "Tipo de Veículo: Caminhão"
                f"\nValor à cobrar: R$ {(15*eixos)+((15*eixos)*0.2):.2f}."
            )
            
        # VEÍCULO OFICIAL
        elif tipo_veiculo == 4:
            print(
                "Tipo de Veículo: Veículo Oficial."
                "\nValor à cobrar: Isento de cobranças."
            )
    
# HORÁRIO NORMAL
    else:

        # CARRO DE PASSEIO
        if tipo_veiculo == 1:
            print(
                "Tipo de Veículo: Carro de Passeio."
                "\nValor à cobrar: R$ 10.00."
            )
            
        # MOTOCICLETA
        elif tipo_veiculo == 2:
            print(
                "Tipo de Veículo: Motocicleta"
                "\nValor à cobrar: R$ 5.00."
            )

        # CAMINHÃO
        elif tipo_veiculo == 3:
            eixos = int(input("Informe o número de eixos deste caminhão: "))
            print(
                "Tipo de Veículo: Caminhão"
                f"\nValor à cobrar: R$ {15*eixos:.2f}."
            )