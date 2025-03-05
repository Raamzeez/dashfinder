import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

from lib import filtermodel


def fetch_android_auto_vehicles():
    data = []
    page = requests.get(
        "https://www.android.com/auto/compatibility/")
    soup = BeautifulSoup(page.content, "html.parser")
    sections = soup.find_all("section", class_="accordion-list--primary")
    for section in sections:
        image_url = section.find("img").get("srcset")[:-5]
        company_name = section.find("span")
        if (company_name):
            company_name = company_name.text
            vehicles = section.find_all("li")
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
                year_pattern = r'\s+\d{4}'
                if not re.search(year_pattern, vehicle_text):
                    startYear = None
                else:
                    startYear = int(startYear)
                model = {"image": image_url,
                         "brand": company_name,
                         "model": filtermodel.filter_model(model_name, company_name),
                         "startYear": startYear,
                         "endYear": datetime.now().year,
                         "wireless": wireless_compatibility}
                data.append(model)
    return data
