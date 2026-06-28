## Converte arquido Dimacs (.col) para Dot (.dot).
## Arquivo Dot é lido por Graphviz para gerar um arquivo com a imagem intuitiva do grafo
## Informe o path do arquivo .col, e o output será o arquivo .dot no mesmo diretório

import sys
import os

def dimacsToDot(filepath):
    if not os.path.isfile(filepath):
        print(f"Erro: Arquivo '{filepath}' não encontrado.")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_name = os.path.splitext(os.path.basename(filepath))[0]
    
    output_filename = f"{base_name}.dot"
    output_filepath = os.path.join(script_dir, output_filename)

    try:
        with open(filepath, 'r') as dimacs_file, open(output_filepath, 'w') as dot_file:
            dot_file.write("graph G {\n")
            
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

if(len(sys.argv) < 2):
    print("Erro. Nenhum caminho de arquivo Dimacs informado.")
    sys.exit(1)

input_filepath = sys.argv[1]
dimacsToDot(input_filepath)