from .db import DB
from peewee import (
    Model, CharField, BooleanField
)


class File(Model):
    name = CharField()
    suffix = CharField(null=True)
    extension = CharField()

    class Meta:
        database = DB


class Component(Model):
    name = CharField()
    path = CharField()
    class_name = CharField(unique=True)
    is_style = BooleanField()

    class Meta:
        database = DB
