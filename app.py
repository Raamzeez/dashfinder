from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
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
                print(vehicle.text)
                car_models.append(vehicle.text)
            brands.append({"name": company_name, "models": car_models})
    print(brands)
    return brands
