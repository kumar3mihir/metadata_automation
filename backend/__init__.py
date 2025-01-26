"""
This module initializes the Flask application.

Functions:
    create_app: Creates and configures an instance of the Flask application.

create_app:
    Returns:
        app (Flask): The configured Flask application instance.
"""
from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('config/settings.py')  # Load configuration

    # Register blueprints or routes
    from .app.routes import main
    app.register_blueprint(main)

    return app
