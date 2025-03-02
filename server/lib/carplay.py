import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_carplay_vehicles():
    #{brand: string, model: string, carKeyCompatible: bool, startYear: string, endYear: string}[]
    data = []
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
                model = {"brand": company_name, "name": model_name,
                         "startYear": startYear, "endYear": endYear,
                         "supportsCarKey": supports_car_key}
                data.append(model)
    return data