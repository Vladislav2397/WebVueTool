from peewee import SqliteDatabase
from src.config import DB_NAME
from .models import File, Component

DB = SqliteDatabase(DB_NAME)
DB.create_tables([File, Component])
