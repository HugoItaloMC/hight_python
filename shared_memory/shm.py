from multiprocessing import shared_memory
import ctypes

# Criar um bloco de memória compartilhada
valor = 42
valor_bytes = ctypes.c_uint8(valor)  # Converter para uint8
shm = shared_memory.SharedMemory(create=True, size=ctypes.sizeof(valor_bytes))

# Escrever o valor na memória compartilhada
shm.buf[:ctypes.sizeof(valor_bytes)] = bytes([valor])

print(f"Nome do bloco de memória compartilhada: {shm.name}")

shm.close()

