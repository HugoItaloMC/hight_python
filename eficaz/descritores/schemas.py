from wrapper import Descritor
from __init__ import RepoUser

class SchemaUser(RepoUser):

    def __init__(self, *args):
        self.args = super().__init__(*args)
        self.post = Descritor()
    
    def __iter__(self):
        self.post = self.args
    

    
