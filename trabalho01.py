#
# Autor: Gabriel Henrique Campos Scalici (9292970)
# Trabalho realizado para a materia de Redes Complexas
# ICMC - USP SAO CARLOS
# DATA: 14/09/2017
#

import networkx as nx
import powerlaw as pl
#import matplotlib.pyplot as plt

#
#   Menu para falicitar a escolha de redes
#

var_usair = 'USairports.txt'
var_euror = 'euroroad.txt'
var_hamst = 'hamster.txt'
var_power = 'powergrid.txt'

print('Selecione a rede desejada:')
print('1 - USairports \n2 - euroroad \n3 - hamster \n4 - powergrid')

op_rede = input()

if op_rede == 1:
    arquivo = 'USairports.txt'
elif op_rede == 2:
    arquivo = 'euroroad.txt'
elif op_rede == 3:
    arquivo = 'hamster.txt'
elif op_rede == 4:
    arquivo = 'powergrid.txt'

#
# Abertura do arquivo/ selecao das colunas necessarias / Criacao Grafo
#

arq = open( arquivo , 'r')

leitura_texto = arq.readlines()

G = nx.Graph()

for linhas in leitura_texto :
    no = linhas.split()
    #Criando as arestas e os vertices se nao existirem
    G.add_edge(no[0], no[1])

arq.close()

#
# Inicio das funcoes que devem ser implementadas
#


#
# (3) Extraindo o Maior componente da Rede
#


#
# (4) Distribuicao dos graus da rede/ Qual eh sem escala/ Estimativa da lei de potencia
#


#
# (5) Medida das propriedade das redes (Montar Tabela)
#

#Numero de Vertices
numero_vertices = G.number_of_nodes()
numero_arestas = G.number_of_edges()

#Grau Medio
from networkx.algorithms import approximation as imp
grau_medio = imp.node_connectivity(G)

#Segundo momento da distribuicao do Grau

#Media dos coeficientes de aglomeracao local

#Coeficiente de aglomeracao pela forma da transitividade

#Media dos menores Caminhos

#Diametro


#
# (6) Histograma para rede
#

#Distribuicao acumulada dos coeficientes de aglomeracao local

#Distribuicao dos menores caminhos


#
# (7) Entropia de Shannon para redes reais
#

# Betweenness centrality
#bet_centrality = nx.betweenness_centrality(G)

# Closenness Centrality

# Eigenvector centrality

# PageRank


#
# (8) Coeficiente de Parson
#



#
# Plotar o grafo, apenas para visualizacao
#

#plt.figure(1, figsize=(12, 8))
#pos=nx.fruchterman_reingold_layout(G)
#plt.axis('off')
#nx.draw_networkx_nodes(G,pos,node_size=50)
#nx.draw_networkx_edges(G,pos,alpha=0.4)
#plt.title('Func', size=16)
#plt.show()

#
# Abertura do arquivo de saida com os resultados
#

#Arquivo de saida diferente para cada rede analisada
var_resultados = 'resultados' + str(op_rede) + '.txt'

arq = open(var_resultados, 'w')

arq.write('Connectivity : ' + str(grau_medio) + '\n')
arq.write('Numero de vertices : ' + str(numero_vertices))

arq.close()
