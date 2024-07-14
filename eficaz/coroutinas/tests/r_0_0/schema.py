from repository import *

class Schema:
    
    
    def post(self, **kw):
        xcoroutine = yield  # Rerênciando memória como generator

        if xcoroutine == 'POST':  # Verificando método send() 
            xcoroutine = yield from iter(RepoPost(name=kw['name'], passwd=kw['passwd'], email=kw['email']))
            next(xcoroutine)
            yield xcoroutine


    def get(self, **kw):
        xcoroutine = yield
        if xcoroutine == 'GET':
            xcoroutine = yield from iter(RepoGet(name=kw['name'], passwd=kw['passwd'], email=kw['email']))
            next(xcoroutine)
        yield xcoroutine
            # Uma alteracão só pode ocorrer após um login
    
    def put(self):
        xcoroutine = yield    
        if xcoroutine[0] == 'PUT':
            _, name, passwd, email = xcoroutine

            xcoroutine = yield from iter(RepoPut(name=name, passwd=passwd, email=email))
            next(xcoroutine)
            yield xcoroutine


if __name__ == '__main__':  # Teste unitário de objetos/coroutinas
    ...