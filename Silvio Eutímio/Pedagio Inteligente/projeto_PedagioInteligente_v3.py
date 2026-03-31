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

# 1. Configurações de Preços
TABELA_PRECOS = {
    1: {"nome": "Carro de Passeio", "base": 10.00},
    2: {"nome": "Motocicleta", "base": 5.00},
    3: {"nome": "Caminhão", "base": 15.00}, # Valor por eixo
    4: {"nome": "Veículo Oficial", "base": 0.00}
}

print("\nID | Tipo de Veículo\n" + "-"*25)
for id_veiculo, dados in TABELA_PRECOS.items():
    print(f"{id_veiculo:02d} | {dados['nome']}")

# 2. Entrada de Dados Segura (Usando a lógica que expliquei antes)
def obter_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("❌ Erro! Digite apenas números inteiros.")

# 3. Coleta de informações
tipo_veiculo = 0
while tipo_veiculo not in TABELA_PRECOS:
    tipo_veiculo = obter_inteiro("\nInforme o Nº de ID do tipo de veículo: ")

if tipo_veiculo == 4:
    print("\nTipo: Veículo Oficial\nValor: Isento de cobranças.")
else:
    # Validação do horário (0-23)
    hora = -1
    while not (0 <= hora <= 23):
        hora = obter_inteiro("Insira o horário atual (0-23): ")

    # 4. Lógica de Negócio Centralizada
    valor_base = TABELA_PRECOS[tipo_veiculo]["base"]
    
    # Se for caminhão, pergunta os eixos
    if tipo_veiculo == 3:
        eixos = obter_inteiro("Informe o número de eixos: ")
        valor_base *= eixos

    # Regra de Pico (Adiciona 20%)
    if (6 <= hora <= 9) or (17 <= hora <= 20):
        # Cálculo: $$ValorFinal = ValorBase \times 1.20$$
        valor_final = valor_base * 1.20
        status_pico = "(Tarifa de Pico Aplicada)"
    else:
        valor_final = valor_base
        status_pico = ""

    # 5. Saída Única
    print(f"\n--- Recibo de Pedágio ---")
    print(f"Veículo: {TABELA_PRECOS[tipo_veiculo]['nome']}")
    print(f"Horário: {hora}h {status_pico}")
    print(f"Total a pagar: R$ {valor_final:.2f}")