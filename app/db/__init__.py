import click

from app.api.utils.db_session import create_tables
from app.api.utils.wrapper import coroutine


def init_db():
    coroutine(args=create_tables())


@click.command('init-db')
def init_db_command():

    init_db()

    click.echo('Initialize DataBase')


def init_app(app):
    with app.app_context():
        app.cli.add_command(init_db_command)
