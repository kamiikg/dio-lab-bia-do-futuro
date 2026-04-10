import json
import pandas as pd
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# acessa as variáveis
url = os.getenv('URL')
modelo = os.getenv('MODELO')
api_key = os.getenv('API_KEY')

# Carregar Dados
perfil = json.load(open('../data/perfil_investidor.json'))
transacoes = pd.read_csv('../data/transacoes.csv')
historico = pd.read_csv('../data/historico_atendimento.csv')
produtos = json.load(open('../data/produtos_financeiros.json'))
