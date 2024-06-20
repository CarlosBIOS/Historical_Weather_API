from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('explanation.html')


@app.route('/api/v1/<word>')
def dictionary(word):
    request = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    contenct_dict = request.json()
    try:
        return {'description': contenct_dict[0]['meanings'][0]['definitions'][0]['definition'],
                'word': word}
    except KeyError:
        return {'description': contenct_dict['title']}


if __name__ == '__main__':
    app.run(debug=True)

# Para usar o jupyter, primeiro tenho que instalá-lo(ver o video 272) e dps escolho um directory e abro-o no terminal e
# escrevo jupyter-lab
