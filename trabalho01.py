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
#

arq = open( arquivo , 'r')

leitura_texto = arq.readlines()

G = nx.Graph()

for linhas in leitura_texto :
    no = linhas.split()
    #Criando as arestas e os vertices se nao existirem
    G.add_edge(no[0], no[1])

arq.close()

texto = G.number_of_edges()


#
# Abertura do arquivo de saida com os resultados
#

var_resultados = 'resultados' + str(op_rede) + '.txt'

arq = open(var_resultados, 'w')

arq.write('Ola')


arq.close()
