# 🎯 Agente Financeiro Inteligente — Planejamento de Metas

> Lab desenvolvido como parte do bootcamp **"Bia do Futuro"** da [Digital Innovation One (DIO)](https://www.dio.me/), com foco na criação de um agente financeiro baseado em IA Generativa.

---

## 📌 Sobre o Projeto

Este projeto consiste no desenvolvimento de uma **agente financeira inteligente** especializada em **planejamento de metas financeiras**. A agente é capaz de analisar o perfil do usuário, seu histórico de transações e produtos financeiros disponíveis para oferecer recomendações personalizadas e proativas sobre como alcançar objetivos financeiros de curto, médio e longo prazo.

A agente vai além de um simples chatbot reativo: ela **antecipa necessidades**, **personaliza sugestões** com base no contexto de cada cliente e atua de forma consultiva, garantindo segurança e confiabilidade nas respostas.

---

## ✨ Funcionalidades

- 🗺️ **Definição de metas financeiras** — viagem, reserva de emergência, aposentadoria, compra de imóvel, etc.
- 📊 **Análise do perfil do investidor** — tolerância a risco, horizonte de tempo e situação atual
- 💳 **Leitura do histórico de transações** — identificação de padrões de gastos e oportunidades de economia
- 🏦 **Sugestão de produtos financeiros** — indicação de produtos alinhados a cada meta
- 🔒 **Respostas seguras e confiáveis** — mecanismos anti-alucinação com grounding em dados reais

---

## 🗂️ Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md
├── 📄 .env.example
├── 📄 .gitignore
│
├── 📁 data/                            # Dados mockados para o agente
│   ├── historico_atendimento.csv       # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json          # Perfil e preferências do cliente (JSON)
│   ├── produtos_financeiros.json       # Produtos e serviços disponíveis (JSON)
│   └── transacoes.csv                  # Histórico de transações (CSV)
│
├── 📁 docs/                            # Documentação do projeto
│   ├── 01-documentacao-agente.md       # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md         # Estratégia de dados
│   ├── 03-prompts.md                   # Engenharia de prompts
│   ├── 04-metricas.md                  # Avaliação e métricas
│   └── 05-pitch.md                     # Roteiro do pitch
│
├── 📁 src/                             # Código da aplicação
│   ├── app.py                          # Aplicação principal (Streamlit)
│   ├── agente.py                       # Lógica do agente financeiro
│   ├── config.py                       # Configurações e variáveis de ambiente
|   └── requirements.txt                # Dependências do projeto
│
└── 📁 assets/                          # Imagens e diagramas
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10+
- [Ollama](https://ollama.com/) instalado e rodando localmente

### Instalação

```bash
# Clone o repositório
git clone https://github.com/kamiikg/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# Instale as dependências
pip install -r requirements.txt

# Configure sua chave de API
cp .env.example .env
# Edite o .env com sua chave de API

# Execute a aplicação
streamlit run src/app.py
```

---

## 🤖 Prompts da Agente

O comportamento da agente é definido por um **system prompt** que estabelece:

- A **persona** da agente: consultora financeira empática, objetiva e didática
- As **restrições de segurança**: a agente nunca inventa dados — só responde com base nos dados fornecidos
- Os **fluxos de conversa**: saudação → diagnóstico financeiro → definição de metas → sugestão de plano

Os prompts completos e os exemplos de interação estão documentados em [`docs/03-prompts.md`](docs/03-prompts.md).

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Ferramenta |
|---|---|
| **LLM** | [Ollama](https://ollama.com/) |
| **Interface** | [Streamlit](https://streamlit.io/) |
| **Dados** | CSV / JSON (mockados) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/) |

---

## 📚 Documentação

| Documento | Descrição |
|---|---|
| [`01-documentacao-agente.md`](docs/01-documentacao-agente.md) | Caso de uso, persona e arquitetura |
| [`02-base-conhecimento.md`](docs/02-base-conhecimento.md) | Estratégia de dados e base de conhecimento |
| [`03-prompts.md`](docs/03-prompts.md) | Engenharia de prompts e exemplos de interação |
| [`04-metricas.md`](docs/04-metricas.md) | Avaliação de qualidade e métricas |
| [`05-pitch.md`](docs/05-pitch.md) | Roteiro do pitch de apresentação |

---

## 🏆 Entregáveis do Lab

- [x] Documentação do agente (`docs/`)
- [x] Prompts do agente (`docs/03-prompts.md`)
- [x] Protótipo funcional (`src/app.py`)
- [x] Pitch gravado

---

## 👩‍💻 Autora

Desenvolvido por **[kamiikg](https://github.com/kamiikg)** como solução para o lab **"Bia do Futuro"** da [DIO](https://www.dio.me/).

---

## 📄 Licença

Este projeto é baseado no repositório original da [Digital Innovation One](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro) e está disponível para fins educacionais.
