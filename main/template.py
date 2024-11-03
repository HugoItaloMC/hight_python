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
        
        [pyqt.Radio('utils', 'RADIO1', default=False, font=("Sans-serif", 15), key='utils'), pyqt.Stretch()],

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
                if 'utils' in cj_tasks:
                    cj_tasks.discard('utils')
                    schema = iter(Schema(cj_tasks.pop(), data_range, 'utils'))
                
                # Enviando tarefas 
                if schema is None:
                    schema = iter(Schema(cj_tasks.pop(), data_range))

                # Iniciando corroutina de Schema
                next(schema)    
                exits, stats = schema.send('START')
                if exits == 1:
                    pyqt.popup('OPERACÃO CONCLUÍDA COM SUCESSO')
                    schema.close()
                else:
                    pyqt.popup('Error %s' % stats)
                    schema.close()
                
                schema.close()


        else:
            self.__window.close()
            return self

if __name__ == '__main__':
    iter(FrontEnd())