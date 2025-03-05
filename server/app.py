from flask import Flask, json, render_template, Response

from lib import carplay
from lib import androidauto

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("./index.html")


@app.route('/carplay-vehicles')
def carplayVehicles():
    return Response(json.dumps(carplay.fetch_carplay_vehicles(),
                               ensure_ascii=False),
                    mimetype='application/json')


@app.route('/android-auto-vehicles')
def androidAutoVehicles():
    return Response(json.dumps(androidauto.fetch_android_auto_vehicles(),
                               ensure_ascii=False),
                    mimetype='application/json')


@app.route('/all-vehicles')
def vehicles():
    data = []
    carplay_cars = carplay.fetch_carplay_vehicles()
    android_auto_cars = androidauto.fetch_android_auto_vehicles()
    data = [carplay_cars, android_auto_cars]
    return Response(json.dumps(data,
                               ensure_ascii=False),
                    mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
