import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-change-me"
    DEBUG = False
    TESTING = False
    MAX_CONTENT_LENGTH = int(os.environ.get("MAX_CONTENT_LENGTH", 8 * 1024 * 1024))
    ALLOWED_UPLOAD_EXTENSIONS = {
        "csv",
        "doc",
        "docx",
        "jpeg",
        "jpg",
        "pdf",
        "png",
        "txt",
        "xls",
        "xlsx",
        "zip",
    }


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "testing-secret"


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    @classmethod
    def validate(cls):
        if not cls.SECRET_KEY:
            raise RuntimeError("SECRET_KEY must be set when FLASK_CONFIG=production")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
