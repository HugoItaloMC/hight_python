import argparse
import subprocess


class NameSpace:
    def __init__(self):
        # argparsers
        self.parser = argparse.ArgumentParser(description='Executar Programa em subprocess recebendo dados por CLI')
        self.parser.add_argument("--start", action='store_true', required=True, help='Inicia aplicacão')

    def __iter__(self):
        send = yield
        if send:
            namespaces = self.parser.parse_args()  # namespaces
            if namespaces.start:
                subprocess.run('python3 $HOME/Documentos/learnings/smooth/high_python/main/template.py', shell=True)
            exit()

if __name__ == '__main__':
    namespaces = iter(NameSpace())
    next(namespaces)
    namespaces.send(True)


