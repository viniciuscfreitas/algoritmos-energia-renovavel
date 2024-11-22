
import csv

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, current, key, data):
        if key < current.key:
            if current.left:
                self._insert(current.left, key, data)
            else:
                current.left = Node(key, data)
        else:
            if current.right:
                self._insert(current.right, key, data)
            else:
                current.right = Node(key, data)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if not current:
            return None
        if current.key == key:
            return current.data
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right)

# Leitura dos dados do arquivo CSV
def carregar_dados_csv(arquivo):
    dados = []
    with open(arquivo, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dados.append({
                "pais": row["pais"],
                "populacao": int(row["populacao"]),
                "pib_per_capita": float(row["pib_per_capita"]),
                "emissoes_co2": float(row["emissoes_co2"]),
                "energia_nuclear": float(row["energia_nuclear"]),
                "energia_eolica": float(row["energia_eolica"]),
            })
    return dados

# Exemplo de uso
if __name__ == "__main__":
    dados = carregar_dados_csv("dados.csv")
    arvore = BinaryTree()
    for pais in dados:
        arvore.insert(pais["pib_per_capita"], pais)

    busca = arvore.search(14400)
    print("Resultado da busca:", busca)
