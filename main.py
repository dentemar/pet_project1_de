from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

if __name__ == "__main__":
    raw = extract_data()
    cleaned = transform_data(raw, filter_currencies=["USD", "EUR", "CNY"])
    load_data(cleaned)
