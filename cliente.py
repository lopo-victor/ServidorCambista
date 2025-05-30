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

    if moeda_origem not in moedas_essenciais or moeda_destino not in moedas_essenciais:
            print("Moeda inválida. Use apenas os códigos listados acima.")
            return

    try:
        quantia = float(input("Informe o valor a ser convertido: "))
    except ValueError:
        print("Valor inválido. Insira um número.")
        return

    try:
        resultado = server.converter(quantia, moeda_origem, moeda_destino)
        if isinstance(resultado, str):
            print(f"Erro do servidor: {resultado}")
        else:
            print(f"Valor convertido: {resultado:.2f} {moeda_destino}")
    except Exception as e:
        print(f"Ocorreu um erro na conversão: {e}")

if __name__ == "__main__":
    server = xmlrpc.client.ServerProxy("http://localhost:8000")
    while True:
        converter_moeda()
        continuar = input("Deseja realizar outra conversão? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando o conversor de moedas.")
            break
