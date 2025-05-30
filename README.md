# Conversor de Moedas usando XML-RPC

Este é um projeto simples para cambio entre moedas que utiliza o protocolo XML-RPC para comunicação entre cliente e servidor. o sistema realiza consultas em tempo real à API de cotações da [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para obter as taxas de câmbio.

## 📦 Funcionamento

O projeto consiste em duas partes: um cliente e um servidor.

### 💻 cliente.py

O cliente é responsável por solicitar a conversão de moeda. Ele solicita ao usuário a moeda de origem, a moeda de destino e a quantidade a ser convertida. Em seguida, envia essa solicitação para o servidor XML-RPC.

### 🖥️  Servidor

O servidor é responsável por receber as solicitações de conversão do cliente e processá-las.
* Implementa a classe ConversorDeMoedas, que contém os métodos converter() e obter_taxa().

* Utiliza a API da AwesomeAPI para buscar taxas de câmbio atualizadas.

* Executa na porta 8000 via SimpleXMLRPCServer.

### 🚀 Execução
#### Requisitos:
* Python 3

#### Executando o servidor:
```bash
python3 servidor.py
```



#### Executando o cliente:
```bash
python3 cliente.py
```

## ✅ Conclusão
Este projeto foi desenvolvido como um caso de estudo acadêmico, com o objetivo de aprofundar o entendimento sobre sistemas distribuídos. Através da implementação do protocolo XML-RPC, foi possível compreender na prática:

* Como funciona a comunicação cliente-servidor via chamadas remotas.

* A estrutura e troca de mensagens no protocolo XML-RPC.

* A integração de APIs externas em sistemas distribuídos.

* Conceitos de serialização, transporte HTTP e robustez na comunicação entre processos.

* O projeto agregou significativamente ao aprendizado técnico, permitindo a aplicação de conceitos teóricos em um cenário funcional e realista.


