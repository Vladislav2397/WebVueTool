from peewee import (
    SqliteDatabase,
    Model, CharField, BooleanField, ForeignKeyField
)
from src.config import DB_NAME

DB = SqliteDatabase(DB_NAME)


class File(Model):

    name = CharField()
    suffix = CharField(null=True)
    extension = CharField()
    path = CharField(null=True)

    class Meta:
        database = DB


class Component(Model):
    name = CharField()
    path = CharField()
    class_name = CharField(unique=True)
    vue_file = ForeignKeyField(
        File, verbose_name='Vue file'
    )
    scss_critical_file = ForeignKeyField(
        File, verbose_name='Scss critical file'
    )
    scss_main_file = ForeignKeyField(
        File, verbose_name='Scss main file'
    )
    is_style = BooleanField()

    class Meta:
        database = DB


def create_tables():
    with DB:
        DB.create_tables([File, Component])
