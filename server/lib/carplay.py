import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

from lib import carimage


def fetch_carplay_vehicles():
    # {image: string, brand: string, model: string, carKeyCompatible: bool, startYear: string, endYear: string}[]
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
                split_text = vehicle_text.split(" ")
                startYear = int(float(split_text[0]))
                i = 3
                if split_text[1] != "-":
                    i = 1
                    endYear = datetime.now().year
                else:
                    endYear = int(split_text[2])
                model_name = ""
                while i < len(split_text):
                    model_name += split_text[i]
                    if (i < len(split_text) - 1):
                        model_name += " "
                    i += 1
                model = {"image": image_url, "brand": company_name, "model": model_name,
                         "startYear": startYear, "endYear": endYear,
                         "supportsCarKey": supports_car_key}
                data.append(model)
    return data
