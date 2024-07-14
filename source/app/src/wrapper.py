"""
   -- Este módulo é responsável pela simultâniedade de aplicacão, onde cada
chamada ao banco de dados vindo da URL, uma request, vai ser tratada como
coroutina

"""
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

from app.src.core.handlers import HandlerWrapper


class ContainerCoroutine(HandlerWrapper):

    def __init__(self, args):
        super().__init__()
        self.args_ = args

    def __iter__(self):

        cores = multiprocessing.cpu_count()
        with ProcessPoolExecutor(max_workers=cores) as executor:
            self.queue.join()  # Bloqueando Queue se tarefas ñ forem concluidas
            executor.map(self._container(args=self.args_, cores=cores+1), timeout=0.3)


if __name__ == '__main__':
    from time import time
    init = time()
    instance_1 = ContainerCoroutine('teste1')  # OK
    instance_2 = ContainerCoroutine('teste2')  # OK
    finish = time()
    print(instance_1.queue.__dict__, id(instance_2), "\nFinish in : %s" % (finish - init))
    # SOME TEST: 140331052948112 140331054446224
