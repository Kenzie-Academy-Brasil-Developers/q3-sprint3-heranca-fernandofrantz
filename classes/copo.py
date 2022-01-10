# -*- coding: utf-8 -*-

from classes.recipient import Recipient

class Copo(Recipient):
    def __init__(self, tamanho):
        self.tamanho = tamanho
    
    def encher(self, bebida = 'água'):
        if(self.limpo == True):
            self.limpo = False
            self.conteudo = self.tamanho
            self.bebida = bebida
        if(self.limpo == False):
            return 'Não se pode encher um copo sujo.'

    def beber(self, quantidade):
        if(quantidade < 0):
            return 'Quantidade deve ser positiva'
        elif(quantidade > self.conteudo):
            return 'Não há bebida suficiente no copo'
        else: 
            self.conteudo -= quantidade
        
    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True


# __str__/__repr__: Ambos os métodos devem retornar uma mensagem
#  representando o objeto Copo:
