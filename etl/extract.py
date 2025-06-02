import requests
from datetime import datetime

def extract_data():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        date_str = data["Date"][:10]
        date = datetime.strptime(date_str, "%Y-%m-%d").date()

        results = []
        for currency_code, info in data["Valute"].items():
            results.append({
                "date": str(date),
                "currency": currency_code,
                "rate": info["Value"]
            })

        return results

    except requests.RequestException as e:
        print("Ошибка при запросе:", e)
        return []
