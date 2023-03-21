<h1>Mastermind en Python</h1>
<p>Ce projet est une implémentation du jeu de plateau Mastermind en Python avec une interface graphique. Le joueur doit deviner un code secret formé de 4 pions de couleur alignés en au plus 10 essais de code. Les règles et les fonctionnalités du jeu sont décrites ci-dessous.</p>
<h2>Fonctionnalités</h2>
<ul><li>Mode 2 joueurs : le premier joueur choisit le code secret, puis celui-ci est caché et l’autre joueur doit le trouver ;</li><li>Mode 1 joueur : idem sauf que le code secret est choisi au hasard au début du jeu ;</li><li>Sauvegarde et rechargement d'une partie en cours ;</li><li>Retour en arrière pour annuler des essais qui ont été faits ;</li><li>Aide proposant un code compatible avec les informations obtenues aux essais précédents ;</li><li>Modification des paramètres du jeu : le nombre de pions constituant le code secret, le nombre de couleurs et le nombre d’essais maximum ;</li><li>Mode sans joueur : le code à chercher est choisi au hasard et une intelligence artificielle (IA) joue à la place du joueur qui décode.</li></ul>
<h2>Règles du jeu</h2>
<ul><li>Il s’agit d’un jeu à 2 joueurs dans lequel un des joueurs choisit un code secret formé de 4 pions de couleur alignés et l’autre joueur doit deviner ce code en au plus 10 essais de code.</li><li>À chaque essai, le joueur qui décode acquiert l’information suivante :<ul><li>Le nombre de pions bien placés (mais il ne sait pas lesquels) ; un pion est bien placé s’il a la même couleur que le pion qui est à la même position dans le code secret.</li><li>Le nombre de pions mal placés; un pion est mal placé s’il a la même couleur qu’un pion du code secret qui n’est pas à une position d’un pion bien placé ; de plus chaque pion du code secret peut compter pour au plus un pion mal placé.</li></ul></li><li>Cette information peut être matérialisée par deux nombres accolés au code essayé ou bien, comme sur le jeu de plateau, par des petits pions dont le nombre indique en rouge (resp. en blanc) le nombre de pions bien (resp. mal) placés.</li></ul>
<h2>Prérequis</h2>
<ul><li>Python 3</li><li>Pygame</li></ul>
<h2>Comment jouer</h2>
<ol><li>Cloner ce dépôt en local. https://github.com/Akimizu26/projet-TD1-Mastermin-BI</li><li>Installer les prérequis en exécutant la commande suivante : <code>pip install pygame</code></li><li>Lancer le jeu en exécutant la commande suivante : <code>python main.py</code></li><li>Suivre les instructions affichées à l'écran pour jouer.</li></ol>
<h2>Auteur</h2>
<p>Ce projet a été réalisé par Enzo Boughanmi,Vianney MOURLON au TD01 .</p>
