# Sistema de Rastreamento de Entregas via HTTP

## Descrição

Este projeto implementa um sistema simplificado de rastreamento de entregas utilizando o protocolo HTTP. O sistema simula entregadores enviando sua localização para um servidor central, que armazena e disponibiliza esses dados para consulta.

O objetivo é demonstrar, na prática, o funcionamento do protocolo HTTP em um cenário realista de comunicação cliente-servidor.

---

## Objetivo

* Implementar um cenário prático de uso do protocolo HTTP
* Simular comunicação entre clientes e servidor
* Avaliar vantagens e limitações do HTTP no contexto de IoT
* Relacionar o uso com outros protocolos como MQTT e CoAP

---

## Cenário

O sistema representa um ambiente de rastreamento de entregas, onde:

* Entregadores enviam sua localização periodicamente
* Um servidor central recebe e armazena os dados
* Um cliente pode consultar a posição atual dos entregadores

---

## Arquitetura

O sistema segue o modelo cliente-servidor baseado em requisição e resposta:

* Cliente (entregador): envia dados via HTTP (POST)
* Servidor: processa e armazena as informações
* Cliente (consulta): obtém dados via HTTP (GET)

---

## Tecnologias Utilizadas

* Python
* FastAPI
* Requests

---

## Como Executar

### 1. Instalar dependências

```bash
pip install fastapi uvicorn requests
```

### 2. Executar o servidor

```bash
uvicorn server:app --reload
```

### 3. Executar o cliente (simulação de entregador)

```bash
python client.py
```

### 4. Consultar localização

```bash
python dashboard.py
```

---

## Endpoints

### Enviar localização

```
POST /localizacao
```

Body:

```json
{
  "entregador_id": "entregador_1",
  "latitude": -30.03,
  "longitude": -51.23
}
```

---

### Obter localização

```
GET /localizacao/{entregador_id}
```

---

## Análise do Protocolo HTTP

### Vantagens

* Simplicidade de implementação
* Ampla adoção e compatibilidade
* Integração direta com aplicações web
* Adequado para construção de APIs REST

### Desvantagens

* Alto overhead de comunicação (headers grandes)
* Maior latência em comparação com MQTT e CoAP
* Consumo elevado de CPU e banda
* Não otimizado para dispositivos com recursos limitados

---

## Considerações

Embora o HTTP funcione corretamente neste cenário, ele não é a escolha mais eficiente para aplicações de IoT em larga escala. Protocolos como MQTT apresentam melhor desempenho em ambientes com muitos dispositivos e restrições de rede.

O uso do HTTP se justifica principalmente quando há necessidade de integração com sistemas web e simplicidade de implementação.

---

## Limitações do Projeto

* Armazenamento em memória (sem persistência)
* Ausência de mecanismos de autenticação e segurança
* Simulação simplificada sem concorrência real

---

## Conclusão

O protocolo HTTP é adequado para cenários baseados em integração web e comunicação simples entre cliente e servidor. No entanto, para aplicações de IoT com alta escala e restrições de recursos, sua utilização pode gerar ineficiência.

A escolha do protocolo deve sempre considerar os requisitos específicos do sistema.
