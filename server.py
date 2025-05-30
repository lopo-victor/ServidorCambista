from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import requests


USD_PARA_BRL = 5.0
BRL_PARA_USD = 1 / USD_PARA_BRL

class ConversorDeMoedas:
    def obter_taxa(self, moeda_origem, moeda_destino):
        if moeda_origem == moeda_destino:
            return 1.0  # conversão entre moedas iguais
        
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
        try:
            resposta = requests.get(url, timeout=5)
            resposta.raise_for_status()
            dados = resposta.json()
            chave = f"{moeda_origem}{moeda_destino}"
            if chave in dados and 'bid' in dados[chave]:
                return float(dados[chave]['bid'])     
            
        except Exception as e:
            print(f"[ERRO] Falha ao obter taxa: {e}")
            
        return None

    def converter(self, quantia, moeda_origem, moeda_destino):
        if not isinstance(quantia, (int, float)):
            return "Erro: quantia inválida"
        
        taxa = self.obter_taxa(moeda_origem, moeda_destino)

        if taxa is None:
            return "Erro: não foi possível obter a taxa de câmbio"
        
        return quantia * taxa


servidor = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
servidor.register_instance(ConversorDeMoedas())
print("Servidor RPC em execução na porta 8000...")
servidor.serve_forever()
