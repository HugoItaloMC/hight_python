from app.repository.repo_auth import register_user
from app.utils.wrapper import ContainerCoroutine


class RegisterUser:

    def __init__(self, **kw):
        self.name = kw['name']
        self.passwd = kw['passwd']
        self.email = kw['email']

    def __iter__(self, **kw):
        ContainerCoroutine(args=register_user(name=self.name, passwd=self.passwd, email=self.email) or kw.keys())
