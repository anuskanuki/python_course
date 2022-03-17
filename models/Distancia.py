
import numpy as np

'''
Classe responsável por gerar uma coordenada única para cada cidade presente na população.
'''
class Distancia:

    def __init__(self, coordenadaX, coordenadaY, distancia = 0):
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.distancia = distancia

    def __str__(self):
        return "(" + str(self.coordenadaX) + "," + str(self.coordenadaY) + ") " + str(self.distancia)