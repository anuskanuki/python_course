
import random
import numpy as np
from models import Distancia as dis

'''
Classe responsável por gerar a matriz de distâncias.
'''
class GeradorMatrizDistancias:
    random_min_value = 0.0
    random_max_value = 1.0
    decimals = 5

    def __init__(self, ordem):
        self.ordem = ordem
        self.matrizDistancias = []


    # Gera a matriz de distâncias, usada no cálculo da distância entre as cidades
    def gerarMatrizDistancias(self):

        matrizResult = np.full((self.ordem, self.ordem), dis.Distancia(0, 0))

        '''
        Percorrendo matriz para preencher as distâncias entre as cidades com base nos números aleatórios gerados.
        Observações: 
                    A distância entre a cidade X até a Y deve ser a mesma quando efetuado o caminho inverso (Y até X);
                    Diagonal principal fica com valores zerados, pois a distância entre um ponto até ele mesmo é zero;
        '''

        for linha in range(0, self.ordem):
            for coluna in range(0, self.ordem):
                # Se não for coluna principal
                if (linha != coluna):
                    coordenadaX = GeradorMatrizDistancias.getRandomNumber()
                    coordenadaY = GeradorMatrizDistancias.getRandomNumber()
                    distanciaValor = self.__calcularDistancia(coordenadaX, coordenadaY)

                    matrizResult[linha, coluna] = dis.Distancia(coordenadaX, coordenadaY, distanciaValor)
                    matrizResult[coluna, linha] = dis.Distancia(coordenadaY, coordenadaX, distanciaValor)

        self.matrizDistancias = matrizResult

        return matrizResult


    #Calcula a distância
    def __calcularDistancia(self, coordenadaX, coordenadaY):
            return self.__getResultadoFormula(coordenadaX, coordenadaY)


    # Aplica a fórmula de cálculo de aptidão para definir a distância
    def __getResultadoFormula(self, coordenadaX, coordenadaY):
        potencia = (coordenadaX + coordenadaY) ** 2
        result = np.sqrt(abs(potencia))
        return round(result, self.decimals)


    #Retorna vetor contendo valores aleatórios
    def __getValoresAleatorios(self, ordem):
        result = np.zeros(ordem)

        for index in range(0, self.ordem):
            result[index] = GeradorMatrizDistancias.getRandomNumber()

        return result


    #Retorna um valor aleatório
    @classmethod
    def getRandomNumber(cls, minValue = 0, maxValue = 0, decimals = 0):
        if(minValue == 0 and maxValue == 0 and decimals == 0):
            return round(random.uniform(cls.random_min_value, cls.random_max_value), cls.decimals)
        else:
            return round(random.uniform(minValue, maxValue), decimals)
