from orm import create_tables
from schemas import SchemaUserPost


if __name__ == '__main__':
    #create_tables()     # Zerando a base de dados
    SchemaUserPost(('name11', 'senhateste11', 'email11teste@app.com'))('POST')