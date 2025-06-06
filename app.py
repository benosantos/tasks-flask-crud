from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello word!'

@app.route('/teste')
def teste():
    return 'Teste!'

@app.route('/teste01')
def teste01():
    return 'Teste01'


app.run(debug=True)