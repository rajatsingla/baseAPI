DEBUG = True
DEFAULT_LANGUAGE = "en"

URL_PREFIX = "/api/"

SERVER_BASE_URL = "http://localhost:5000"
MIN_PASSWORD_LENGTH = 5
SALT = "default salt"

# PostgreSQL
DB_NAME = "wclub"
DB_USER = "dev"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_MAXCONNECTIONS = 32
DB_TRANSACTIONS_ENABLED = True

class API_LOGGER:
    ENABLED = False