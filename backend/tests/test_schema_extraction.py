from data_processing.schema_extraction.mongodb import extract_mongodb_schema
from data_processing.schema_extraction.mysql import extract_mysql_schema
from data_processing.schema_extraction.sqlserver import extract_sqlserver_schema

def test_mongodb():
    uri = "mongodb://localhost:27017"
    print(extract_mongodb_schema(uri))

def test_mysql():
    print(extract_mysql_schema("localhost", "root", "password", "schema_db"))

def test_sqlserver():
    print(extract_sqlserver_schema("localhost", "sa", "password", "schema_db"))

if __name__ == "__main__":
    # Uncomment the function you want to test
    test_mongodb()
    # test_mysql()
    # test_sqlserver()
