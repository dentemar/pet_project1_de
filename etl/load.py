# etl/load.py

import sqlite3
from pathlib import Path

DB_PATH = Path("currency_data.db")

def load_data(data):
    if not data:
        print("Нет данных для загрузки.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currency_rates (
            date TEXT,
            currency TEXT,
            rate REAL,
            PRIMARY KEY (date, currency)
        );
    """)

    # Загружаем данные
    for item in data:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO currency_rates (date, currency, rate)
                VALUES (?, ?, ?)
            """, (item["date"], item["currency"], item["rate"]))
        except Exception as e:
            print(f"Ошибка при вставке {item}: {e}")

    conn.commit()
    conn.close()
    print("Загрузка завершена.")
