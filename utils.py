from zipfile import ZipFile
import json


def open_file_in_zip(file_zip):
    with ZipFile(file_zip, "r") as myzip:
        for item in myzip.infolist():
            if item.filename.endswith(".json"):
                with myzip.open(item.filename, "r") as f:
                    return json.load(f)


def date_reversed(date):
    return ".".join(date.split("T")[0].split("-")[::-1])
