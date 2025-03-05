import requests


def get_coordinates(address):
    api_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": "ваш_api_key",
        "format": "json",
        "geocode": address
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()
    pos = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = map(float, pos.split())
    return lon, lat


def get_district_by_coordinates(coords):
    api_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": "ваш_api_key",
        "format": "json",
        "geocode": f"{coords[0]},{coords[1]}",
        "kind": "district"
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()

    try:
        district_name = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]
        return district_name
    except IndexError:
        return "Район не найден"
