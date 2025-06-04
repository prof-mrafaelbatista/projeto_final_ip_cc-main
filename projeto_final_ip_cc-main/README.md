Projeto Final de Introdução à Programação e Computação Científica
Este repositório contém o código-fonte e os recursos do projeto final da disciplina de Introdução à Programação e Computação Científica. O objetivo principal deste projeto é , demonstrando a aplicação de conceitos de programação e a integração com serviços externos, especificamente a API do Gemini.

Tecnologias Utilizadas
Este projeto foi desenvolvido utilizando as seguintes tecnologias:

Linguagem de Programação:

Python 3.x: A linguagem principal para o desenvolvimento do backend e a lógica da aplicação.
Framework Web:

Flask: Um microframework web leve para Python, utilizado para construir a aplicação web, gerenciar rotas, requisições e respostas.
Bibliotecas Python:

google-generativeai: Biblioteca oficial do Google para interagir com a API do Gemini.
python-dotenv: Utilizada para carregar variáveis de ambiente a partir de um arquivo .env, garantindo a segurança de chaves de API.
requests (se usado diretamente): Para fazer requisições HTTP (se você não usar apenas a biblioteca google-generativeai para interações com a API).
jinja2 (integrada ao Flask): Para renderização de templates HTML dinâmicos no frontend.
Tecnologias Frontend:

HTML5: Para a estrutura e conteúdo das páginas web.
CSS3: Para estilização e design das interfaces do usuário.
JavaScript (se aplicável): Para interações dinâmicas no lado do cliente (validação de formulários, chamadas AJAX, etc.).
Estrutura do Site e Conteúdo
A aplicação Flask segue uma estrutura típica, com as seguintes seções e seus conteúdos:

Página Principal (/ ou /index):

Conteúdo: A página inicial da aplicação. Geralmente contém um formulário de entrada onde o usuário pode digitar sua consulta, um botão de envio, e uma área onde as respostas da API do Gemini serão exibidas. Pode incluir uma breve descrição do projeto.
Arquivos Relacionados: app.py (rota principal), templates/index.html (template HTML).
Endpoint da API (/processar_consulta ou similar):

Conteúdo: Este não é uma página visível, mas sim um endpoint do backend que recebe as consultas do usuário via POST. Ele processa a requisição, interage com a API do Gemini e retorna a resposta para o frontend.
Arquivos Relacionados: app.py (função de rota para processamento).
Páginas de Erro (Opcional, e.g., /erro ou /404):

Conteúdo: Páginas para exibir mensagens de erro, como API key inválida, problemas de conexão, ou requisições malformadas.
Arquivos Relacionados: app.py (manipuladores de erro), templates/error.html.
A estrutura de pastas do projeto é organizada da seguinte forma:

projeto_final_ip_cc/
├── app.py                  # Arquivo principal da aplicação Flask
├── .env.example            # Exemplo do arquivo .env para variáveis de ambiente
├── requirements.txt        # Lista de dependências Python
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/
│   │   └── style.css       # Folha de estilo CSS
│   └── js/
│       └── script.js       # Scripts JavaScript (se houver)
├── templates/              # Templates HTML renderizados pelo Flask
│   ├── index.html          # Página principal da aplicação
│   └── layout.html         # (Opcional) Template base para herança
├── .gitignore              # Arquivo para ignorar arquivos e pastas no Git
└── README.md               # Este arquivo README
Integração com a API do Gemini
A integração com a API do Gemini é um dos pilares deste projeto. Veja como ela foi implementada:

Obtenção da Chave de API:

A chave de API do Google Gemini é armazenada de forma segura em um arquivo .env (não versionado) e carregada pela aplicação utilizando a biblioteca python-dotenv. Isso evita que a chave seja exposta no código-fonte ou no repositório público.
Inicialização do Modelo Gemini:

