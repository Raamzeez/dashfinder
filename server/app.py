import requests
import re
from flask import Flask, render_template
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("./index.html")


@app.route('/carplay-vehicles')
def carplayVehicles():
    # model = {name: string, carKeyCompatible: bool, startYear: string, endYear: string}
    # {name: string, models: model[]}
    brands = []
    page = requests.get(
        "https://www.apple.com/ios/carplay/available-models/")
    soup = BeautifulSoup(page.content, "html.parser")
    companies = soup.find_all("div", class_="row")
    for company in companies:
        company_name = company.find(
            "span", class_="image-logo-text")
        if (company_name):
            company_name = company_name.text
            vehicles = company.find_all("li")
            car_models = []
            for vehicle in vehicles:
                supports_car_key = False
                if vehicle.find('figure'):
                    supports_car_key = True
                vehicle_text = vehicle.text.strip()
                vehicle_text = re.sub(
                    r'\\u[0-9a-fA-F]{4}',
                    '',
                    vehicle_text.encode('unicode_escape').decode())
                startYear = vehicle_text[:4]
                if " - " not in vehicle_text:
                    model_name = vehicle_text[5:]
                    endYear = str(datetime.now().year)
                else:
                    endYear = vehicle_text[7:11]
                    model_name = vehicle_text[12:]
                model = {"name": model_name,
                         "startYear": startYear, "endYear": endYear,
                         "supportsCarKey": supports_car_key}
                car_models.append(model)
            brands.append({"name": company_name, "models": car_models})
    return brands


@app.route('/android-auto-vehicles')
def androidAutoVehicles():
    # model = {name: string,
    # startYear: string,
    # endYear: string,
    # wirelessCompatibility: bool}

    # {name: string, models: model[]}
    brands = []
    page = requests.get(
        "https://www.android.com/auto/compatibility/")
    soup = BeautifulSoup(page.content, "html.parser")
    sections = soup.find_all("section", class_="accordion-list--primary")
    for section in sections:
        company_name = section.find("span")
        if (company_name):
            company_name = company_name.text
            vehicles = section.find_all("li")
            car_models = []
            for vehicle in vehicles:
                wireless_compatibility = False
                vehicle_text = vehicle.text.strip()
                if (vehicle_text[-1] == "*"):
                    model_name = vehicle_text[:-8]
                    startYear = vehicle_text[-7:-3]
                    wireless_compatibility = True
                else:
                    model_name = vehicle_text[:-6]
                    startYear = vehicle_text[-5:-1]
                model = {"name": model_name,
                         "startYear": startYear,
                         "endYear": str(datetime.now().year),
                         "wireless": wireless_compatibility}
                car_models.append(model)
            brands.append({"name": company_name,
                           "models": car_models})
    return brands


if __name__ == "__main__":
    app.run(debug=True)
