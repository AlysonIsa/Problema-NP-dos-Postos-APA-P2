# Usar time.perf_counter() para testar performance

import os
import sys

# Dimacs to graph_data
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

# graph_data to Dimacs
def writeDimacsGraph(graph_data, file_name):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    output_filename = f"{file_name}"
    output_file_path = os.path.join(script_dir, output_filename)

    with open(output_file_path, 'w') as file:
        file.write("c Arquivo gerado a partir do dicionario graph_data\n")
        
        # Salva as centrais como comentários (ex: "c centrais 1 5 12")
        if graph_data.get('centrais'):
            centrais_str = " ".join(map(str, graph_data['centrais']))
            file.write(f"c centrais {centrais_str}\n")
            
        prob_type = graph_data.get('problem_type') or 'edge'
        n = graph_data.get('num_nodes', 0)
        m = graph_data.get('num_edges', 0)
        file.write(f"p {prob_type} {n} {m}\n")
        
        for u, v in graph_data.get('edges', []):
            file.write(f"e {u} {v}\n")
            
    print(f"Grafo salvo com sucesso em: {output_file_path}")


# Pruning: Reduz a parte sem solução do grafo resultado G do problema A, de forma que δ(parte sem solução de G) >= 2, onde δ é o grau mínimo do grafo
# Altera grafo resultado, colocando os postos com 100% de corretude

# Lógica da função recursiva prune:
# Seja d o grau do vértice e g o grafo da iteração atual de prune(g)
# Passo 1. 'return' se g é vazio ou δ(g) >= 2
# Passo 2. Coloca em G central em todos os vértices isolados de g (d = 0)
# Passo 3. Coloca em G central em todos os vizinhos de vértices folhas sem centrais de g (d = 1)
# Passo 4. Gera um subgrafo g' (pruned) sem os vércices de g que é central ou vizinho de central
# Passo 5. Chama prune(g')

def prune(g):
    # Instrução para adicionar central em G:
    # finalGraph['centrais'].append(<numeroDoGrafo>)

    # TODO implemntar essa função - Falta escolher estrutura de dados
    pass

if(len(sys.argv) <= 1):
    print("Erro. Nenhum caminho de arquivo Dimacs informado.")
    sys.exit()

path = sys.argv[1]

resultG = readDimacsGraph(path)

# Coloca centrais trivias em G ( δ(pruned(G)) < 2 )
prune(resultG)

print(resultG)

# Cria arquivo dimacs resultado, com centrais em comentário
writeDimacsGraph(resultG, "result.col")