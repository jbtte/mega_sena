from flask import Flask, render_template, jsonify, request
from random import sample

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gerar')
def gerar():
    # run random number generator function
    num_jogos = request.args.get("num_jogos")
    jogos = numeros_mega(int(num_jogos))
    return jsonify({"jogos":jogos})

# Random number generator function
def numeros_mega(num_jogos):
    '''
    Gerador de jogos da Mega Sena
    Parâmetro: Número de jogos
    '''

    jogos = []
    for each in range(num_jogos):
        temp = list(sample(range(1,61),6))
        temp.sort()
        dezenas = ""
        for num in temp:
            dezenas = dezenas + str(num) + " - "
        jogos.append(dezenas[:-3])
    return jogos


if __name__ == '__main__':
    app.run()
