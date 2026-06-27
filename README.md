# Sistema de Rastreamento de Entregas via HTTP

## Descrição

Este projeto implementa uma **versão inicial e simplificada** de um sistema de rastreamento utilizando o protocolo HTTP.

O objetivo é demonstrar, na prática, a comunicação cliente-servidor através de requisições HTTP.

Esta versão é apenas uma **prova de conceito**, sem foco em escalabilidade ou arquitetura completa.

---

## Protocolo Utilizado

O protocolo utilizado é o **HTTP**, com operações básicas:

* POST para envio de dados
* GET para consulta

---

## Tecnologias Utilizadas

* Python
* Flask
* uv (gerenciamento de ambiente e dependências)

---

## Cenário Implementado

* Um cliente envia dados de localização
* O servidor armazena os dados em memória
* Um cliente consulta os dados enviados

---

## Resultado Esperado

* Receber dados via HTTP (POST)
* Armazenar temporariamente
* Retornar os dados via HTTP (GET)

---

## Estrutura do Projeto

```id="w4ksmn"
.
├── app.py
├── pyproject.toml
└── README.md
```

---

## Instalação

### 1. Instalar o uv

```bash id="6lbm0u"
pip install uv
```

### 2. Criar ambiente e instalar dependências

```bash id="l8y3b0"
uv venv
uv sync
```

---

## Execução

```bash id="2q9b3c"
python app.py
```

Servidor disponível em:

```id="n4d2ye"
http://localhost:5000
```

---

## Teste da API

### Enviar dados

```bash id="v5x9rk"
curl.exe -X POST http://localhost:5000/enviar -H "Content-Type: application/json" -d "{\"id\":\"caminhao_01\",\"lat\":-30.03,\"lon\":-51.23}"
```

---

### Consultar dados

```id="z3p8xk"
http://localhost:5000/consultar/caminhao_01
```

---

## Arquitetura Atual

* Cliente → envia dados (HTTP POST)
* Servidor → armazena em memória
* Cliente → consulta dados (HTTP GET)

---

## Arquitetura Futura (Planejada)

* Persistência em banco de dados
* Suporte a múltiplos clientes simultâneos
* Autenticação
* Interface web
* Avaliação de protocolos como MQTT e CoAP

---

## Limitações

* Armazenamento em memória
* Sem autenticação
* Sem escalabilidade
* Implementação simplificada
