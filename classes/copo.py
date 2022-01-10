# -*- coding: utf-8 -*-

from classes.recipient import Recipient



class Copo(Recipient):
    def __init__(self, tamanho=0, conteudo=0, limpo=True):
        super().__init__(tamanho=tamanho, conteudo=conteudo, limpo=limpo)
        self.tamanho = tamanho        
    
    def encher(self, bebida = 'água'):
        if(self.limpo == True):
            self.limpo = False
            self.conteudo = self.tamanho
            self.bebida = bebida
        if(self.limpo == False):
            return 'Não se pode encher um copo sujo'

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


    def __repr__(self) :
        return f'Um %s vazio de %s.0ml' % ((Copo.__name__).lower(), self.tamanho)


    # def __str__(self):
    #     return f"Um recipiente {self.estado()} não especificado"