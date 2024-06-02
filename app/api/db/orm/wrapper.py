import asyncio
from functools import wraps

from orm.utils.db_session import create_tables


def container(func):
    @wraps(func)
    def wrapper(args):
        create_ = func(args)
        next(create_)
        create_.send(args)
        return create_
    return wrapper


@container
def coroutine(args):
    while True:
        recv = yield args
        asyncio.run(recv)

