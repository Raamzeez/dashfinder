from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("./index.html")


@app.route('/carplay-vehicles')
def carplayVehicles():
    # model = {name: string, startYear: string, endYear: string}
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
                for tag in vehicle.find_all("figure"):
                    tag.decompose()
                startYear = vehicle.text[:4]
                if " - " not in vehicle.text:
                    model_name = vehicle.text[5:].replace('\u2011', '-')
                    endYear = str(datetime.now().year)
                else:
                    endYear = vehicle.text[7:11]
                    model_name = vehicle.text[12:].replace('\u2011', '-')
                model = {"name": model_name,
                         "startYear": startYear, "endYear": endYear}
                car_models.append(model)
            brands.append({"name": company_name, "models": car_models})
    return brands


@app.route('/android-auto-vehicles')
def androidAutoVehicles():
    # model = {name: string, startYear: string, endYear: string}
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
                splitText = vehicle.text.split()
                model_name = splitText[0]
                if (len(splitText) > 1):
                    startYear = splitText[1][:4]
                    model = {"name": model_name,
                             "startYear": startYear, "endYear": str(datetime.now().year)}
                    car_models.append(model)
            brands.append({"name": company_name, "models": car_models})
    return brands


if __name__ == "__main__":
    app.run(debug=True)
