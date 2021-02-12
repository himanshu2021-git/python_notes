from inventory.summary import productsummary

def sell():
    print("SALES SCREEN".center(50,"*"))
    product_id = int(input('PRODUCT ID : '))
    result = productsummary(flag=True, product_id  = product_id)
    print(result)

