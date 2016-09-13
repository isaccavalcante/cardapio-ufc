#-*-coding: utf-8-*-
# Cardápio UFC versão 0.1
# Autor: Isac C.
from subprocess import Popen, PIPE
import os
import sys
import time

class cores:
	lilas = '\033[95m'
	azul = '\033[94m'
	verd = '\033[92m'
	amar = '\033[93m'
	verm = '\033[91m'
	negr = '\033[1m'
	subl = '\033[4m'
	fim =  '\033[0m'


def executar(cmd):
    processo = Popen([cmd], stdout=PIPE, shell=True)
    saida, erro = processo.communicate()
    return saida


html = executar("curl http://www.ufc.br/restaurante/cardapio/2-restaurante-universitario-do-interior 2> /dev/null")
html = html.split("Almoço")[1]


tags = ['<br />', '</center>', '<p>', '</p>', '<center>']
html = html.replace('<br>', '\n')
for t in tags:
    if t in html:
        html = html.replace(t, '')

dicionario = {"<b>":cores.negr, "<strong>":cores.negr, "</b>":cores.fim,\
     "</strong>":cores.fim, "<em>":cores.subl, "<i>":cores.subl, "</em>":cores.fim, "</i>":cores.fim,\
     "<td class=":"\n",  'colspan="2"><span class="item">':'->',"</td>":"","</tr>":"","<tr>":"", '</span><span class="item">':" - ", "<span>":"", "</span>":"",\
     '<span class="item">':" - ", 'colspan="2">':"", '"suco"':"", '"sobremesa"':'', '"principal"':"", '"guarnicao"':"", '"salada"':"", '"vegetariano"':"",\
     '"acompanhamento"':"", "<h3>":"", "</h3>":"", ">":"", '"jantar" colspan="3"':"", '<span class="item lactose"':" "
     
            }

for x in dicionario:
    if x in html:
        html = html.replace(x, dicionario[x])

for linha in  html.split("</tbody")[0].split('\n'):
    if linha.isspace() ==  False:
        print linha

