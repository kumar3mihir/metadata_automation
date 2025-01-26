import mysql.connector

def extract_mysql_schema(host, user, password, database):
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    schema = {}
    for (table,) in tables:
        cursor.execute(f"DESCRIBE {table}")
        schema[table] = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()
    return schema