A biblioteca google-generativeai é utilizada para configurar e inicializar o modelo. O código tipicamente faz:
Python

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do .env
API_KEY = os.getenv("GOOGLE_API_KEY") # Ou o nome da sua variável
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro') # Ou o modelo que você está usando
Envio de Requisições:

Quando o usuário envia uma consulta através do formulário na página web, o backend da aplicação Flask recebe essa consulta.
Essa consulta é então passada para o método generate_content() do modelo Gemini.
Python

response = model.generate_content(user_query)
Processamento da Resposta:

A resposta da API do Gemini (que pode ser um objeto complexo) é processada para extrair o texto gerado.
Esse texto é então enviado de volta para o frontend, onde é exibido ao usuário.
Python

generated_text = response.text
Essa arquitetura garante que a lógica de interação com a IA esteja no backend, mantendo a chave de API segura e permitindo que o frontend se concentre na apresentação.

Como Executar a Aplicação Localmente
Para configurar e rodar a aplicação Flask em sua máquina local, siga os passos abaixo:

Pré-requisitos
Certifique-se de ter instalado:

Python 3.x (versão 3.8 ou superior é recomendada).
pip (gerenciador de pacotes do Python).
Configuração da Chave de API do Gemini
Obtenha sua Chave de API: Acesse o Google AI Studio e crie uma chave de API para o Gemini.
Crie o arquivo .env: Na raiz do diretório do projeto (projeto_final_ip_cc/), crie um arquivo chamado .env.
Adicione sua chave: Dentro do arquivo .env, adicione a seguinte linha, substituindo SUA_CHAVE_AQUI pela sua chave de API real:
Snippet de código

GOOGLE_API_KEY=SUA_CHAVE_AQUI
Instalação e Execução
Clone o repositório:
Bash

git clone https://github.com/guilhermlcn/projeto_final_ip_cc.git
Navegue até o diretório do projeto:
Bash

cd projeto_final_ip_cc
Crie um ambiente virtual (opcional, mas recomendado):
Bash

python -m venv venv
Ative o ambiente virtual:
No Windows: .\venv\Scripts\activate
No macOS/Linux: source venv/bin/activate
Instale as dependências:
Bash

pip install -r requirements.txt
Se você não tem o arquivo requirements.txt, você pode criá-lo com as bibliotecas listadas em Tecnologias Utilizadas (e.g., Flask, google-generativeai, python-dotenv).
Defina a variável de ambiente FLASK_APP:
Bash

export FLASK_APP=app.py  # No macOS/Linux
set FLASK_APP=app.py     # No Windows
Execute a aplicação Flask:
Bash

flask run
Acesse a aplicação: Abra seu navegador e navegue para http://127.0.0.1:5000/.
Principais Partes do Código Python
Aqui está uma breve descrição das principais partes do código Python, localizadas no arquivo app.py (ou onde quer que você tenha organizado sua lógica):

Inicialização da Aplicação Flask:

from flask import Flask, render_template, request
app = Flask(__name__)
Define a aplicação Flask e importa os módulos necessários para renderizar templates e lidar com requisições.
Configuração do Gemini API:

As linhas que carregam a chave de API do .env e configuram o google.generativeai. Isso geralmente é feito no início do app.py para que o modelo esteja pronto para uso.
Rotas (@app.route(...)):

Rota principal (/):
Python

@app.route('/')
def index():
    return render_template('index.html')
Esta função é responsável por carregar e exibir a página inicial da aplicação (index.html).
Rota de processamento (/processar_consulta ou similar):
Python

@app.route('/processar_consulta', methods=['POST'])
def processar_consulta():
    user_query = request.form['query'] # Ou request.json se for AJAX
    # Lógica para chamar a API do Gemini e processar a resposta
    # ...
    return render_template('index.html', response=generated_text) # Ou jsonify
Esta rota é acessada quando o usuário envia uma consulta. Ela recebe a entrada do usuário, interage com a API do Gemini e retorna a resposta.
Funções de Interação com Gemini (se separadas):
