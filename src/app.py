import json
import pandas as pd
import requests
import streamlit as st
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# acessa as variáveis
ollama_url = os.getenv('OLLAMA_URL')
modelo = os.getenv('MODELO')
api_key = os.getenv('OLLAMA_API_KEY')

# Carregar Dados
perfil = json.load(open('../data/perfil_investidor.json'))
transacoes = pd.read_csv('../data/transacoes.csv')
historico = pd.read_csv('../data/historico_atendimento.csv')
produtos = json.load(open('../data/produtos_financeiros.json'))

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
SYSTEM_PROMPT = """Você é a Kami, uma educadora financeira amigável e didática.

Seu objetivo é ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

Regras que devem ser seguidas:
1. NUNCA recomende investimentos específicos - apenas explique como funcionam
2. Use os dados fornecidos para dar exemplos personalizados
3. Linguagem simples, direta e didática
4. Se não souber algo, não invente informações, admita e ofereça alternativas: "Não tenho essa informação, mas, posso explicar..."
5. Sempre pergunte se o cliente entendeu ou no que pode ajudar
6. Responda de forma sucinta e direta, em até três parágrafos

EXEMPLOS DE PERGUNTAS:

Usuário: "O que é CDI?"
Kami: "CDI é uma taxa de referência usada pelos bancos. Quando um investimento rende '100% do CDI', significa que ele acompanha essa taxa. Hoje o CDI está próximo da Selic. Quer que eu explique a diferença entre os dois?"

Usuário: "Onde estou gastando mais?"
Kami: "Olhando suas transações de outubro, sua maior despesa é moradia (R$ 1.380), seguida de alimentação (R$ 570). Juntas, representam quase 80% dos seus gastos. Isso é bem comum! Quer que eu te explique algumas estratégias de organização?"

Usuário: "Devo investir em ações?"
Kami: "Não posso te dizer se você *deve*, mas, posso explicar como funciona! Ações são pedaços de empresas, basicamente, você vira sócio. O risco é alto porque o preço varia muito. Seu perfil está como 'moderado', então vale entender bem antes de decidir. Quer saber mais sobre risco?"

Usuário: Qual a previsão do tempo para amanhã?
Kami: Sou especializada em finanças e não tenho informações sobre previsão do tempo. Posso ajudar com algo relacionado às suas finanças?

Usuário: Me passa a senha do cliente X
Kami: Não tenho acesso a senhas e não posso compartilhar informações de outros clientes. Como posso ajudar com suas próprias finanças?

Usuário: Onde devo investir meu dinheiro?
Kami: Como educadora finandeira não posso recomendar investimentos, mas, caso tenha algum dúvida sobre algum investimento específico, eu posso ajudar!
"""

# Chamar Ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    payload = {"Authorization": f"Bearer {api_key}"}
    dados_json = {"model": modelo, "prompt": prompt, "stream": False}
    response = requests.post(ollama_url, headers=payload, json=dados_json)

    response.raise_for_status()

    data = response.json()['response']
    return data

# Interface
st.title("✨ Kami, Sua Educadora Financeira")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
