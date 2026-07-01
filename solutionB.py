import os
import sys
import time

# Lê os dados do arquivo de intervalos específico da Parte B
def readIntervals(file_path):
    intervals = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Ignora linhas vazias ou comentários/cabeçalhos eventuais
            if not line or line.startswith('c') or line.startswith('p'):
                continue
            
            parts = line.split()
            # Formato esperado: posto inicio fim
            if len(parts) >= 3:
                posto = int(parts[0])
                inicio = float(parts[1])
                fim = float(parts[2])
                intervals.append({'id': posto, 'start': inicio, 'end': fim})
                
    return intervals

# Algoritmo Guloso Exato para Grafos de Intervalos (Parque Linear)
def solve_linear_park(intervals):
    # Passo 1: Ordenar os intervalos pelo término da área monitorada (r_i)
    intervals.sort(key=lambda x: x['end'])
    
    centrais = []
    dominated = set()

    # Função auxiliar para verificar interseção entre dois postos
    def intersects(i1, i2):
        return max(i1['start'], i2['start']) <= min(i1['end'], i2['end'])

    # Passo 2: Varredura Gulosa
    for current in intervals:
        # Se o posto atual ainda não possui comunicação com nenhuma central
        if current['id'] not in dominated:
            best_candidate = current
            
            # Passo 3: Encontrar o vizinho que intercepta 'current' e alcança mais longe à direita
            for candidate in intervals:
                if intersects(current, candidate):
                    if candidate['end'] > best_candidate['end']:
                        best_candidate = candidate
            
            # Promove o melhor candidato a central de monitoramento
            centrais.append(best_candidate['id'])
            
            # Passo 4: Atualiza o status de todos os postos cobertos por essa nova central
            for other in intervals:
                if other['id'] not in dominated and intersects(best_candidate, other):
                    dominated.add(other['id'])
                    
    return centrais

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Erro. Nenhum caminho de arquivo de intervalos informado.")
        print("Uso: python3 solutionB.py <arquivo.intervalos.txt>")
        sys.exit()

    path = sys.argv[1]
    
    # Leitura
    intervals = readIntervals(path)
    
    # Medição de tempo exigida pelo protocolo de testes
    start_time = time.perf_counter()
    
    # Execução do Algoritmo Exato
    centrais_escolhidas = solve_linear_park(intervals)
    
    end_time = time.perf_counter()
    exec_time = end_time - start_time
    
    # Formatação de saída conforme o requisito do trabalho
    print(f"Quantidade minima de centrais: {len(centrais_escolhidas)}")
    print(f"Postos escolhidos: {' '.join(map(str, sorted(centrais_escolhidas)))}")
    print("Otimalidade comprovada: sim")
    print(f"Tempo de execucao: {exec_time:.5f} segundos")