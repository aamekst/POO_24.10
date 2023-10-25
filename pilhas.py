#fila - o primeiro a entra é o primeiro a sair 
#o numero é colocado no final da fila 
#remove o primeiro numero

#pilha insere e remove no final
#o ultimo a ser inserido é o primeiro a ser removido
'''Em Filas, temos inserção no final e remoção do início (extremos opostos da estrutura)
Em Pilhas, temos a inserção no final e remoção no final (mesmo extremo da estrutura)
'''
'''
Implemente os métodos da classe Pilha, definidos abaixo.
'''


class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        return self.itens.append(item)

    def desempilhar(self):
        return self.itens.pop(-1)
    #return self.itens.pop(-1)
       

    def tamanho(self):
        '''Retorna a quantidade de itens na pilha'''
        return len(self.itens)
        

    def vazia(self):
        if len(self.itens) ==0:
            return True
        else:
            return False
        

    def topo(self):
        '''Retorna o item do topo da pilha sem remove-lo da pilha'''
        return self.itens[-1]


    def exibir(self):
        print(self.itens)


# Programa principal
pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(5)
pilha.empilhar(10)
print('-'*40)
pilha.exibir()              # [1, 2, 5, 10]
print(pilha.tamanho())      # 4
print(pilha.vazia())        # False
print(pilha.topo())         # 10

pilha.desempilhar()# tira os ultimos
pilha.desempilhar()
item = pilha.desempilhar()
print('-'*40)
print(item)                 # 2
pilha.exibir()              # [1]
print(pilha.tamanho())      # 1
print(pilha.vazia())        # False
print(pilha.topo())         # 1


pilha.empilhar(4)
pilha.empilhar(20)
print('-'*40)
pilha.exibir()              # [1, 4, 20]
print(pilha.tamanho())      # 3
print(pilha.vazia())        # False
print(pilha.topo())         # 20

pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print('-'*40)
print(pilha.tamanho())       # 0
print(pilha.vazia())         # True