import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_android_auto_vehicles():
    # model = {name: string,
        # startYear: string,
        # endYear: string,
        # wirelessCompatibility: bool
    #}

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