import PySimpleGUIQt as pyqt

from __init__ import Schema

class FrontEnd:

    def __init__(self):
        self.__LAYOUT: list = [
        [pyqt.Text('=' * 80, justification='center')],
        [pyqt.Text("TASKS", justification='center', font=("Goto", 15))],
        [pyqt.Text("_" * 80, justification='center')],

        [pyqt.Stretch(),
        pyqt.Checkbox('N', font=("Sans-serif", 10), key='N'),
        pyqt.Checkbox('X', font=("Sans-serif", 10), key='X'),
        pyqt.Checkbox('Y', font=("Sans-serif", 10), key='Y'), 
        pyqt.Stretch()],
        [pyqt.Text('_' * 80, justification='center')],

        [pyqt.Button('Executar Tarefa', key='start_task')],
        [pyqt.Exit()]
        ]
        self.__window = pyqt.Window(title='THE SIMPLE GUI', size=(280, 210), layout=self.__LAYOUT)
    
    def __iter__(self):
        while True:
            event, values = self.__window.read()

            if event in (None, 'Exit'):
                exit(1)

            if event == 'start_task':
                cj_tasks = {key for key, values in values.items() if values}

                while not cj_tasks:
                    break

                for line in cj_tasks:
                    data_range = set(range(1, 101))
                    schema = iter(Schema(line, data_range))
                    next(schema)

                    exits, stats = schema.send('START')

                    if exits == 1:
                        pyqt.popup('OPERACÃO CONCLUÍDA COM SUCESSO')
                    
                    else:
                        pyqt.popup('Error %s' % stats)

if __name__ == '__main__':
    while True:
        iter(FrontEnd())
