from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

USER_DB=os.environ.get('USER_DB')
PASS_DB=os.environ.get('PASS_DB')
URL_DB=os.environ.get('URL_DB')
NAME_DB=os.environ.get('NAME_DB')


FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:5433/{NAME_DB}'