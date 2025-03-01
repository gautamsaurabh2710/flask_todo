import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy

# Database connection details
DB_USERNAME = "root"
DB_PASSWORD = "Saurabh@2710"
DB_HOST = "localhost"
DB_NAME = "todo_db"

# Database URI
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Saurabh%402710@localhost/todo_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
