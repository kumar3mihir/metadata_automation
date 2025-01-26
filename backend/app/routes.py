
from flask import Blueprint
"""
This module defines the routes for the Flask application.

Blueprints:
    main (Blueprint): A Flask Blueprint for the main routes.

Routes:
    / (GET): Returns a welcome message for the Schema Extraction API.
"""

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Schema Extraction API!"
