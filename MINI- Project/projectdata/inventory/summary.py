from config import db
def productsummary(flag=False,product_id = None):
    if flag:
        return db.readData(product_id = product_id)
    else:
        pass

    
