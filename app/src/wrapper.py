"""
   -- Este módulo é responsável pela simultâniedade de aplicacão, onde cada
chamada ao banco de dados vindo da URL, uma request, vai ser tratada como
coroutina

"""
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

from app.utils.core.handlers import HandlerWrapper


class ContainerCoroutine(HandlerWrapper):

    def __init__(self, args):
        self.args_ = super(__class__, self).__init__(args)

    def __iter__(self):
        cores = multiprocessing.cpu_count()
        with ProcessPoolExecutor(max_workers=cores) as executor:
            for _ in range(1, cores + 1, 1):
                executor.map(self._container(args=self.args_))


if __name__ == '__main__':
    instance_1 = ContainerCoroutine('teste1')  # OK
    instance_2 = ContainerCoroutine('teste2')  # OK
    print(id(instance_1), id(instance_2))
    # SOME TEST: 140331052948112 140331054446224
