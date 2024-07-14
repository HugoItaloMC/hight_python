from orm import create_tables
from schemas import SchemaUser


if __name__ == '__main__':
    #create_tables()     # Zerando a base de dados
    SchemaUser(('name11', 'senhateste11', 'email11teste@app.com'))()