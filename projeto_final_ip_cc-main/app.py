from flask import Flask, render_template, request, url_for, redirect, session
import csv
import os
import requests

app = Flask(__name__)
app.secret_key = 'chave_secreta_do_app'  # Necessário para usar sessões

@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/sobre_equipe')
def alo():
    return render_template('sobre_equipe.html')

@app.route('/glossario')
def glossario():
    glossario_de_termos = []

    with open ('bd_glossario.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for t in reader:
            glossario_de_termos.append(t)

    return render_template('glossario.html', glossario=glossario_de_termos)

@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

@app.route('/deletar_termo')
def deletar_termo():
    return render_template('deletar_termo.html')

@app.route('/delet_termo', methods=['POST'])
def delet_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']
    linhas = []
    with open('bd_glossario.csv', mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for linha in reader:
            if linha != [termo, definicao]:
                linhas.append(linha)

    with open('bd_glossario.csv', mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(linhas)

    return redirect(url_for('glossario'))

@app.route('/editar_termo')
def editar_termo():
    return render_template('editar_termo.html')

@app.route('/edit_termo', methods=['POST'])
def edit_termo():
    termo = request.form['termo']
    novo_termo = request.form['novo_termo']
    nova_definicao = request.form['nova_definicao']
    linhas = []
    with open('bd_glossario.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for linha in reader:
            if linha[0] == termo:
                linha[0] = novo_termo
                linha[1] = nova_definicao
            linhas.append(linha)

    with open('bd_glossario.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(linhas)

    return redirect('glossario')


@app.route('/chat_bot')
def chat_form():
    # Inicializa o histórico se não existir
    if 'historico_chat' not in session:
        session['historico_chat'] = []
    
    resposta_bot = session.get('resposta_bot', None)
    historico_chat = session.get('historico_chat', [])
    
    return render_template('chat_bot.html', 
                         resposta=resposta_bot, 
                         historico_chat=historico_chat)


def consulta_chatbot(prompt):
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAC4Bn0hkU6aQV0iS5GEf-gLnn49uIIfao"
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "Desculpe, ocorreu um erro ao processar sua solicitação."
            
    except Exception as e:
        return "Desculpe, ocorreu um erro inesperado."

@app.route('/chat_bot_form', methods=['POST'])
def chat_bot_form():
    try:
        prompt = request.form['prompt']
        resposta = consulta_chatbot(prompt)
        
        # Atualiza o histórico do chat
        historico_chat = session.get('historico_chat', [])
        historico_chat.append({
            'prompt': prompt,
            'resposta': resposta
        })
        
        # Atualiza a sessão
        session['historico_chat'] = historico_chat
        session['resposta_bot'] = resposta
        
        return redirect(url_for('chat_form'))
        
    except Exception as e:
        return redirect(url_for('chat_form'))

if __name__ == '__main__':
    app.run(debug=True)



