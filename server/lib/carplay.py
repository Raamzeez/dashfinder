import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

from lib import carimage


def fetch_carplay_vehicles():
    #{image: string, brand: string, model: string, carKeyCompatible: bool, startYear: string, endYear: string}[]
    css_url = "https://www.apple.com/v/ios/carplay/m/built/styles/available-models.built.css"
    css_data = requests.get(css_url).text
    data = []
    page = requests.get(
        "https://www.apple.com/ios/carplay/available-models/")
    soup = BeautifulSoup(page.content, "html.parser")
    companies = soup.find_all("div", class_="row")
    for company in companies:
        image_classes_array = company.find("figure").get("class")
        if (len(image_classes_array) > 1):
            image_class = image_classes_array[1]
        image_url = carimage.get_car_image_url(css_data, image_class)
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
                model = {"image": image_url, "brand": company_name, "model": model_name,
                         "startYear": startYear, "endYear": endYear,
                         "supportsCarKey": supports_car_key}
                data.append(model)
    return data