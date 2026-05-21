from flask import Flask
from config import config


def create_app(config_name="default"):
    selected_config = config[config_name]
    if hasattr(selected_config, "validate"):
        selected_config.validate()

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(selected_config)

    from app.routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        response.headers.setdefault(
            "Referrer-Policy", "strict-origin-when-cross-origin"
        )
        return response

    return app
