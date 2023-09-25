from flask import Flask, render_template, request
from periodic import periodic

app = Flask(__name__)

# Rota da página inicial (home)
@app.route('/')
def index():
    return render_template('index.html')

# Rota da página de processamento do form
@app.route('/processar_formulario', methods=['POST'])
def processar_formulario():
    numeroAtomico = int(request.form['numeroAtomico'])
    
    # Manipule os dados aqui (por exemplo, concatenando nome e email)
    resultado = periodic(numeroAtomico)
    
    # Redirecione de volta para a página 1 ou qualquer outra página que você desejar
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
