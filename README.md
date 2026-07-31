# ⚙️ API de Processamento e Análise de Pedidos (ERP Protheus)

> **Back-End / Engine de ETL:** API RESTful desenvolvida em Python com **FastAPI**, **Pandas** e **NumPy** para automação da leitura, sanitização de dados e cálculo de KPIs operacionais de planilhas exportadas do ERP TOTVS Protheus.

---

## 🎯 Objetivo do Projeto

Automatizar o pipeline de tratamento de dados de saldo e liberação de pedidos comerciais. 

A API recebe o arquivo em Excel exportado do ERP, realiza a conversão e limpeza de tipos numéricos (moedas e quantidades), aplica regras de negócio para verificação de saldo disponível e calcula o percentual de **representatividade do pedido** liberado em segundos.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/):** Linguagem principal.
- **[FastAPI](https://fastapi.tiangolo.com/):** Framework para construção da API assíncrona de alta performance.
- **[Pandas](https://pandas.pydata.org/):** Tratamento, conversão, cruzamento e agregação de dados.
- **[NumPy](https://numpy.org/):** Criação de vetores lógicos e condicionais de status (`np.where`).
- **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI para execução da aplicação.

---

## 🧠 Regras de Negócio e Processamento (ETL)

O arquivo script `tratar_dados.py` executa os seguintes passos principais:

1. **Sanitização de Dados:** Tratamento e padronização de strings formatadas em padrão brasileiro (`1.000,00`) para valores decimais `float` navegáveis no Pandas.
2. **Classificação de Saldo:** Avaliação lógica do estoque com status de aprovação/reprovação por item.
3. **Cálculo de Métricas:**
   - Valor total individual de cada item (`Quantidade x Preço de Venda`).
   - Valor total liberado por pedido (*Valor Total com Saldo Aprovado*).
   - Percentual de **Representatividade** do saldo em relação ao valor total do pedido.
4. **Exportação de Payload:** Retorno estruturado em JSON contendo o resumo consolidado por pedido e o detalhamento item a item para o consumo do Front-End.

---

## 🔌 Endpoints da API

### `POST /tratar`
Recebe um arquivo `.xlsx` enviado via formulário (`UploadFile`) e retorna o payload com os dados consolidados.

- **Requisição:** `multipart/form-data`
- **Validação:** Aceita apenas extensões `.xlsx` (retorna erro HTTP 400 em caso inválido).
