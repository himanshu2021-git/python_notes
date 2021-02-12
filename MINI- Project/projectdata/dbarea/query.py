create_table = """
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY,
    product_name VARCHAR(30) NOT NULL,
    price REAL NOT NULL,
    in_stock INTEGER DEFAULT 0,
    barcode_no INTEGER,
    barcode TEXT
)
"""

insert_data = """
INSERT INTO {table_name}(
    id,
    product_name,
    price,
    in_stock,
    barcode_no,
    barcode
)values(
    {id},
    '{product_name}',
    {price},
    {in_stock},
    {barcode_no},
    '{barcode}'
)
"""

read_data = """
SELECT * FROM {table_name} WHERE id = {product_id}
"""