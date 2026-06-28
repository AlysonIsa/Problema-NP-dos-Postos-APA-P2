# Usar time.perf_counter()

def readDimacsGraph(file_path):
    graph_data = {
        "num_nodes": 0,
        "num_edges": 0,
        "problem_type": None,
        "edges": []
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

import sys

if(len(sys.argv) <= 1):
    print("Erro. Nenhum caminho de arquivo Dimacs informado.")
    sys.exit()

path = sys.argv[1]

graph = readDimacsGraph(path)
print(graph)