import xmlrpc.client

moedas_essenciais = {
    "BRL": "Real Brasileiro",
    "USD": "Dólar Americano",
    "CAD": "Dólar Canadense",
    "EUR": "Euro",
    "GBP": "Libra Esterlina",
    "BTC": "Bitcoin",
    "ETH": "Ethereum"
}

def exibir_moedas_disponiveis():
    print("Moedas disponíveis para conversão:")
    for codigo, nome in moedas_essenciais.items():
        print(f"{codigo} - {nome}")
    print()  # Linha em branco para melhor legibilidade


def converter_moeda():
    print("Conversor de Moedas")
    exibir_moedas_disponiveis()

    moeda_origem = input("Informe a moeda de origem: ").upper()
    moeda_destino = input("Informe a moeda de destino: ").upper()
    quantia = float(input("Informe o valor a ser convertido: "))
        
    try:
        quantia_convertida = server.converter(quantia, moeda_origem, moeda_destino)
        print(f"Valor convertido: {quantia_convertida:.2f} {moeda_destino}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

server = xmlrpc.client.ServerProxy("http://localhost:8000")
converter_moeda()
