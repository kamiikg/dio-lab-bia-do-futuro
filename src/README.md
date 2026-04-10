# Código da Aplicação
Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Passo a Passo de Execução

## Setup do Ollama

```bash
# Instalar [Ollama](https://ollama.com/)

# Teste se funciona
ollama run gpt-oss:120b-cloud "Olá!"

# Crie uma chave de API, e em seguida defina as variáveis de ambiente abaixo:
export URL = 'https://ollama.com/api/generate'
export MODELO = 'gpt-oss:120b-cloud'
export API_KEY=sua_chave_api
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
python -m streamlit run app.py

```

## Evidências de Execução

![alt text](../assets/evidencia.png)
