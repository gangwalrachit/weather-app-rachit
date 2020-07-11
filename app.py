import requests
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

def main_work(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8b54ca27c904f6956c146c69f66a232c'
    r = requests.get(url.format(city)).json()
    print(r)

    if(r['cod'] == 200):
        cel = (r['main']['temp'] - 32) * 5 / 9
        cel = round(cel, 2)

        weather = {
            'city': r['name'],
            'count': r['sys']['country'],
            'temp': cel,
            'desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'press': r['main']['pressure'],
            'humid': r['main']['humidity'],
            'wind': r['wind']['speed'],
            'cod': r['cod']
        }
    
    else:
        weather = {
            'cod': r['cod']
        }

    return weather


@app.route('/find', methods=["GET", "POST"])
def find():
    city = request.args.get('city')
    return jsonify(main_work(city))

@app.route('/', methods=["GET", "POST"])
def index():
    city = 'Mumbai'
    return render_template('index.html', wthr = main_work(city))


if __name__ == '__main__':
    app.run(debug=True)