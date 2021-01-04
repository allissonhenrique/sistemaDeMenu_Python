#from interface import*
from arquivo import *
from time import sleep

arq = 'páginaDeCadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas',  'Sair do Sistema'])
    if resposta ==1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção de sair do sistema.
        cabeçalho('Sair do Sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)