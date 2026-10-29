import json
import logging

def load_data_from_file(filename: str = "input_data.json") -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Файл {filename} не знайдено!")
        raise
    except json.JSONDecodeError:
        logging.error(f"Помилка зчитування JSON з файлу {filename}!")
        raise
