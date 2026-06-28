# Projeto de Análise e Projeto de Algorirmos - Problema dos postos A e B

O projeto a ser entregado (codigo, relatorio, testes, anexos, etc) será inteiramente organizado neste repositório.

Integrantes: Alyson Valério Isaluski, Atos Aires Arrudo, Leandro Hyeda Martins, Rainier Ryu Waki


### Rodar Script principal

```python3 main.py <dimacs_file_path>```

exemplo de <dimacs_file_path>: /home/user/Documentos/grafo.col


### Converter .col para .dot

```python3 convert.py <dimacs_file_path>```

exemplo de <dimacs_file_path>: /home/user/Documentos/grafo.col


### Instalar Visualizador de Grafo GraphViz
https://graphviz.org/download/s


### Desenhar grafo

```neato -Tpng <dot_file_name> -o <output_image_file_name> -Goverlap=scale```

exemplo de <dot_file_name>: grafo.dot

exemplo de <output_image_file_name>: grafo.png