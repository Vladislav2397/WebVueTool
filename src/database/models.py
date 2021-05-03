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
    class_name = CharField(null=True)
    vue_file = ForeignKeyField(
        File, verbose_name='Vue file'
    )
    scss_critical_file = ForeignKeyField(
        File, verbose_name='Scss critical file', null=True
    )
    scss_main_file = ForeignKeyField(
        File, verbose_name='Scss main file', null=True
    )
    is_style = BooleanField(null=True)

    class Meta:
        database = DB


def create_tables():
    with DB:
        DB.create_tables([File, Component])
