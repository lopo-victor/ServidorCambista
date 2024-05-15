import xmlrpc.client

def converter_moeda():
    print("Conversor de Moedas")
    moeda_origem = input("Informe a moeda de origem (USD ou BRL): ").upper()
    moeda_destino = input("Informe a moeda de destino (USD ou BRL): ").upper()
    quantia = float(input("Informe o valor a ser convertido: "))
        
    try:
        quantia_convertida = server.converter(quantia, moeda_origem, moeda_destino)
        print(f"Valor convertido: {quantia_convertida:.2f} {moeda_destino}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

server = xmlrpc.client.ServerProxy("http://localhost:8000")
converter_moeda()
