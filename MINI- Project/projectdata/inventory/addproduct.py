"""
this module contains the code regarding adding the product.

"""
#DB DEPS

from pickle import  dump,load
#BARCODE DEPS
from .generatebarcode import generate
from config import db

try:
    product_id = load(open("temp","rb"))
except:
    product_id = 1000000000000001


def add():
    global product_id
    product_id += 1
    print("ADD PRODUCT".center(50,"*"))
    product_name = input('PRODUCT NAME : ')
    price = float(input('PRICE PER UNIT : '))
    quantity = int(input('QUANTITY : '))
    barcode_location = generate(product_id)

    db.insertData(
        id=product_id,
        product_name=product_name,
        price = price,
        in_stock = quantity,
        barcode_no = product_id,
        barcode = barcode_location
    )
    try:
        dump(product_id,open("temp","wb"))
    except:
        pass
    # print(barcode_location)
    # db.insertData()