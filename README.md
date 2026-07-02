# Projeto de Análise e Projeto de Algoritmos - Problema dos Postos de Monitoramento (A e B)

O projeto aborda o problema de encontrar o menor número de centrais de monitoramento (Conjunto Dominante Mínimo) em duas disposições diferentes de parques florestais:

* **Parte A (Parque Geral):** A disposição dos postos é arbitrária. A modelagem recai sobre o problema do Conjunto Dominante Mínimo em grafos gerais, que é um problema **NP-Difícil**. A solução implementada utiliza um algoritmo exato de **Branch and Bound** (com podas por tamanho e viabilidade de cobertura) para encontrar a resposta ótima.
* **Parte B (Parque Linear):** O parque é uma trilha contínua, modelado como um **Grafo de Intervalos**. Ao explorar essa característica estrutural, o problema deixa de ser NP-Difícil. Implementamos um **Algoritmo Guloso** exato que resolve a instância em tempo polinomial O(nlog(n)), garantindo otimalidade.

Este repositório contém todo o código-fonte, relatórios, testes e utilitários de visualização.

A data de entrega é **01/07/2026**.

**Integrantes:** Alyson Valério Isaluski, Atos Aires Arruda, Leandro Martins Hyeda, Rainier Ryu Waki

---

## Organização dos Arquivos

* `solutionA.py`: Script Python - Resolve o problema A (Grafo Geral) lendo arquivos `.col`. Imprime as métricas no terminal e gera um arquivo `result.col` com as centrais escolhidas em formato de comentário.
* `solutionB.py`: Script Python - Resolve o problema B (Parque Linear) lendo arquivos `.intervalos.txt`. Utiliza estratégia gulosa de varredura para selecionar as centrais ótimas de forma muito rápida.
* `convert.py`: Script Python - Converte arquivos DIMACS (`.col`) para o formato `.dot`, permitindo gerar uma representação visual do grafo (com as centrais destacadas) usando Graphviz.
* `referencias/`: Diretório - Contém o enunciado do problema em PDF, informações complementares de testes e instâncias de grafos (`.col` e `.intervalos.txt`) fornecidas para avaliação.

---

## Execução e Interpretação dos Resultados

Os scripts são feitos em Python e não requerem compilação, basta rodá-los diretamente pelo interpretador.

### 1. Rodar a Solução da Parte A (Parque Geral)

O script requer um arquivo DIMACS de grafo como entrada.

```bash
python3 solutionA.py <caminho_arquivo.col>

```

**Exemplo:**

```bash
python3 solutionA.py /home/user/Documentos/P01_completo_12.col

```

**Interpretação da Saída:**
O terminal exibirá a quantidade mínima de centrais, a lista de postos escolhidos, a validação de otimalidade e o tempo exato de execução utilizando o relógio monotônico de alta resolução.
Adicionalmente, o script criará (ou sobrescreverá) um arquivo chamado **`result.col`** no mesmo diretório, contendo a estrutura do grafo e uma linha de comentário indicando as centrais (ex: `c centrais 1 5 12`), pronto para ser desenhado.

---

### 2. Rodar a Solução da Parte B (Parque Linear)

Para o parque linear, o algoritmo ignora as arestas e foca exclusivamente nas coordenadas geográficas dos postos. O script requer o arquivo de intervalos.

```bash
python3 solutionB.py <caminho_arquivo.intervalos.txt>

```

**Exemplo:**

```bash
python3 solutionB.py /home/user/Documentos/P01_linear.intervalos.txt

```

**Interpretação da Saída:**
Similar à Parte A, o terminal exibirá a solução ótima e o tempo de execução. Note que o tempo de execução deste script deverá ser em frações de milissegundos comparado ao algoritmo da Parte A, provando a eficiência da exploração da estrutura de intervalos.