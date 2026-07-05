import requests

BASE_URL = "https://identity-forge.adi7ya.workers.dev"


def get_countries():
    try:
        res = requests.get(f"{BASE_URL}/countries", timeout=10)
        return res.json()
    except Exception as e:
        return {"success": False, "error": str(e)}


def generate_identity(country):
    try:
        res = requests.get(
            f"{BASE_URL}/generate?country={country}",
            timeout=10
        )
        return res.json()
    except Exception as e:
        return {"success": False, "error": str(e)}
