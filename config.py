class Config:
    # Database configuration (replace with your actual database URI)
    SQLALCHEMY_DATABASE_URI = "sqlite:///music_library.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management (replace with a secure secret key)
    SECRET_KEY = "pa$$wd4ML"

    # Other application-specific configurations can be added here
    # For example:
    DEBUG = True
    # TESTING = False
    # MAIL_SERVER = 'smtp.example.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # ...


# Define additional configuration classes for different environments
class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific configurations here


# Create a dictionary to map configuration names to their respective classes
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    # Add more configurations as needed
}


# Define a function to get the configuration class based on the environment name
def get_config(environment_name):
    return config_by_name.get(environment_name, DevelopmentConfig)
