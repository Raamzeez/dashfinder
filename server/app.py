from flask import Flask, render_template

from lib import carplay
from lib import androidauto

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("./index.html")

@app.route('/carplay-vehicles')
def carplayVehicles():
    return carplay.fetch_carplay_vehicles()

@app.route('/android-auto-vehicles')
def androidAutoVehicles():
   return androidauto.fetch_android_auto_vehicles()

@app.route('/')
def vehicles():
    data = []
    # carplay_cars = carplay.fetch_carplay_vehicles()
    # android_auto_cars = androidauto.fetch_android_auto_vehicles()
    # for i in range(len(carplay_cars)):
    #     carplay_car_company = carplay_cars[i].name
    #     android_auto_car = None
    #     for j in range(len(android_auto_cars)):
    #         android_auto_car_company = android_auto_cars[j].name
    return data


    
if __name__ == "__main__":
    app.run(debug=True)
