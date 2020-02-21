from flask import Flask, redirect, render_template, url_for
from random import sample
from flask_wtf import FlaskForm
from wtforms import IntegerField
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
bootstrap = Bootstrap(app)


@app.route('/', methods=('GET', 'POST'))
def index():
    form = Num_Jogos()
    if form.validate_on_submit():
        num = numeros_mega(form.name.data)
        return render_template("index.html", form=form, num = num)
    return render_template("index.html", form=form)



def numeros_mega(num_jogos):
    '''
    Gerador de jogos da Mega Sena
    Parâmetro: Número de jogos
    '''

    jogos = []

    for each in range(num_jogos):
        temp = list(sample(range(1,61),6))
        temp.sort()
        jogos.append(temp)

    return jogos


class Num_Jogos(FlaskForm):
    name = IntegerField('Jogos')


if __name__ == '__main__':
    app.run()
