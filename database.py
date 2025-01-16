from peewee import *

db = SqliteDatabase('usuarios.db')

class Usuarios(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    funcao = CharField()

    class Meta:
        database = db