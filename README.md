********************************************************************************
  **		VALORISATION DE DONNEES OPEN DATA PAR INTERFACE GEOGRAPHIQUE	**
********************************************************************************

**Qu'est-ce c'est ?**
--------------------

	C’est un service gratuit de cartographie mettant en avant les lieux remarquables de Lyon (hôtels, restaurants, hébergement collectif, hébergement locatif, patrimoine, commerce et service) destinée à tous utilisateurs souhaitant effectuer une recherche plus approfondie.

**Participants au projet**
---------------------------
	MAILLOT Claudia  p1507893
	REISSER Juliette p1409933

**FAQ**
-------
1. Quel est le fichier contenant la page web de l'interface?

	index.html qui est à la racine du fichier.

2. Avec quel navigateur dois-je ouvrir index.html ?

	Veuillez ouvrir avec Firefox.

3. Comment zoomer ou bien pivoter la carte ?

	En bas à droite de la page, vous trouverez trois icônes.
	À l'aide du "+" et du "-", vous pouvez respectivement agrandir ou diminuer le champ de vision de la carte. Il existe aussi la molette de la souris pour exécuter plus rapidement ces actions.
	Avec le triangle, maintenez le clic gauche de la souris enfoncé tout en la bougeant dans la direction voulue ou placez directement le pointeur sur la carte en imitant les mouvements précédemment décrits mais avec le clic droit.

4. Comment trouver une adresse à l'aide de la barre de recherche ?

	Tapez une adresse dans la barre de recherche. Au bout de 3 caractères, vous aurez une autocomplétion.
	Puis choisissez dans la liste, à l'aide des flèches directionnelles, l'adresse souhaitée.
	Cliquez sur la touche entrée ou bien directement sur le bouton avec la loupe.

5. Comment choisir un hôtel, par exemple ?

	Dirigez-vous sur l'icône du menu. Un sous-menu s'affichera.
	Faites un choix. Le(s) élément(s) souhaité(s) s'affichera(ont).

6. Comment avoir des informations sur une adresse tapée la main ou bien à l'aide du sous-menu?

	Cliquez sur le marqueur pour voir l'adresse.
	Pour accéder au numéro de téléphone ou bien à l'adresse, cliquer sur "Plus de détails".

**Fonctions implémentées:**
---------------------------
1. *en jQuery*

	--> Initialisation des tableaux de données et des booléens
	--> Récupération des données contenues dans les fichiers .js

2. *en jQuery-ui*

	--> Initialisation et opérations sur les sliders
	--> Autocomplétion de la barre de recherche

3. *en JavaScript*

	--> Ajout des markers et des popups : function ajouterElementSurCarte(marker, typeMarker)

	--> Suppression des markers de la map : function supprimer()

	--> Transformation d'une chaine de caractère : function decouperChaine(string)

	--> Ajout des éléments selon le type (ex. typeResto) et la catégorie de la donnée (ex. Bouchon) : function typeSousCategorie(type, categorie)

	--> Coloration d'étoile lorsqu'on passe la souris dessus : function rate(level, type)

	--> Remets toutes les étoiles en blanc : function zero(id, type)

	--> Ajout des éléments selon le choix des étoiles : function etoile(char, type)

	--> Récupération d'un intervalle : function prix(type, indice)

	--> Ajout des données dont le prix appartient à un intervalle : function calculPrix(minimumSlider, maximumSlider, x, type)

	--> Calcul de prix : function prixParCategorie(type, min, max)

	--> Change le collapse selon s'il est déplié ou non : function changementBoutton(pointer)

	--> Gestion de l'évènement sur la touche Entree : function toucheEntree (event)

	--> Recherche d'une adresse taper à la main dans la base de données : function rechercher()

4. *Corps de la page*

	--> Barre de recherche
	--> Menu vertical de gauche
	--> Map

**Contenus du répertoire R1-RC6:**
----------------------------------

1. *data*

2. *src*

3. *index.html*

	--> exécutable

4. *README.md*

**Contenus des fichiers du répertoire src:**
--------------------------------------------

1. *style.css*

	Feuille de style CCS personnalisé

2. *datajson.py*

	Géocode les adresses sous forme de latitude et de longitude en les mettant dans des fichiers :
		--> data_coll.js
		--> data_commerce.js
		--> data_hotel.js
		--> data_loc.js
		--> data_patri.js
		--> data_resto.js

**Contenus des fichiers du répertoire data/font:**
--------------------------------------------------

	--> les polices souhaitées

**Contenus des fichiers du répertoire data/img:**
-------------------------------------------------

	--> des images dont nos markers

**Contenus des fichiers du répertoire data/jquery-ui:**
-------------------------------------------------------

	--> bibliothèques nécessaires pour utiliser jquery-ui

**Contenus des fichiers du répertoire data/js:**
------------------------------------------------

	--> bibliothèques nécessaires pour utiliser jquery et bootstrap

**Contenus des fichiers du répertoire data/slider:**
----------------------------------------------------

	--> bibliothèques nécessaires pour utiliser le slider

**Information complémentaire**
--------------------------------

	Notre jeu de données est fait à partir des données récupérées sur la plateforme du Data Grand Lyon :
<https://data.grandlyon.com># LIFPROJET
