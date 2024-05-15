# Conversor de Moedas usando XML-RPC

Este é um simples projeto de conversor de moedas que utiliza o protocolo XML-RPC para comunicação entre cliente e servidor. Ele permite a conversão entre as moedas USD (Dólar Americano) e BRL (Real Brasileiro).

## Funcionamento

O projeto consiste em duas partes: um cliente e um servidor.

### Cliente

O cliente é responsável por solicitar a conversão de moeda. Ele solicita ao usuário a moeda de origem, a moeda de destino e a quantidade a ser convertida. Em seguida, envia essa solicitação para o servidor XML-RPC.

### Servidor

O servidor é responsável por receber as solicitações de conversão do cliente e processá-las. Ele possui uma classe `ConversorDeMoedas` que contém um método `converter()` para realizar a conversão das moedas. O servidor registra essa classe para que seus métodos estejam disponíveis para chamadas remotas. Ele fica aguardando por chamadas remotas na porta 8000.


