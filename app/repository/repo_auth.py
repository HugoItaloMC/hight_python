__all__ = ['RepoAuthPost']

from typing import Generator, Coroutine, Tuple

from sqlalchemy import insert

from db import Session
from db._all_models import AuthModel

class RepoAuthPost:

    def __init__(self, nrequest: Tuple) -> None:
        self.request = nrequest


    def __iter__(self) -> Generator:
        send: Coroutine = yield

        if send:
            for line in self.request:
                print(line)
            yield

if __name__ == '__main__':
    from collections import namedtuple
    Request = namedtuple('Request', ('name', 'passwd', 'email', 'method'))

    xdata = Request('Name111', 'Passwd111', 'Email111', 'POST')
    data = iter(RepoAuthPost(xdata))
    next(data)
    data.send(True)