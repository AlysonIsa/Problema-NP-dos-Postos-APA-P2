# Usar time.perf_counter() para testar performance

def readDimacsGraph(file_path):
    graph_data = {
        "num_nodes": 0,
        "num_edges": 0,
        "problem_type": None,
        "edges": [],
        "centrais": [] # Conjunto de vértices com centrais de mon. do problema A
    }

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith('c'):
                continue

            parts = line.split()

            if parts[0] == 'p':
                graph_data['problem_type'] = parts[1]
                graph_data['num_nodes'] = int(parts[2])
                graph_data['num_edges'] = int(parts[3])
                 
            elif parts[0] in ('e', 'a'):
                u = int(parts[1])
                v = int(parts[2])
                graph_data['edges'].append((u, v))

    return graph_data

# Pruning: Reduz o grafo resultado G do problema A para δ >= 2, onde δ é o grau mínimo de G
# Altera grafo resultado, colocando os postos com 100% de corretude

# Lógica da função recursiva prune:
# Seja d o grau do vértice e g o grafo da iteração atual de prune(g)
# Passo 1. 'return' se g é vazio
# Passo 2. Coloque em G central em todos os vértices isolados de g (d = 0)
# Passo 3. Coloque em G central em todos os vizinhos de vértices folhas sem centrais de g (d = 1)
# Passo 4. Gere um subgrafo g' (pruned) sem os vércices de g que é central ou vizinho de central
# Passo 5. Chame prune(g')

def prune(g):
    # Instrução para adicionar central em G
    # finalGraph['centrais'].append(<numeroDoGrafo>)
    pass


import sys

if(len(sys.argv) <= 1):
    print("Erro. Nenhum caminho de arquivo Dimacs informado.")
    sys.exit()

path = sys.argv[1]

resultG = readDimacsGraph(path)


prune(resultG) # Coloca centrais trivias em G ( δ(pruned(G)) < 2 )

print(resultG)