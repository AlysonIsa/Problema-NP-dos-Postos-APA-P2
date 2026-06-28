import sys
import os

def dimacsToDot(filepath, centrais=None):
    if not os.path.isfile(filepath):
        print(f"Erro: Arquivo '{filepath}' não encontrado.")
        sys.exit(1)

    # Garante que centrais seja uma lista, mesmo se nada for passado
    if centrais is None:
        centrais = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_name = os.path.splitext(os.path.basename(filepath))[0]
    
    output_filename = f"{base_name}.dot"
    output_filepath = os.path.join(script_dir, output_filename)

    try:
        with open(filepath, 'r') as dimacs_file, open(output_filepath, 'w') as dot_file:
            dot_file.write("graph G {\n")
            
            # Configuração padrão visual dos nós e arestas
            dot_file.write("    node [shape=circle, style=filled, fillcolor=lightgrey, color=black, fontcolor=black];\n")
            dot_file.write("    edge [color=dimgrey];\n\n")
            
            # Aplica o estilo destacado para as centrais informadas
            if centrais:
                dot_file.write("    // Destacando as centrais de monitoramento\n")
                for central in centrais:
                    dot_file.write(f"    {central} [fillcolor=firebrick, fontcolor=white, shape=doublecircle, color=black];\n")
                dot_file.write("\n")
            
            # Processa as arestas do arquivo DIMACS
            for line in dimacs_file:
                line = line.strip()
                if line.startswith('e '):
                    parts = line.split()
                    if len(parts) >= 3:
                        u, v = parts[1], parts[2]
                        dot_file.write(f"    {u} -- {v};\n")
            
            dot_file.write("}\n")
            
        print(f"Sucesso! Arquivo convertido salvo em:\n{output_filepath}")
        
    except Exception as e:
        print(f"Um erro aconteceu durante a conversão: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erro. Uso correto: python convert.py <caminho_arquivo_dimacs> [central1 central2 ...]")
        sys.exit(1)

    input_filepath = sys.argv[1]
    
    # Captura todos os argumentos passados após o nome do arquivo como a lista de centrais
    lista_centrais = sys.argv[2:]
    
    dimacsToDot(input_filepath, lista_centrais)