import json
import os

from src.task import Product, Category

def read_file(file_name: str) -> dict:
    full_path = os.path.abspath(file_name)
    with open(full_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def create_object_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
