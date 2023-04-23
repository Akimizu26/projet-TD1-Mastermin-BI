#Ici on va importer toutes les libraires dont on a besoin pour le projet
import tkinter as tk
import random
import json

#On donne un nom à notre fenêtre principale et on la dimensionne
PATH = "data.json"

NB_OF_GUESS = 11
TMP = NB_OF_GUESS
CODE_LENGTH = 4
COLOR_SIZE = 40
COLOR_PADDING = 50

WIDTH = CODE_LENGTH*90
HEIGHT = NB_OF_GUESS*55+70

NB_PLAYER = 1
CODED_MESSAGE = []

#On donne le nom des couleurs pour le jeu
basecolors = ['white','green','red','maroon1','gold','dark orange','dodger blue']
color_indice = ['black','white']

color_button = "#613a19"
position = 0


row = 0
cpos = 0

selectColors = []

colorpicks = [[-1 for i in range(CODE_LENGTH)] for j in range(NB_OF_GUESS)]
indice = [[-1 for i in range(CODE_LENGTH)] for j in range(NB_OF_GUESS)]

