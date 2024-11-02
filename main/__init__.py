from src import Facade

class Schema:
    # Client Class
    def __init__(self, *args):
        self.__args = args
    
    def __iter__(self):
        send = yield
        if 'START' in send.upper():
            start = iter(Facade(self.__args[1]))  # Enviando dados para Facade
            next(start)  # Iniciando a corroutina da Facade
            start.send(self.__args[0])  # Enviando operacão, chamando factory imputida na facade
            yield start.send('SET')  # Executando tarefa incluída na factory a qual foi chamada
        else:
            send.close()
            exit(0)

if __name__ == '__main__':
    ALLOWED = ('N', 'X', 'Y')
    while (op := input("ESCOLHA OPERACÃO\n\n\nOPERACÕES(Y, N, X)\ndigite `exit` para sair\n: ")) != 'exit':
        if op not in ALLOWED:
            print("OPERACÃO INVÁLIDA")
            pass
        else:
            schema = iter(Schema(op, set(range(1, 101))))
            next(schema)
            exits, stats = schema.send('START')

            if exits:
                print("OPERACÃO CONCLUÍDA\n")
            else:
                print("Error %s" % stats)
                break

    