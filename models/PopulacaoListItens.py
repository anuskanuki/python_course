

from models import PopulacaoItem as popItem
import numpy as np
import random

'''
Classe que auxilia na geração e controle de itens da população
'''
class PopulacaoListItens:

    def __init__(self, qtdItens, qtdItensArrayCidades):
        self.__numeroAleatorioMinimo = 1
        self.__numeroAleatorioMaximo = 20
        self.__qtdItens = qtdItens
        self.__qtdItensArrayCidades = qtdItensArrayCidades
        self.__itens = []


    #Adiciona um item na população
    def addItem(self, populacaoItem):
        if (populacaoItem is None):
            raise Exception("populacaoItem não pode ser nulo")
        self.__itens.append(populacaoItem)
        self.__resequenciarIndicesDaLista()


    #Seta os itens da população
    def setItens(self, populacaoItens):
        if (populacaoItens is None):
            raise Exception("populacaoItens não pode ser nulo")
        self.__itens = populacaoItens
        self.__resequenciarIndicesDaLista()


    #Seta a distância da população
    def addDistancia(self, index, distancia):
        self.__itens[index].distancia = distancia


    #Retorna os itens da população
    def getItens(self):
        return self.__itens


    #Exibe os itens da população
    def exibir(self):
        for item in self.__itens:
            print(item)


    #Método serve somente para organização dos indices da lista
    def __resequenciarIndicesDaLista(self):
        newIndex = 0
        for item in self.__itens:
            item.index = newIndex
            newIndex += 1


    #Cria a população
    def criar(self):
        for index in range(0, self.__numeroAleatorioMaximo):
            arrayCidades = self.__criarArrayItensUnico()
            populacaoItem = popItem.PopulacaoItem(arrayCidades, index)
            self.addItem(populacaoItem)


    # Cria o vetor de cidades da população (genes)
    def __criarArrayItens(self):
        listaAleatoria = np.arange(self.__numeroAleatorioMinimo, self.__numeroAleatorioMaximo + 1, 1).tolist()
        listaItens = []

        while ((len(listaItens) < self.__qtdItens) and (len(listaAleatoria) != 0)):
            numeroAleatorio = random.choice(listaAleatoria)
            if not (numeroAleatorio in listaItens):
                listaItens.append(numeroAleatorio)
                listaAleatoria.remove(numeroAleatorio)

        array = np.array(listaItens)
        return array


    #Cria e garante que o vetor de cidades é único
    def __criarArrayItensUnico(self):
        arrayItens = self.__criarArrayItens()

        while(self.__itemJaExisteNaPopulacao(arrayItens)):
            arrayItens = self.__criarArrayItens()

        return arrayItens


    #Verifica se a sequência de genes já existem na população
    def __itemJaExisteNaPopulacao(self, arrayItens):
        estaNaLista = False
        arrayItensString = str(arrayItens)

        for item in self.__itens:
            if(str(item) == arrayItensString):
                estaNaLista = True
                break

        return estaNaLista