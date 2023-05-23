from zipfile import ZipFile
from typing import Any
import json


def open_file_in_zip(file_zip: Any) -> list[dict]:
    """
    Функция открывать zip файл, находит json и загружает из объекты
    :param file_zip: зип файл где хранится файл с операцями
    :return: список, состоящий из операций из файла json
    """
    with ZipFile(file_zip, "r") as myzip:
        for item in myzip.infolist():
            if item.filename.endswith(".json"):
                with myzip.open(item.filename, "r") as f:
                    return json.load(f)


def date_reversed(date: str) -> str:
    """Функция инвертирует строку даты из формата «ГГГГ-ММ-ДД» в «ДД.ММ.ГГГГ»."""
    return ".".join(date.split("T")[0].split("-")[::-1])
