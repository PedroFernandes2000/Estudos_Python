import math

print('Hello World!')
nome = input('Qual é o seu nome? ')
print('Olá',nome,'seja bem vindo ao curso de Python')

def hello(): 
    print('olá')



def ex1():
    print('Hello World!')
    i = input('nome? ')
    print('tamo junto d++ {:-^20}!'.format(i))
    
def ex2():
    n1 = int(input('digite um numero '))
    n2 = int(input('digite outro numero '))
    s = n1 + n2
    print('a soma entre {} e {} é {}'.format(n1, n2, s))
# A formatação usando {} (chaves) se assemelha ao %i ou %c da linguagem 
# antes do "format()" é . (*PONTO*) não é , (virgula)
def ex3():
    n1 = input('akjcscb? ')
    print(' isalpha() = {} \n isnumeric() = {} \n isalnum() = {} \n isupper() = {} \n isdigit() = {}'.format(n1.isalpha(), n1.isnumeric(), n1.isalnum(), n1.isupper() , n1.isdigit()))
    
    
def ex4():
    i = float(input('escreve um numero ai mlk '))
    print(' {} ^ 2 = {} \n raiz de {} = a {} '.format(i,i**2,i,math.sqrt(i)))
