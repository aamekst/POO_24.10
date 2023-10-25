'''
Implemente os métodos da classe Fila, definidos abaixo.
'''


class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
       return self.itens.append(item)

    def desenfileirar(self):
        return self.itens.pop(0)

    def tamanho(self):
        return len(self.itens)
         

    def vazia(self):
        if len(self.itens) ==0:
            return True
        else:
            return False
     
        
    def primeiro(self):
        return self.itens[0]
        

    def exibir(self):
        print(self.itens)


# Programa principal
fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(5)
fila.enfileirar(10)

fila.exibir()               # [1, 2, 5, 10]
print(fila.tamanho())       # 4
print(fila.vazia())         # False
print(fila.primeiro())      # 1

fila.desenfileirar() #tiras os primeiro
item = fila.desenfileirar()
print('-'*34)
print(item)                 # 5
fila.exibir()               # [10]
print(fila.tamanho())       # 1
print(fila.vazia())         # False
print(fila.primeiro())      # 10


fila.enfileirar(4)
fila.enfileirar(20)

print('-'*34)
fila.exibir()               # [10, 4, 20]
print(fila.tamanho())       # 3
print(fila.vazia())         # False
print(fila.primeiro())      # 10

fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
print('-'*34)
print(fila.tamanho())       # 0
print(fila.vazia())         # True