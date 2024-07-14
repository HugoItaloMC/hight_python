from app.repository.repo_auth import RepoUser, RepoUserLogin, RepoUserID
from app.src.wrapper import ContainerCoroutine


class RegisterUser:

    def __init__(self, **kw):
        self.name = kw['name']
        self.passwd = kw['passwd']
        self.email = kw['email']

    def __call__(self, **kw):
        user = RepoUser(name=self.name, passwd=self.passwd, email=self.email)
        ContainerCoroutine(args=user())


class LoginUser:

    def __init__(self, **kw):
        self.name = kw['name']
        self.passwd = kw['passwd']
        self.email = kw['email']
        self.token = None

    def __call__(self, **kw):
        user = RepoUserLogin(name=self.name, passwd=self.passwd, email=self.email)
        ContainerCoroutine(args=user())
        self.token = user.token
        return user


class UserID:

    def __init__(self, **kw):
        self.id = kw['id']

    def __call__(self, **kwargs):
        user_id = RepoUserID(id_=self.id)
        ContainerCoroutine(args=user_id())
        return user_id
