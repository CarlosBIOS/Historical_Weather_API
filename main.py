from flask import Flask, render_template
import pandas as pd
import numpy

app = Flask(__name__)  # É como fazem os profissionais, colocam __name__ em vez de 'word'
stations = pd.read_csv('data_small/stations.txt', skiprows=17)[:183][['STAID',
                                                                      'STANAME                                 ']]
# Vou criar uma varoável chamada stations que servirá para mostrar uma tabela sobre todos os stations disponiveis. Para
# isso, vou ter que usar o read_csv e dps to_html e coloquei só até 101, devido ao data_small. No ficheiro home.html,
# tenho que acescentar este código:
# <p>{{data|safe}}</p>, onde safe cria uma tabela formatada!!!


@app.route('/')
def home():
    return render_template('home.html', data=stations.to_html())


@app.route('/api/v1/<station>/<date>')
def station_date(station, date):
    data_frame = pd.read_csv('data_small/TG_STAID' + str(station).zfill(6) + '.txt', skiprows=20,
                             parse_dates=['    DATE'])
    temperature = data_frame.loc[data_frame['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        'station': stations.loc[stations['STAID'] == int(station)]['STANAME                                 ']
        .squeeze().strip(),
        'date': f'{date[len(date)-2:]}-{date[4:6]}-{date[:4]}',
        'temperature': temperature}


@app.route('/api/v1/<station_number>')
def all_data(station_number):
    data_frame = pd.read_csv('data_small/TG_STAID' + str(station_number).zfill(6) + '.txt', skiprows=20,
                             parse_dates=['    DATE'])[['    DATE', '   TG']]
    data_frame['   TG'] = data_frame['   TG'].mask(data_frame['   TG'] == -9999, numpy.nan) / 10
    number = (stations.loc[stations['STAID'] == int(station_number)]['STANAME                                 '].squeeze()
              .strip())
    return render_template('station.html', station=data_frame.to_html(),
                           text=f'Here is the information about the station {station_number}: {number}')


@app.route('/api/v1/<station_number>/<year>')
def yearly(station_number, year):
    data_frame = pd.read_csv('data_small/TG_STAID' + str(station_number).zfill(6) + '.txt', skiprows=20,
                             parse_dates=['    DATE'])[['    DATE', '   TG']].to_html()
    return render_template('station.html', station=data_frame, text=f'Here is the information about the station '
                                                                    f'{station_number}')


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
