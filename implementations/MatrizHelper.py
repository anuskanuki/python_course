
from models import PopulacaoItem as popItem
from models import PopulacaoListItens as popList
import numpy as np

'''
Classe que auxilia na geração de matrizes
'''
class MatrizHelper:

    # Duplica a primeira coluna e retorna uma nova população
    def gerarPopulacoComUltimaColunaDaMatrizCopiaDaPrimeira(self, listaPopulacaoItens):

        linhas = len(listaPopulacaoItens)
        colunas = len(listaPopulacaoItens[0].arrayCidades) + 1  # Incrementando para gerar uma coluna a mais

        listaDeItensDaPopulacao = popList.PopulacaoListItens(linhas, colunas)


        for item in listaPopulacaoItens:
            index = item.index
            novoArrayCidades = np.zeros(colunas, dtype=int)
            for i in range(0, colunas):
                if(i == colunas-1):
                    novoArrayCidades[i] = item.arrayCidades[0]
                    index += 1
                else:
                    novoArrayCidades[i] = item.arrayCidades[i]

            listaDeItensDaPopulacao.addItem(popItem.PopulacaoItem(novoArrayCidades, index))

        return listaDeItensDaPopulacao.getItens()
