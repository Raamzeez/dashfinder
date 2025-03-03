import re

def get_car_image_url(css_text: str, car_class: str) -> str:
    pattern = re.compile(rf'\.{car_class}\s*{{[^}}]*background-image:\s*url\((.*?)\)', re.DOTALL)
    match = pattern.search(css_text)

    if match:
        image_url = match.group(1).strip().strip('"').strip("'")
        if image_url.startswith('/'):
            base_url = "https://www.apple.com"
            image_url = base_url + image_url
        return image_url

    return ""