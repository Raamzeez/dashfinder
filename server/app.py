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


if __name__ == "__main__":
    app.run(debug=True)
