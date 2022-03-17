
import random

'''
Classe responsável por controlar a mutação de um filho
'''
class GeradorMutacao:

    def __init__(self, qtdGenesFilho):
        self.__qtdGenesFilho = qtdGenesFilho


    # Gera a mutação de um filho
    def getFilhoComMutacao(self, filho):
        posAleatoriaX = 0
        posAleatoriaY = 0

        while(posAleatoriaX == posAleatoriaY):
            posAleatoriaX = random.randint(0, self.__qtdGenesFilho-1)
            posAleatoriaY = random.randint(0, self.__qtdGenesFilho-1)

        #Gerando a mutacao
        backupPosX = filho.arrayCidades[posAleatoriaX]
        filho.arrayCidades[posAleatoriaX] = filho.arrayCidades[posAleatoriaY]
        filho.arrayCidades[posAleatoriaY] = backupPosX

        return filho