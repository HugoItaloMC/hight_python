from src import Facade

class Schema:
    # Client Class
    def __init__(self, *args):
        self.__args = args
    
    def __iter__(self):
        send = yield
        global facade
        facade = None
        if 'START' in send.upper():

            # Verificando se template solicitou funcões/objetos auxiliares e enviando
            if len(self.__args) > 2:
                facade = iter(Facade(self.__args[0], self.__args[1], self.__args[2]))
            
            # Enviando tarefas recebidas de template sem funcões/objetos auxiliares
            if facade is None:
                facade = iter(Facade(self.__args[0], self.__args[1]))
            
            # Iniciando corroutina de Facade
            next(facade)  
            # Executando tarefa incluída na factory a qual foi chamada, verificando status e saída
            yield facade.send('SET')  
        else:
            send.close()
            exit(0)
        facade.close()

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

    