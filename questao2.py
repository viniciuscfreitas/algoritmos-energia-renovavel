
import matplotlib.pyplot as plt

# Definindo as estações e a matriz de adjacências
estacoes = [
    "Estação A", "Estação B", "Estação C", "Estação D", "Estação E",
    "Estação F", "Estação G", "Estação H", "Estação I", "Estação J"
]

matriz_adjacencias = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
]

# Salvar a matriz de adjacências como imagem
def salvar_imagem_matriz(estacoes, matriz):
    plt.figure(figsize=(10, 10))
    plt.imshow(matriz, cmap="Greys", interpolation="none")
    plt.xticks(range(len(estacoes)), estacoes, rotation=90)
    plt.yticks(range(len(estacoes)), estacoes)
    plt.colorbar(label="Conexão")
    plt.title("Matriz de Adjacências")
    plt.savefig("matriz_adjacencia.png")

# Exemplo de uso
if __name__ == "__main__":
    salvar_imagem_matriz(estacoes, matriz_adjacencias)
