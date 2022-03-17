
import numpy as np
import matplotlib.pyplot as plt

'''
Classe que exibe o gráfico
'''
class InterfaceGrafica:

    def __init__(self, populacao):
        self.populacao = populacao
        self.populacaoItens = self.populacao.getItens()
        self.populacaoMatriz = self.__converterParaMatriz(self.populacaoItens)
        self.matrizDistancias = self.populacao.matrizDistancias


    #Exibe o gráfico
    def exibir(self):
        vetor_trajeto_x = np.zeros(21, dtype=np.float64)
        vetor_trajeto_y = np.zeros(21, dtype=np.float64)

        for i in range(0, 20):
            vetor_trajeto_x[i] = self.matrizDistancias[0, int(self.populacaoMatriz[0, i] - 1)].coordenadaX
            vetor_trajeto_y[i] = self.matrizDistancias[0, int(self.populacaoMatriz[0, i] - 1)].coordenadaY

        vetor_trajeto_x[20] = self.matrizDistancias[0, int(self.populacaoMatriz[0, 0] - 1)].coordenadaX
        vetor_trajeto_y[20] = self.matrizDistancias[0, int(self.populacaoMatriz[0, 0] - 1)].coordenadaY

        plt.figure(3)
        plt.plot(vetor_trajeto_x, vetor_trajeto_y)
        # label do eixo x
        plt.xlabel('Distância X')
        # label do eixo y
        plt.ylabel('Distância Y')
        # label do título
        plt.title("Melhor caminho encontrado pelo Algoritmo Genético")

        plt.show(block = True)
        plt.clf()


    #Converte a lista de cromossomos para uma matriz
    def __converterParaMatriz(self, cromossomos):
        qtdItens = len(cromossomos)
        matrizResult = np.array([[0 for x in range(qtdItens)] for y in range(qtdItens)])


        for item in cromossomos:
            indexItem = item.index
            arrayCidades = item.arrayCidades

            for index in range(0, len(item.arrayCidades)):
                matrizResult[indexItem, index] = arrayCidades[index]


        return matrizResult