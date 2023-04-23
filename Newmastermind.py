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
