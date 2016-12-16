from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/temperature', methods=['POST'])
def temperature():
    #return render_template('temperature.html')
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+ zipcode + ',us&appid=26c66420874168632298abeff098ec15')
    #http: // api.openweathermap.org / data / 2.5 / weather?zip = 94040, us & appid = b1b15e88fa797225412429c1c50c122a1
    json_object = r.json()
    #return r
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html', temp=temp_f)

    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
