print("Siga a tabela abaixo para organização e melhor fluxo de trabalho.\n"
"\n| ID | Tipo de Veículo  |"
"\n| 01 | Carro de passeio |"
"\n| 02 | Motocicleta      |"
"\n| 03 | Caminhão         |"
"\n| 04 | Veículo oficial* |"
"\n* Veículos oficiais são: veículos pertencentes a hospitais, veículos do corpo de bombeiros, veículos pertencentes à PM, PRF, PF e PC.")

'''
A região acima é, apenas, para organização da tabela, imaginando que o usuário não tem acesso a ela
'''

processo = int(input("Deseja iniciar o processo de avaliação do pedágio? (1 - Sim / 2 - Não): "))
while processo not in [1, 2]:
    print("Opção inválida. Por favor tente novamente.")
    processo = int(input("Deseja iniciar o processo de avaliação do pedágio? (1 - Sim / 2 - Não): "))

'''
A região acima é pra validar se você deseja ou não dar início ao programa
Eu não encontrei formas de loopar o que tá em cima pro programa ficar sempre ativo
então o programa encerra se você digitar 2
'''

while processo == 1:
    tipo_veiculo = int(input("Informe o ID do veículo: "))          # Aqui o usuario informa o ID e o programa identifica o tipo do veiculo
    while tipo_veiculo not in [1, 2, 3, 4]:                         # Aqui o programa valida se o ID existe, se não existir, pede pra informar novamente o ID
        print("ID de veículo inválido. Por favor tente novamente.")
        tipo_veiculo = int(input("Informe o ID do veículo: "))
    match tipo_veiculo:
        case 1:
            print("O veículo é um carro de passeio. Informe o horário atual: ")
            hora_atual = int(input("Hora atual (0-23): "))          # Eu tinha tentado uma forma de validar o horário automaticamente, mas não funcionou oq eu tinha achado
            if((hora_atual >= 6 and hora_atual <= 9) or (hora_atual >= 17 and hora_atual <= 20)):
                print("O valor a ser pago é 'R$ 12.00', devido ao horário de pico.")
            else:
                print("O valor a ser pago é 'R$ 10.00'.")
            processo = int(input("Deseja avaliar outro veículo? (1 - Sim / 2 - Não): "))
        case 2:
            print("O veículo é uma motocicleta. Informe o horário atual: ")
            hora_atual = int(input("Hora atual (0-23): "))
            if((hora_atual >= 6 and hora_atual <= 9) or (hora_atual >= 17 and hora_atual <= 20)):
                print("O valor a ser pago é 'R$ 6.00', devido ao horário de pico.")
            else:
                print("O valor a ser pago é 'R$ 5.00'.")
            processo = int(input("Deseja avaliar outro veículo? (1 - Sim / 2 - Não): "))
        case 3:
            print("O veículo é um caminhão. Informe o número de eixos: ")
            eixos = int(input("Número de eixos: "))         # Aqui o usuário informa o número de eixos do caminhão, e o programa calcula o valor a ser pago, considerando o número de eixos e o horário     
            valor = 15.00 * eixos
            print("Informe o horário atual: ")
            hora_atual = int(input("Hora atual (0-23): "))
            if((hora_atual >= 6 and hora_atual <= 9) or (hora_atual >= 17 and hora_atual <= 20)):
                print(f"Por cada eixo é cobrado um valor de 'R$ 15.00'. O valor a ser pago é 'R$ {(valor+valor*0.2):.2f}', devido ao horário de pico e número de eixos.")
            else:
                print(f"O valor a ser pago é 'R$ {valor:.2f}', devido ao número de eixos.")
            processo = int(input("Deseja avaliar outro veículo? (1 - Sim / 2 - Não): "))
        case 4:
            print("Veículo oficial. Isento de pagamento.")
            processo = int(input("Deseja avaliar outro veículo? (1 - Sim / 2 - Não): "))
if processo == 2:
    print("Processo de avaliação do pedágio encerrado.")