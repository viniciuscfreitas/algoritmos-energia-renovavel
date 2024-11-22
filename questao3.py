
import time

# Função com complexidade O(n)
def funcao_lenta(lista):
    return max(lista)

# Função com complexidade O(log n)
def funcao_rapida(lista):
    return sorted(lista)[-1]

# Testando as funções
if __name__ == "__main__":
    lista = list(range(1000))
    inicio = time.time()
    print("Resultado da função lenta:", funcao_lenta(lista))
    print("Tempo da função lenta:", time.time() - inicio)

    inicio = time.time()
    print("Resultado da função rápida:", funcao_rapida(lista))
    print("Tempo da função rápida:", time.time() - inicio)
