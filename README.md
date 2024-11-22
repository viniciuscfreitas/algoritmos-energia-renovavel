# Trabalho de Algoritmos: Energia Renovável e Estruturas de Dados

Este projeto foi desenvolvido para responder às três questões propostas sobre energia renovável, utilizando conceitos de algoritmos e estruturas de dados, como árvores binárias, grafos e análise de complexidade.

---

## 1. Informações do Grupo

- **Integrantes:**
    1. Vinicius do Carmo Fonseca Freitas - **RM 97599**
    2. Gustavo Cristiano Pessoa de Souza - **RM 551924**
    3. Gustavo Medeiros Miranda da Silva - **RM 552093**

---

## 2. Estrutura do Projeto

### Arquivos Incluídos
- **`dados.csv`**: Arquivo contendo os dados reais de 20 países com as seguintes variáveis:
    - População (em milhões)
    - PIB per capita (em dólares)
    - Emissões de CO₂ (em milhões de toneladas métricas)
    - Produção de energia nuclear (em TWh)
    - Produção de energia eólica (em TWh)

- **`questao1.py`**: Implementação da árvore binária para organizar e buscar países com base no PIB per capita.
- **`questao2.py`**: Representação de um sistema fictício de transporte por meio de grafos e matriz de adjacências.
- **`questao3.py`**: Comparação de duas funções resolvendo o mesmo problema, com complexidades diferentes (O(n) e O(log n)).
- **`matriz_adjacencia.png`**: Imagem gerada pelo código da Questão 2, representando a matriz de adjacências.

---

## 3. Descrição das Questões

### Questão 1: Árvores Binárias com Dados de Países
- **Objetivo**: Organizar e buscar informações sobre países utilizando uma estrutura de árvore binária.
- **Descrição**:
    - Foi criada uma árvore binária baseada no **PIB per capita** dos países.
    - As funções de **inserção** e **busca** permitem adicionar países à árvore e encontrar um país específico com base no PIB.
    - Os dados reais de 20 países foram utilizados do arquivo `dados.csv`.

- **Como executar**:
    1. Certifique-se de que o arquivo `dados.csv` está no mesmo diretório que o código.
    2. Execute o script:
       ```bash
       python questao1.py
       ```
    3. O resultado da busca será exibido no terminal, como no exemplo:
       ```
       Resultado da busca: {'pais': 'Brasil', 'populacao': 212, 'pib_per_capita': 14400.0, 'emissoes_co2': 467.0, 'energia_nuclear': 0.0, 'energia_eolica': 60.0}
       ```

---

### Questão 2: Grafos - Matriz de Adjacências
- **Objetivo**: Representar um sistema de transporte ferroviário ou metroviário como um grafo.
- **Descrição**:
    - Foi criada uma matriz de adjacências para representar 10 estações fictícias e suas conexões.
    - O grafo é salvo como uma imagem (`matriz_adjacencia.png`), que ilustra a matriz de adjacências.

- **Como executar**:
    1. Execute o script:
       ```bash
       python questao2.py
       ```
    2. O arquivo `matriz_adjacencia.png` será gerado no mesmo diretório.

---

### Questão 3: Funções e Complexidade
- **Objetivo**: Comparar duas funções resolvendo o mesmo problema, mas com diferentes complexidades.
- **Descrição**:
    - **Função Lenta (O(n))**: Encontra o maior número de uma lista percorrendo todos os elementos.
    - **Função Rápida (O(log n))**: Usa `sorted()` para encontrar o maior número rapidamente.
    - Foi feita uma análise comparativa dos tempos de execução.

- **Como executar**:
    1. Execute o script:
       ```bash
       python questao3.py
       ```
    2. O terminal exibirá o resultado das duas funções e os tempos de execução, como no exemplo:
       ```
       Resultado da função lenta: 999
       Tempo da função lenta: 2.7179718017578125e-05
       Resultado da função rápida: 999
       Tempo da função rápida: 7.152557373046875e-06
       ```

---

## 4. Tecnologias Utilizadas
- **Python 3.12**
- **Bibliotecas**:
    - `matplotlib`: Para gerar a imagem da matriz de adjacências.
    - `csv`: Para leitura do arquivo `dados.csv`.
    - `time`: Para medir o tempo de execução das funções na Questão 3.

---

## 5. Como Configurar o Ambiente
1. Certifique-se de ter o Python 3.12 instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install matplotlib
   ```
3. Verifique se todos os arquivos do projeto estão no mesmo diretório.

---

## 6. Conclusão
Este projeto demonstra a aplicação de estruturas de dados e algoritmos na solução de problemas relacionados à energia renovável e sistemas de transporte. Os três scripts foram desenvolvidos com base nos requisitos estabelecidos, utilizando dados reais e representações precisas.

Se houver dúvidas ou necessidade de ajustes, estamos à disposição!

---

## 7. Arquivos Incluídos
- `dados.csv`
- `questao1.py`
- `questao2.py`
- `questao3.py`
- `matriz_adjacencia.png`