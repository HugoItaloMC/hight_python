import PySimpleGUIQt as pyqt

from __init__ import Schema

class FrontEnd:

    def __init__(self):
        self.__window = pyqt.FlexForm(title='THE SIMPLE GUI', size=(210, 160))
        self.__LAYOUT: list = [
        [pyqt.Text('=' * 25, justification='center')],
        [pyqt.Text("TASKS", justification='center', font=("Goto", 15))],
        [pyqt.Text("_" * 25, justification='center')],

        [pyqt.Stretch(),
        pyqt.Checkbox('N', font=("Sans-serif", 10), key='N'),
        pyqt.Checkbox('X', font=("Sans-serif", 10), key='X'),
        pyqt.Checkbox('Y', font=("Sans-serif", 10), key='Y'), 
        pyqt.Stretch()],
        [pyqt.Text('_' * 25, justification='center')],
        
        [pyqt.Text("UTILS", justification='center', font=("Goto", 15))],
        
        [pyqt.Radio('somente par', 'RADIO1', default=False, font=("Sans-serif", 11), key='par'), pyqt.Stretch()],

        [pyqt.Button('Executar Tarefa', key='start_task')],
        [pyqt.Exit()]
        ]
    
    def __iter__(self):
        self.__window.Layout(self.__LAYOUT)
        while True:
            global schema
            schema = None
            event, values = self.__window.read()

            if event in (None, 'Exit'):
                exit()

            if event == 'start_task':
                cj_tasks = {key for key, values in values.items() if values}

                while not cj_tasks:
                    break

                data_range = set(range(1, 101))


                # Enviando tarefas com  funcões/objetos auxiliares
                if 'par' in cj_tasks:
                    cj_tasks.discard('par')
                    schema = iter(Schema(cj_tasks.pop(), data_range, 'par'))
                
                # Enviando tarefas 
                if schema is None:
                    schema = iter(Schema(cj_tasks.pop(), data_range))

                # Iniciando corroutina de Schema
                next(schema)    
                factory = schema.send('START')
                if ~factory:
                    +factory
                    pyqt.popup('OPERACÃO CONCLUÍDA COM SUCESSO')

                else:
                    pyqt.popup('Error %s' % factory.__dict__)

                
                schema.close()


        else:
            self.__window.close()
            return self

if __name__ == '__main__':
    iter(FrontEnd())