# Projeto de Análise e Projeto de Algorirmos - Problema dos postos A e B

O projeto a ser entregado (codigo, relatorio, testes, anexos, etc) será inteiramente organizado neste repositório.

A data de entrega é **01/07/2026**.

Integrantes: Alyson Valério Isaluski, Atos Aires Arrudo, Leandro Hyeda Martins, Rainier Ryu Waki



## Organização dos arquivos:

**solutionA**: Script Python - Resolve o problema A, imprimindo a solução na tela e gerando seu arquivo dimacs

**convert.py**: Script Python - Converte Dimacs para arquivo Dot, o qual Graphviz consegue gerar uma representação visual do grafo, com centrais

**referencias/**: Diretorio - Contém enunciado do problema em pdf, LEIA-ME com informações do problema e testes, e arquivos .col com alguns exemplos de grafo usados para teste de avaliação.



## Execução e geração de imagem do grafo (sem compilação pq python lixo usa interpretador, ent não precisa)

### Rodar Script da solução para o problema 1 (Postos A)

```python3 solutionA.py <dimacs_file_path>```

exemplo de <dimacs_file_path>: /home/user/Documentos/P01_completo_12.col



### Converter .col para .dot

```python3 convert.py <dimacs_file_path>```

ou se quiser marcar centrais específicas para teste (ex: marcar 3, 7 e 12 como centrais manualmente):

```python3 convert.py <dimacs_file_path> 3 7 12``` 

exemplo de <dimacs_file_path>: /home/user/Documentos/result.col


### Instalar Visualizador de Grafo GraphViz (Windows, Linux ou Mac)
https://graphviz.org/download/s


### Desenhar grafo com GraphViz

```neato -Tpng <dot_file_name> -o <output_image_file_name> -Goverlap=scale```

exemplo de <dot_file_name>: result.dot

exemplo de <output_image_file_name>: grafo.png


<img width="323" height="314" alt="image" src="https://github.com/user-attachments/assets/2ab2d7d7-e789-4dec-b122-a6009f75d3b5" />

Imagem gerada pelo fluxo:

```python3 solutionA.py /home/user/Documentos/parte_A_parque_geral/P01_completo_12.col```

```python3 convert.py result.col 12```

```neato -Tpng result.dot -o grafo.png -Goverlap=scale```


