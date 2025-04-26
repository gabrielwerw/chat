
from flask import Flask, request, session, redirect, url_for, send_from_directory, render_template_string

app = Flask(__name__)
app.secret_key = 'secret_key'

# HTML carregado diretamente
with open('index.html', 'r', encoding='utf-8') as f:
    template_html = f.read()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        user_input = request.form['user_input']
        response = generate_response(user_input)
        session['history'].append({'question': user_input, 'answer': response})

    return render_template_string(template_html, history=session['history'])

def generate_response(user_input):
    user_input = user_input.lower()
    if 'ganhar peso' in user_input:
        return 'Para ganhar peso, aumente a ingestão calórica com alimentos nutritivos.'
    elif 'perder peso' in user_input:
        return 'Para perder peso, reduza calorias e pratique atividades físicas regularmente.'
    elif 'dieta' in user_input:
        return 'Uma dieta equilibrada inclui frutas, vegetais, proteínas magras e grãos integrais.'
    else:
        return 'Desculpe, não entendi. Por favor, pergunte sobre dieta, ganhar ou perder peso.'

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/clear')
def clear():
    session.pop('history', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Acesse o chat em: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=10000)

