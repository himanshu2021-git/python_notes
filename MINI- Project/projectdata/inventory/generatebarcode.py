import barcode
import os

def generate(product_id):
    barcode_class = barcode.get_barcode_class("code39")
    product_barcode = barcode_class(str(product_id))
    filename = os.path.join(
        os.getcwd(),
        "storagearea",
        "barcodes",
        str(product_id)+".svg"
    )
    product_barcode.save(filename)
    return filename
