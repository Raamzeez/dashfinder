from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("./index.html")


@app.route('/carplay-vehicles')
def carplayVehicles():
    brands = []  # {name: string, models: string[]}
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
                startYear = vehicle.text[:4]
                endYear = vehicle.text[7:11]
                model_name = vehicle.text[12:]
                model = {"name": model_name,
                         "startYear": startYear, "endYear": endYear}
                car_models.append(model)
            brands.append({"name": company_name, "models": car_models})
    return brands


if __name__ == "__main__":
    app.run(debug=True)
