import random
import numpy as np
from collections import Counter
from models import PopulacaoItem as popItem

'''
Classe responsável por efetuar a geração de dois novos filhos com base em dois pais
'''
class GeradorFilhos:

    def __init__(self, numeroGenes):
        self.__numeroGenes = numeroGenes


    #Método responsável pela geração de novos filhos
    def gerarDoisNovosFilho(self, x, y):
        paiX = popItem.PopulacaoItem(x.arrayCidades).arrayCidades.tolist()
        paiY = popItem.PopulacaoItem(y.arrayCidades).arrayCidades.tolist()

        # Aplicar crossover com técnica “cycle”
        # Selecionar um local aleatório dentro do cromossomo
        posicaoAleatoriaDentroDoCromossomo = self.__obterPosicaoAleatoriaDentroDoCromossomo(paiX, paiY)

        # Passo1: Os dois cromossomos pais trocam os números inteiros neste local para gerar os descendentes.
        # Valores trocados não podem ter o mesmo valor
        # Trocando os valores na posição aleatória para gerar dois descendentes
        self.__efetuarTrocaDeValores(paiX, paiY, posicaoAleatoriaDentroDoCromossomo)

        descendente1 = paiX
        descendente2 = paiY

        # Passo2: Em seguida, mudamos o número duplicado da primeira descendência com o
        # mesmo local do número da segunda descendência
        # Passo 3 e 4: Isto significa que temos agora outro número duplicado, então repita este
        # processo até não terem mais números duplicados.
        pocisaoDentroDoCromossomo = posicaoAleatoriaDentroDoCromossomo

        while self.__existeGeneDuplicado(descendente1):
            repetido = list((Counter(descendente1) - Counter(set(descendente1))).keys())[0]
            indiceRepetido = self.__obterIndiceQueNaoFoiTrocado(repetido, descendente1, pocisaoDentroDoCromossomo,
                                                                self.__numeroGenes)

            self.__efetuarTrocaDeValores(descendente1, descendente2, indiceRepetido)
            pocisaoDentroDoCromossomo = indiceRepetido

        self.__validarCrossoverComSucesso(descendente1, descendente2)
        return [popItem.PopulacaoItem(np.array(descendente1)), popItem.PopulacaoItem(np.array(descendente2))]


    # Verifica se houve algum erro na troca de valores(genes) entre os cromossomos
    def __existeGeneDuplicado(self, elemento):
        return [item for item, count in Counter(elemento).items() if count > 1]


    # Efetua a troca de valores entre os descendentes
    def __efetuarTrocaDeValores(self, paiX, paiY, posicao):
        backupPosicaoX = paiX[posicao]
        paiX[posicao] = paiY[posicao]
        paiY[posicao] = backupPosicaoX


    # Aplica a roleta para definir uma posição aleatória dentro do cromossomo que será usada para a troca dos valores
    def __obterPosicaoAleatoriaDentroDoCromossomo(self, array1, array2):
        indiceMaximoValido = self.__numeroGenes - 1
        result = random.randint(0, indiceMaximoValido)

        return result


    # Obtém o índice do elemento que está repetido, sem considerar o valor tracado na última iteracao
    def __obterIndiceQueNaoFoiTrocado(self, repetido, descendente, posicaoAleatoriaDentroDoCromossomo, numeroGenes):
        for index in range(0, numeroGenes):
            valor = descendente[index]
            if valor == repetido and index != posicaoAleatoriaDentroDoCromossomo:
                return index


    def __validarCrossoverComSucesso(self, elemento1, elemento2):
        if (self.__existeGeneDuplicado(elemento1) or self.__existeGeneDuplicado(elemento2)):
            mensagem = "Houve um erro no crossover:\nCromossomos:"
            mensagem = mensagem + str(elemento1) + "\n"
            mensagem = mensagem + str(elemento2) + "\n"
            raise Exception(mensagem)
