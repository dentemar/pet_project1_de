# etl/transform.py

def transform_data(raw_data, filter_currencies=None):
    """
    Преобразует и фильтрует данные.
    :param raw_data: список словарей вида {'date': ..., 'currency': ..., 'rate': ...}
    :param filter_currencies: список кодов валют (например, ['USD', 'EUR'])
    :return: очищенный и отфильтрованный список
    """
    transformed = []

    for item in raw_data:
        try:
            currency = item["currency"]
            rate = float(item["rate"])
            date = item["date"]

            if filter_currencies and currency not in filter_currencies:
                continue

            transformed.append({
                "date": date,
                "currency": currency,
                "rate": rate
            })

        except (KeyError, ValueError, TypeError):
            continue

    return transformed
