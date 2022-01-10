# -*- coding: utf-8 -*-

class Recipient():
    def __init__(self, tamanho = 0, conteudo = 0, limpo = True):
        if(tamanho < 0):
            self.tamanho = 0    
        else:
            self.tamanho = tamanho
        self.conteudo = conteudo
        self.limpo = limpo
    
    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        if (self.conteudo <= 0):
            return True
        else:
            return False
        
    def lavar(self):
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self):
        return self.limpo
        
    
    def estado(self):
        if (self.limpo):
            return 'limpo'
        else: 
            return 'sujo'
    
    def sujar(self):
        self.limpo = False


    def __repr__(self) :
        return f'Um %se %s não especificado' % ((Recipient.__name__).lower(), self.estado())

    # def __str__(self):
    #     return f"Um recipiente {self.estado()} não especificado"

    # __str__/__repr__: Ambos os métodos devem retornar uma mensagem
    #  representando o estado do recipiente dicamicamente, seguindo o exemplo abaixo.