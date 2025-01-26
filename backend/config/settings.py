import os

# Basic Flask Configurations
DEBUG = True
# replace with your own secret key
SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")
# print(SECRET_KEY)