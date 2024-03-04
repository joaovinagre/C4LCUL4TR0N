
import random
import os
import argparse


manual = "Arredonde para duas casas decimais. \n Use ponto como vírgula."
win = "Parabens!!"
lose = "Burrinho kkkkkk"


parser = argparse.ArgumentParser(
                    prog='C4LCUL4TR0N',
                    description='******** Bem-vindo ao desafio de C4LCUL4TR0N ******** ',
                    epilog= 'O único jeito de conseguir o prêmio ao final do labirinto é respondendo corretamente pelo menos 20 desafios. Pressione "enter" para se provar.',
                    add_help= False
                    )

parser.add_argument('-e', dest='encontros', metavar='[ 5 ]', type=int, required=True)      # option that takes a value
parser.add_argument('-i', dest='input', metavar='')           # positional argument
parser.add_argument('-D', dest='dificuldade', metavar='', type=int)
parser.add_argument('-d', dest='manual', metavar='')

args = parser.parse_args()
infile = args.input 
encontros = args.encontros
dificuldade = args.dificuldade
manual_args = args.manual

parser.print_help()
if args.manual:
    print(manual)

respostas = []
gabarito = [] 
op = ['+','-','*','/', '**', '**']


'''
with open('Questões.txt', encoding= 'UTF-8') as arquivo: 
    lines = arquivo.readlines()
for i in lines:
    print(i) 
'''


def compararrespostas(lista1, lista2):
    if lista1 == lista2:
        print(win)
    else:
        print(lose)

def criarquestao(operação):
    ask = ' ?'
    space = ' '
    a, b, c = random.randint(0,100), random.randint(1,100), random.randint(0,len(operação)-1)
    if c == 4 or c == 5 :
        a, b = a/10, b-50 
        b = b/12
        b = round(b,0)
    questao = str(a) + space + operação[c] + space + str(b) + ask     #criando a questão
    buffer = eval(f"{a} {operação[c]} {b}")        
    buffer = round(buffer,2)
    gabarito.append(str(buffer))
    return print(questao)


### start:


for i in range(0,encontros):
    criarquestao(op)
    r = input()
    respostas.append(r)
compararrespostas(respostas, gabarito)
#print(respostas, gabarito)