import click
from time import time

from app.src.db_session import DBInit
from app.src.wrapper import ContainerCoroutine


def init_db():
    db = DBInit()
    ContainerCoroutine(args=db())


@click.command('init-db')
def init_db_command():
    init = time()

    init_db()
    end = time()
    click.echo('Initialize DataBase -- Time Command finish: %s' % (end - init))


def init_app(app):
    app.cli.add_command(init_db_command)
