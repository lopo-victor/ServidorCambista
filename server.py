from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

USD_PARA_BRL = 5.0
BRL_PARA_USD = 1 / USD_PARA_BRL

class ConversorDeMoedas:
    def converter(self, quantia, moeda_origem, moeda_destino):
        if moeda_origem == "USD" and moeda_destino == "BRL":
            return quantia * USD_PARA_BRL
        elif moeda_origem == "BRL" and moeda_destino == "USD":
            return quantia * BRL_PARA_USD
        else:
            return "Código de moeda inválido"


servidor = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
servidor.register_instance(ConversorDeMoedas())
print("Servidor RPC em execução na porta 8000...")
servidor.serve_forever()
