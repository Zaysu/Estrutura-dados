class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0
    
    def inserir_elemento_posicao(self, elemento, posicao):
        self.__elementos[posicao] = elemento
        
    def inserir_elememento_final(self, elemento):
        if self.__posicao >= len(self.__elementos):
            self.__elementos = self.__elementos + [None]
            
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1
        
    def listar_elemtento(self, posicao):
        return self.__elementos[posicao]