
from models import Populacao as pop
from presentation import InterfaceGrafica as interface

"""
Classe principal do sistema
"""
class MainClass:

    def __init__(self, numeroIteracoes):
        self.numeroIteracoes = numeroIteracoes


    def exibir(self, iteracao, melhorItem):
        print("iteracao: " + str(iteracao) + " Melhor item: '" + str(melhorItem) + "'")

    def run(self):
        populacao = pop.Populacao()
        # Criando população 20x20 (20 cromossomos onde cada um possui 20 genes)
        populacao.criar()

        #Iterando a populacao
        for iteracao in range(0, self.numeroIteracoes):
            #Rodar a função de aptidão para cada cromossomo (vai percorrer 20 vezes neste ponto)
            populacao.executarFuncaoAptidao()

            #Ordenar resultado da função de aptidão por ordem de distância
            populacao.ordenarPelaDistanciaDesc()

            #Pegar os 10 cromossomos que possuem menor distância (Serão os 10 melhores)
            populacao.manterMetadeMelhores()

            #Exibe o melhor item na iteração atual
            self.exibir(iteracao, populacao.getMelhor())

            #Os 10 melhores irão gerar 10 novos filhos (gerando um total de 20 cromossomos)
            populacao.gerarNovosFilhos()

        print()
        print()
        #Gerar detalhes finais em linha de comando
        print("Tamanho da População: " + str(populacao.numeroItensPopulacao))
        print("Taxa de Mutação: 100%")
        print("Número de Cidades: " + str(len(populacao.getMelhor().arrayCidades)))
        print("Melhor Custo : " + str(populacao.getMelhor().distancia))
        print("Melhor Solução: " + str(populacao.getMelhor().exibirArrayCidades()))

        inter = interface.InterfaceGrafica(populacao)
        inter.exibir()

#Número de iterações do algoritmo
numeroIteracoes = 10000

#Execução da classe principal
mainClass = MainClass(numeroIteracoes)
mainClass.run()