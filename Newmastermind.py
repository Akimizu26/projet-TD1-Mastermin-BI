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

#Dans cette fonction on va donner a nos touches des "attributions"
def userAction():
    CANVAS.unbind('<space>')
    CANVAS.bind('<Left>', lambda _: selectPos(-1))
    CANVAS.bind('<Right>', lambda _: selectPos(1))
    CANVAS.bind('<Up>', lambda _: switchColor(1))
    CANVAS.bind('<Down>', lambda _: switchColor(-1))
    CANVAS.bind('<Return>', lambda _: switchrow())

# Ici on va retirer les attributions des touches
def userInAction():
    CANVAS.unbind("<Left>")
    CANVAS.unbind("<Right>")
    CANVAS.unbind("<Up>")
    CANVAS.unbind("<Down>")
    CANVAS.unbind("<Return>")

# voici le code pour la fenêtre de jeu à un joueur
def create_code_one_player():
    selection = [x for x in range(len(basecolors))]
    code = []
    for _ in range(CODE_LENGTH):
        codeIndex = random.randint(0,len(selection)-1)
        code.append(selection[codeIndex])
        selection.pop(codeIndex)
    return code

#voici le code pour la fenêtre de jeu à deux joueurs
def initRow():
    global selectColors,tops, bots
    selectColors = [x for x in range(len(basecolors))]
    tops = 0
    bots = 0


#voici le code pour initialiser le jeu (la partie)
def initGame(board, response):
    global row, cpos, colorpicks, codedColor, NB_PLAYER
    CANVAS.itemconfig(board[row][cpos],width=1)
    userAction()
    if NB_PLAYER == 1:
        codedColor = create_code_one_player()
    initRow()
 #voici le code pour pour selectionner le petit rond     
def select(colorPosition):
    CANVAS.itemconfig(colorPosition, width=5)
#voici le code pour désélectionner le petit rond
def deselect(colorPosition):
    CANVAS.itemconfig(colorPosition, width=0)

# ici ce code permet de changer la couleur du petit rond (on va la définir)
def setcolor(colorPosition,color):
    CANVAS.itemconfig(colorPosition, fill=color)

#ce code permet de selectionner la position du petit rond
def selectPos(increment):
    global cpos
    CANVAS.itemconfig(board[row][cpos],width=0)
    cpos += increment
    if cpos < 0:
        cpos = CODE_LENGTH-1
    if cpos >= CODE_LENGTH:
        cpos = 0
    CANVAS.itemconfig(board[row][cpos],width=1)

#pour switch entre plusieurs couleurs on peut passer d'une a l'autre
def switchColor(increment):
    colorpicks[row][cpos] += increment
    if colorpicks[row][cpos] > len(basecolors)-1:
        colorpicks[row][cpos] = 0
    if colorpicks[row][cpos] < 0:
        colorpicks[row][cpos] = len(basecolors)-1
    CANVAS.itemconfig(board[row][cpos], fill=basecolors[colorpicks[row][cpos]])

#cette fonction est la base du programme , elle permet de verifier la compinaison de couleurs choisi esi elle concorde avec la combinaison de couleurs du code
def switchrow():
    global row, tops, bots, colorpicks, codedColor, indice
    tops, bots = 0, 0
    if NB_OF_GUESS == 1:
            codedColor = colorpicks.copy()[0]
            colorpicks[0] = [-1 for i in range(CODE_LENGTH)]
            FRAME.destroy()
            select_un_joueur()
            return
    utilise = []
    compteur = 0
    for i in range(CODE_LENGTH):
        if colorpicks[row][i] == -1:
            print(f"Colors not set {row},{i}:")
            return False
        if (codedColor[i]==colorpicks[row][i]): #bien placé
            indice[row][compteur] = 0
            compteur += 1
            tops += 1
            utilise.append(i)
    for i in range(CODE_LENGTH):
        for j in range(CODE_LENGTH):
            if (j!=i and codedColor[j]==colorpicks[row][i] and j not in utilise):
                indice[row][compteur] = 1
                compteur += 1
                bots += 1
                utilise.append(j)
                break
        
    if tops < CODE_LENGTH and row < NB_OF_GUESS-2:
        print(f"tops:{tops}, bots:{bots}")
        for i in range(tops):
            CANVAS.itemconfig(response[row][i], fill="black")
        for i in range(bots):
            CANVAS.itemconfig(response[row][i+tops], fill="white")
        CANVAS.itemconfig(board[row][cpos],width=0)
        row += 1
        CANVAS.itemconfig(board[row][cpos],width=1)
        initRow()
        return False
    else:
        print(f"Row{row} tops{tops} and bots{bots}")
        print(response, codedColor, colorpicks)
        output = True
        if row == NB_OF_GUESS-2:
            output = False
        for i in range(tops):
            print(row, i)
            CANVAS.itemconfig(response[row][i], fill="black")
        #for i in range(bots):
        #    print(row, i, tops)
        #    CANVAS.itemconfig(response[row][i+tops], fill="white")
        for i in range(CODE_LENGTH):
            CANVAS.itemconfig(board[NB_OF_GUESS-1][i], fill=basecolors[codedColor[i]])
        userInAction()
        CANVAS.bind("<space>", lambda _: initGame(board, response))
        return output

