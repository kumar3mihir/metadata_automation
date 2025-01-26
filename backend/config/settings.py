import os

# Basic Flask Configurations
DEBUG = True
# replace with your own secret key
SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")
# print(SECRET_KEY)


# MongoDB Config
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")

# MySQL Config
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "schema_db")

# SQL Server Config
SQLSERVER_HOST = os.environ.get("SQLSERVER_HOST", "localhost")
SQLSERVER_USER = os.environ.get("SQLSERVER_USER", "sa")
SQLSERVER_PASSWORD = os.environ.get("SQLSERVER_PASSWORD", "password")
SQLSERVER_DATABASE = os.environ.get("SQLSERVER_DATABASE", "schema_db")
