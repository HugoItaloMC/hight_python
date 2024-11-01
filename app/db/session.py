from sqlalchemy import insert

from handlers import *

__all__ = ['DBSession']

class DBSession(HandlerORM):

    def __init__(self, *args):
        super(__class__, self).__init__()
        self.args = args
        self.session = None
    

    def __call__(self):
        return super().__call__()
    
    ### CAN WILL USE JUST AFTER DO IT RUN INIT FUNCTION
    def __enter__(self):
        if not self._engine:
            self()
            db = iter(self)
            next(db)
            self.session = db.send(self.args[0])
            return self.session
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
    
    # ONCE'LL DO USE
    def init_db(self):
        import _all_models
        if not self._engine:
            self()
        with self._engine.connect() as engine:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
        
        

if __name__ == '__main__':
    from _all_models  import AuthModel
    #db = DBSession()
    #db.init_db()
    with DBSession('SET') as session:
        user: AuthModel = insert(AuthModel).values(name='name22', passwd='passwd22', email='email22@app.com')
        session.execute(user)