#voici le code pour le mode un joueur il s'agit de la fonction select_un_joueur qui va créer la fenêtre et le canvas
def drawBoard():
    global colorpicks, indice
    print(indice)
    board = []
    response = []
    button_annuler = tk.Button(FRAME, text="Annuler", command=annuler, bg=color_button, fg="#ffffff")
    button_sauvegarde = tk.Button(FRAME, text="Sauvegarder", command=sauvegarder, bg=color_button, fg="#ffffff")
    button_annuler.place(x=10, y=10)
    button_sauvegarde.place(x=100, y=10)
    for i in range(NB_OF_GUESS):
        newRow = []
        newResponse = []
        for j in range(CODE_LENGTH):
            x = COLOR_PADDING*j+5
            y = HEIGHT - COLOR_PADDING*i - COLOR_SIZE - 5
            if colorpicks[i][j] == -1:
                newRow.append(CANVAS.create_oval(x,y,x+COLOR_SIZE,y+COLOR_SIZE,fill=color_button,outline='black',width=0))
            else:
                print(basecolors[colorpicks[i][j]])
                newRow.append(CANVAS.create_oval(x,y,x+COLOR_SIZE,y+COLOR_SIZE,fill=basecolors[colorpicks[i][j]],outline='black',width=0))
            if i < NB_OF_GUESS-1:
                x = COLOR_PADDING/2*j+CODE_LENGTH*COLOR_PADDING+20
                y += COLOR_SIZE/8
                if indice[i][j] == -1:
                    newResponse.append(CANVAS.create_oval(x+ COLOR_SIZE/4, y+ COLOR_SIZE/4, x + COLOR_SIZE/2, y + COLOR_SIZE/2, fill=color_button, outline='black', width=0))
                else:
                    newResponse.append(CANVAS.create_oval(x+ COLOR_SIZE/4, y+ COLOR_SIZE/4, x + COLOR_SIZE/2, y + COLOR_SIZE/2, fill=color_indice[indice[i][j]], outline='black', width=0))
        board.append(newRow)
        if i < NB_OF_GUESS - 1:
            response.append(newResponse)
    initGame(board, response)
    CANVAS.itemconfig(board[row][cpos],width=1)
    return board, response

# voici le code qui permet d'annuler la partie en cours 
def annuler():
    global board, response, row, CANVAS, colorpicks, indice
    if row == 0:
        return
    for i in range(CODE_LENGTH):
        CANVAS.itemconfig(board[row][i], fill=color_button, width=0)
        CANVAS.itemconfig(response[row][i], fill=color_button)
        colorpicks[row][i] = -1
        indice[row][i] = -1
    row -= 1
    for i in range(CODE_LENGTH):
        CANVAS.itemconfig(board[row][i], fill=color_button)
        CANVAS.itemconfig(response[row][i], fill=color_button)
        colorpicks[row][i] = -1
        indice[row][i] = -1
    
    
#Voici le code qui permet de sauvegarder la partie
def sauvegarder():
    global colorpicks, codedColor, indice, row
    data = {}
    with open(PATH, 'w') as f:
        data['sequence_couleur'] = colorpicks
        data["resultat"] = codedColor
        data["indice"] = indice
        data["row"] = row
        json.dump(data, f)

#Voici le code qui permet de restaurer la partie        
def restorer():
    global colorpicks, codedColor, indice, row
    with open(PATH, 'r') as f:
        data = json.load(f)
        colorpicks = data['sequence_couleur']
        codedColor = data['resultat']
        indice = data['indice']
        row = data['row']
    select_un_joueur()

#ici ce code permet de selectionner entre le mode un seul et deux joueurs 
def selection_joueur():
    fenetre = tk.Frame(ROOT, width=200, height=100)
    un_joueur = tk.Button(fenetre, text="1 joueur", command=select_un_joueur)
    deux_joueur = tk.Button(fenetre, text="2 joueur", command=select_deux_joueur)
    restoration = tk.Button(fenetre, text="Restorer", command=restorer)
    fenetre.pack()
    un_joueur.place(x=10, y=10)
    deux_joueur.place(x=100, y=10)
    restoration.place(x=55, y=50)

#Voici le code pour le menu pour un seul joueur 
def select_un_joueur():
    global FRAME, CANVAS, board, response, NB_OF_GUESS, TMP, HEIGHT, NB_PLAYER
    NB_OF_GUESS = TMP
    HEIGHT = NB_OF_GUESS*55+70
    FRAME = tk.Toplevel(ROOT)
    CANVAS = tk.Canvas(FRAME, width=WIDTH, height=HEIGHT, highlightthickness=0,highlightbackground="black", relief=tk.FLAT,bg='#8c582d',bd=0)
    CANVAS.pack()
    board, response = drawBoard()
    CANVAS.focus_set()
    userAction()
    CANVAS.bind("<space>", lambda _: initGame(board, response))

#Voici le menu pour les deux joueurs , à l'inverse de celui pour un seul joueur     
def select_deux_joueur():
    global FRAME, CANVAS, board, response, NB_OF_GUESS, HEIGHT, NB_PLAYER
    NB_PLAYER = 2
    NB_OF_GUESS = 1
    HEIGHT = NB_OF_GUESS*55+70
    FRAME = tk.Toplevel(ROOT)
    CANVAS = tk.Canvas(FRAME, width=WIDTH, height=HEIGHT, highlightthickness=0,highlightbackground="black", relief=tk.FLAT,bg='#8c582d',bd=0)
    CANVAS.pack()
    board, response = drawBoard()
    CANVAS.focus_set()
    userAction()

ROOT = tk.Tk()
selection_joueur()
ROOT.mainloop()
