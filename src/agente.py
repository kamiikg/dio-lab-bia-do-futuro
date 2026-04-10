import json
import requests
from config import url, modelo, api_key, perfil, transacoes, historico, produtos

# Montar Contexto
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# System Prompt
with open('../docs/03-prompts.md', 'r', encoding='utf-8') as f:
    system_prompt = f.read()

# Chamar Ollama
def perguntar(msg):
    prompt = f"""
    {system_prompt}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    payload = {"Authorization": f"Bearer {api_key}"}
    dados_json = {"model": modelo, "prompt": prompt, "stream": False}
    response = requests.post(url, headers=payload, json=dados_json)

    response.raise_for_status()

    data = response.json()['response']
    return data
