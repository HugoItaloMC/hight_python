from wrapper import Descritor
from __init__ import RepoUserPost

class SchemaUserPost(RepoUserPost):
    
    def __init__(self, *args):
        super().__init__(*args)
    
    
    def __call__(self, method: str):
        super(__class__, self).__call__(method=method)
    

    
