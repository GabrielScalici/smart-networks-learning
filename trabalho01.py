#
# Autor: Gabriel Henrique Campos Scalici (9292970)
# Trabalho realizado para a materia de Redes Complexas
# ICMC - USP SAO CARLOS
# DATA: 14/09/2017
#

import networkx as nx

#
#   Menu para falicitar a escolha de redes
#

var_usair = 'USairports.txt'
var_euror = 'euroroad.txt'
var_hamst = 'hamster.txt'
var_power = 'powergrid.txt'

print('Selecione a rede desejada:')
print('1 - USairports \n2 - euroroad \n3 - hamster \n4 - powergrid')

op = input()

if op == 1:
    arquivo = 'USairports.txt'
elif op == 2:
    arquivo = 'euroroad.txt'
elif op == 3:
    arquivo = 'hamster.txt'
elif op == 4:
    arquivo = 'powergrid.txt'

#
# Abertura do arquivo/ selecao das colunas necessarias / Criacao Grafo
#
#

arq = open( arquivo , 'r')

leitura_texto = arq.readlines()

G = nx.Graph()

for linhas in leitura_texto :
    no = linhas.split()
    #print(no[0], no[1])
    G.add_edge(no[0], no[1])

print(G.number_of_edges())
print(G.number_of_nodes())


arq.close()
