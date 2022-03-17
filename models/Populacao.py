
import random
import numpy as np
from models import PopulacaoListItens as popList
from implementations import GeradorMatrizDistancias as gen
from implementations import MatrizHelper as matHelp
from implementations import GeradorMutacao as genMut
from implementations import GeradorFilhos as genFil

"""
Classe para representar a população
    (Analogia: "Array/Lista de cromossomos")
    Objeto responsável por criar e representar uma população de algoritmo genético.
"""
class Populacao:

    def __init__(self):
        self.numeroItensPopulacao = 20
        self.__matrizHelpder = matHelp.MatrizHelper()
        self.__geradorMutacao = genMut.GeradorMutacao(self.numeroItensPopulacao)
        self.__geradorFilhos = genFil.GeradorFilhos(self.numeroItensPopulacao)
        self.geradorMatrizDistancias = gen.GeradorMatrizDistancias(self.numeroItensPopulacao)
        self.matrizDistancias = self.geradorMatrizDistancias.gerarMatrizDistancias()
        self.__PopulacaoListItens = popList.PopulacaoListItens(self.numeroItensPopulacao, self.numeroItensPopulacao)
        self.__itens = []


    #Cria a população
    def criar(self):
        self.__PopulacaoListItens.criar()
        self.__itens = self.__PopulacaoListItens.getItens()


    #Exibe todos os itens da população
    def exibir(self):
        print("População:")
        self.__PopulacaoListItens.exibir()
        print()


    #Adiciona um item na população
    def __addItem(self, populacaoItem):
        self.__PopulacaoListItens.addItem(populacaoItem)


    #Seta os itens da população
    def __setItens(self, novosItens):
        self.__PopulacaoListItens.setItens(novosItens)
        self.__itens = self.__PopulacaoListItens.getItens()


    #Seta a distância de um item da população
    def __addDistancia(self, index, distancia):
        self.__PopulacaoListItens.addDistancia(index, distancia)
        self.__itens = self.__PopulacaoListItens.getItens()


    #Retorna o item com melhor aptidão da população
    def getMelhor(self):
        return self.__itens[0]


    #Retorna todos os itens da população
    def getItens(self):
        return self.__itens;


    #Executa a função de aptidão
    def executarFuncaoAptidao(self):
        qtdItens = self.numeroItensPopulacao

        '''
        Criação de uma matriz 20x21 da populacao onde a ultima coluna é a copia da primeira coluna (o agente deve voltar a cidade inicial)
        Obs: Será utilizada para calcular as distâncias
        '''
        tour = self.__matrizHelpder.gerarPopulacoComUltimaColunaDaMatrizCopiaDaPrimeira(self.__itens)

        #Percorrendo matriz tour para definir a distância(aptidão) de cada item
        for index in range(0, qtdItens):
            if(self.__itens[index].distancia == 0):
                item = tour[index]
                self.__addDistancia(index, self.__getSomaDistancias(item, self.matrizDistancias))



    #Soma as distâncias usando o Tour para obter a distância total do cromossomo
    def __getSomaDistancias(self, item, matrizDistancias):
        distancia = 0
        copiaItensArrayCidade = np.copy(item.arrayCidades).tolist()

        while len(copiaItensArrayCidade) != 0:

            cidadeAtual = copiaItensArrayCidade[0]
            copiaItensArrayCidade.remove(cidadeAtual)

            cidadeProxima = copiaItensArrayCidade[0]
            if(len(copiaItensArrayCidade) != 2):
                copiaItensArrayCidade.remove(cidadeProxima)

            distancia += matrizDistancias[cidadeAtual-1, cidadeProxima-1].distancia

        return round(distancia, 5)


    #Ordena os itens da população em ordem crescente
    def ordenarPelaDistanciaDesc(self):
        self.__itens.sort(key=lambda x: x.distancia, reverse=False)


    #Mantém apenas a metade dos melhores itens da população na lista.
    def manterMetadeMelhores(self):
        metade = int(len(self.__itens) / 2)
        novaLista = self.__itens[:metade]
        self.__setItens(novaLista)


    #Método responsável por gerar novos filhos para a população
    def gerarNovosFilhos(self):
        qtdVetorItens = int(len(self.__itens) / 2)

        roleta = self.__gerarRoletaPais()
        escolhas = self.__gerarEscolhas(roleta)

        escolha1 = escolhas[0]
        escolha2 = escolhas[1]

        for index in range(0, qtdVetorItens):
            paiXAleatorio = roleta[escolha1[index]]
            paiYAleatorio = roleta[escolha2[index]]

            result = self.__geradorFilhos.gerarDoisNovosFilho(paiXAleatorio, paiYAleatorio)

            #Gerar mutação para todos os filhos gerados sempre
            filho1 = self.__gerarMutacao(result[0])
            filho2 = self.__gerarMutacao(result[1])

            self.__addItem(filho1)
            self.__addItem(filho2)


    #Método responsável por efetuar a mutação em um filho
    def __gerarMutacao(self, filho):
        filho = self.__geradorMutacao.getFilhoComMutacao(filho)
        return filho


    #Método responsável por gerar a roleta de pais,
    # visando uma melhor % de o melhor pai ser escolhido
    def __gerarRoletaPais(self):
        copiaLista = np.copy(self.__itens).tolist()
        listaRoleta = []

        qtdVezesIncluir = 1
        for index in range(len(copiaLista)-1, -1, -1):
            for indexInc in range(0, qtdVezesIncluir):
                listaRoleta.append(copiaLista[index])
            qtdVezesIncluir += 1

        return np.array(listaRoleta)


    #Gera vetor de escolhas para usar no crossover
    def __gerarEscolhas(self, roleta):
        qtdItensRoleta = len(roleta) - 1
        qtdVetorItens = int(len(self.__itens) / 2)
        vetorResult1 = np.zeros(qtdVetorItens, dtype=int)
        vetorResult2 = np.zeros(qtdVetorItens, dtype=int)

        for index in range(0, qtdVetorItens):
            num1 = random.randint(0, qtdItensRoleta)
            num2 = random.randint(0, qtdItensRoleta)

            while num1 == num2:
                num1 = random.randint(0, qtdItensRoleta)
                num2 = random.randint(0, qtdItensRoleta)

            vetorResult1[index] = num1
            vetorResult2[index] = num2

        return [vetorResult1, vetorResult2]