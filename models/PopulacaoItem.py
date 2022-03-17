"""
Classe para representa um item do cromossomo
    Analogia: ("Array de genes")
    Neste trabalho, um gene é uma cidade, que seria um dos caminhos que devem ser percorridos pelo caixeiro viajante.
"""


class PopulacaoItem:

    def __init__(self, arrayCidades, index = 0):
        self.index = index
        self.arrayCidades = arrayCidades
        # resultado do cálculo de aptidão
        self.distancia = 0


    def __str__(self):
        value = str(self.index)
        if(self.index < 10):
            value = "0" + str(self.index)
        return value + " - " + str(self.arrayCidades) + " - Distância: " + str(self.distancia)


    #Exibe apenas as cidades(genes)
    def exibirArrayCidades(self):
        result = ""
        for index in range(0, len(self.arrayCidades)):
            if(index == len(self.arrayCidades)-1):
                result += str(self.arrayCidades[index])
            else:
                result += str(self.arrayCidades[index]) + ", "

        return result