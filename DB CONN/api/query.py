create_table = """
CREATE TABLE IF NOT EXISTS PythonBricks(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    email VARCHAR(50),
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
"""

insert_data = """
INSERT INTO PythonBricks(
    firstname,
    lastname,
    email
)VALUES(
    '{}',
    '{}',
    '{}'
)
"""

read_data = "SELECT * FROM PythonBricks"