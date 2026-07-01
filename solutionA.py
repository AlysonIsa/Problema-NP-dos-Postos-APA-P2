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

def solve(adj, n):
    """
    Encontra o Conjunto Dominante Mínimo usando Branch and Bound.
    
    :param adj: Dicionário representando a lista de adjacência do grafo (1-indexado)
    :param n: Número total de vértices
    :return: (tamanho_minimo, melhor_solucao)
    """
    # Variáveis Globais do Escopo do Algoritmo
    tamanho_minimo = n
    melhor_solucao = list(range(1, n + 1))
    
    d_atual = []                # Conjunto de vértices escolhidos na chamada atual
    cobertura = [0] * (n + 1)   # Array que conta quantas vezes cada vértice está coberto

    def bb(u):
        nonlocal tamanho_minimo, melhor_solucao
        
        # Já passamos por todos os vértices (atingiu a folha da árvore)
        if u > n:
            # Todos os vértices de 1 a n devem ter cobertura > 0
            if all(cobertura[i] > 0 for i in range(1, n + 1)):
                # Se for estritamente menor que o tamanho mínimo atual, atualiza
                if len(d_atual) < tamanho_minimo:
                    tamanho_minimo = len(d_atual)
                    melhor_solucao = list(d_atual)
            return

        # Inclui vértice u

        d_atual.append(u)
        cobertura[u] += 1
        for vizinho in adj[u]:
            cobertura[vizinho] += 1

        # Avança para o próximo vértice
        bb(u + 1)

        # Faz o Backtracking das alterações da inclusão de u para limpar estado
        for vizinho in adj[u]:
            cobertura[vizinho] -= 1
        cobertura[u] -= 1
        d_atual.pop()

        # Não inclui vértice u

        # 1º poda: Limite por tamanho
        # Se o tamanho atual já igualou ou superou o mínimo global, não há como melhorar
        if len(d_atual) >= tamanho_minimo:
            return

        # 2º poda: Limite por viabilidade (Inviabilidade de Cobertura)
        # Se algum vértice ficou sem cobertura (0) e a sua última oportunidade de ser 
        # coberto acabou de passar (ele e todos os seus vizinhos são <= u), corta o ramo.
        for v in range(1, n + 1):
            if cobertura[v] == 0:
                if v <= u and all(vizinho <= u for vizinho in adj[v]):
                    return  # Poda aqui (esse caminho nunca gerará uma solução válida)

        # Se passou pelo pruning, avança sem incluir u
        bb(u + 1)

    # Inicia a árvore de decisão a partir do vértice 1
    bb(1)
    return tamanho_minimo, melhor_solucao

if __name__ == "__main__":
    import time

    if len(sys.argv) <= 1:
        print("Erro. Nenhum caminho de arquivo Dimacs informado.")
        sys.exit()

    path = sys.argv[1]

    # Lê o grafo e gera o dicionário
    resultG = readDimacsGraph(path)

    n = resultG['num_nodes']

    # Inicializa o dicionário com listas vazias para todos os vértices
    adj = {i: [] for i in range(1, n + 1)}
    
    # Add arestas nas duas direções
    for u, v in resultG['edges']:
        adj[u].append(v)
        adj[v].append(u)


    start_time = time.perf_counter()
    
    tamanho_minimo, melhor_solucao = solve(adj, n)
    
    end_time = time.perf_counter()
    exec_time = end_time - start_time

    resultG['centrais'] = melhor_solucao

    # Exibe a saída formatada de acordo com o padrão exigido no trabalho
    print(f"Quantidade minima de centrais: {tamanho_minimo}")
    print(f"Postos escolhidos: {' '.join(map(str, sorted(melhor_solucao)))}")
    print(f"Otimalidade comprovada: sim")
    print(f"Tempo de execucao: {exec_time:.5f} segundos")
    print("-" * 40)

    writeDimacsGraph(resultG, "result.col")