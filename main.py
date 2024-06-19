from flask import Flask, render_template
import pandas

app = Flask(__name__)  # É como fazem os profissionais, colocam __name__ em vez de 'word'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def station_date(station, date):
    temperature = 23
    return {'station': station,
            'date': date,
            'temperature': temperature}


@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact_us/')
def contact_us():
    return render_template('contact_us.html')


@app.route('/store/')
def store():
    return render_template('store.html')


if __name__ == '__main__':
    app.run(debug=True)  # debug=True, serve para ver erros, se tiver
    # app.run(debug=True, port=5001)
    # Como esccrevi /home, tenho que usar o URL que me deram e acrescentar /home
