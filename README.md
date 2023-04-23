<h1>Mastermind</h1>
<p>Ce programme est un jeu Mastermind en utilisant la bibliothèque tkinter en Python. Le but du jeu est de deviner une combinaison de couleurs de longueur 4 en un nombre limité d'essais.</p>
<h2>Fonctionnalités</h2><ul><li>Une interface graphique pour interagir avec le joueur</li><li>Le joueur peut choisir parmi une gamme de couleurs pour composer la combinaison</li><li>Le joueur reçoit une rétroaction sur la couleur et la position de chaque tentative.</li></ul><h2>Règles du jeu</h2><ul><li>Le jeu consiste à deviner une combinaison secrète de quatre couleurs choisies par l'ordinateur.</li><li>Les couleurs sont choisies parmi une gamme de six couleurs de base : blanc, vert, rouge, marron, doré et orange foncé.</li><li>Les joueurs peuvent choisir la couleur et l'ordre de chaque tentative.</li><li>Pour chaque tentative, l'ordinateur fournit une rétroaction sur le nombre de couleurs correctes et mal placées.</li><li>Le joueur a 11 essais pour trouver la combinaison secrète.</li></ul><h2>Fonctions créées</h2><ul><li><code>userAction()</code> : cette fonction est appelée lorsqu'un tour commence pour permettre au joueur d'interagir avec l'interface utilisateur en utilisant les touches fléchées.</li><li><code>userInAction()</code> : cette fonction est appelée lorsque le joueur a terminé de sélectionner les couleurs et souhaitent confirmer leur choix. Elle annule toutes les liaisons de touche pour empêcher l'utilisateur de continuer à interagir avec l'interface utilisateur.</li><li><code>create_code_one_player()</code> : cette fonction est appelée pour créer une combinaison secrète pour le mode de jeu solo. Elle choisit au hasard une couleur parmi la gamme de couleurs de base et crée une combinaison de 4 couleurs différentes.</li><li><code>initRow()</code> : cette fonction est appelée pour initialiser les valeurs pour chaque tour. Elle initialise la position de chaque couleur, le nombre de couleurs correctes et le nombre de couleurs correctes mais mal placées.</li><li><code>initGame(board, response)</code> : cette fonction est appelée pour initialiser le jeu. Elle configure l'interface utilisateur, la combinaison secrète pour le mode de jeu solo et appelle la fonction <code>initRow()</code>.</li><li><code>select(colorPosition)</code> : cette fonction est appelée pour mettre en évidence la couleur sélectionnée par l'utilisateur.</li><li><code>deselect(colorPosition)</code> : cette fonction est appelée pour annuler la mise en évidence de la couleur sélectionnée par l'utilisateur.</li><li><code>setcolor(colorPosition,color)</code> : cette fonction est appelée pour mettre à jour la couleur d'une case sur l'interface utilisateur.</li><li><code>selectPos(increment)</code> : cette fonction est appelée pour déplacer la sélection de couleur de l'utilisateur vers la gauche ou la droite.</li><li><code>switchColor(increment)</code> : cette fonction est appelée pour mettre à jour la couleur sélectionnée par l'utilisateur.</li><li><code>switchrow()</code> : cette fonction est appelée lorsque l'utilisateur a terminé de sélectionner la combinaison de couleurs et souhaite confirmer sa sélection. Elle vérifie si la sélection de l'utilisateur est correcte, met à jour l'interface utilisateur avec les résultats et passe au tour suivant.</li></ul></div>
<ul><li><p><code>drawBoard()</code> : Cette fonction crée le plateau de jeu en utilisant un tableau et une réponse pour stocker les choix de couleurs des joueurs. Elle crée également deux boutons pour annuler et sauvegarder les coups des joueurs et renvoie le tableau et la réponse.</p></li><li><p><code>annuler()</code> : Cette fonction permet d'annuler le dernier coup du joueur en supprimant la dernière ligne du tableau et de la réponse. Elle utilise une variable globale pour suivre le numéro de ligne actuel et la position de la dernière case remplie.</p></li><li><p><code>sauvegarder()</code> : Cette fonction permet de sauvegarder les choix du joueur dans un fichier JSON qui peut être restauré plus tard. Elle utilise également des variables globales pour stocker les choix de couleur, la couleur codée, les indices et le numéro de ligne actuel.</p></li><li><p><code>restorer()</code> : Cette fonction permet de restaurer les choix de couleurs et l'état du jeu à partir du fichier JSON sauvegardé précédemment.</p></li><li><p><code>selection_joueur()</code> : Cette fonction permet de sélectionner le mode de jeu : un joueur ou deux joueurs. Elle utilise la bibliothèque tkinter pour créer une fenêtre et deux boutons pour choisir le mode de jeu.</p></li><li><p><code>select_un_joueur()</code> : Cette fonction est appelée lorsque le joueur choisit de jouer seul. Elle initialise la fenêtre de jeu et appelle la fonction <code>drawBoard()</code> pour créer le plateau de jeu.</p></li><li><p><code>select_deux_joueur()</code> : Cette fonction est appelée lorsque le joueur choisit de jouer à deux joueurs. Elle initialise la fenêtre de jeu et appelle la fonction <code>drawBoard()</code> pour créer le plateau de jeu avec une seule ligne pour les choix et la réponse.</p></li></ul>
<h2>Auteur</h2>
<p>Ce projet a été réalisé par Enzo Boughanmi,Vianney MOURLON,Kimberly PLANCY, Safia AON au TD01 .</p>
