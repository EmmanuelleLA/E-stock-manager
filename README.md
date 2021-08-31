# E-stock-manager
L’ E-Stock Manager est un dispositif qui permet de transformer n'importe quel rangement en objet connecté. Ce dispositif étant conçu pour simplifier le quotidien de l’utilisateur, il est très simple à utiliser. De plus, il est compatible avec tout type de rangement (placard, armoire, commode) et tout type de produit du moment qu’il possède un code-barre. L’E-Stock Manager est également accompagné d’une application mobile. Cette application permet de présenter et d’organiser les données récoltées par le dispositif. L’application est indispensable car c’est grâce à elle que l’utilisateur peut pleinement utiliser l’E-Stock Manager. 

Objectifs : 
- Surveiller le stock et générer un inventaire 
- Transformer n'importe quel rangement en objet connecté 
- Créer des listes de courses 

Composants : 
- lecteur de code-barres 
- un Raspberry Pi 3 
- un bouton vert pour les entrées 
- un bouton rouge pour les sorties 
- une application WEB

Fonctionnement : 
Les scripts Python permettent de récupérer la valeur du code-barres, de faire du Web scraping afin de récupérer le nom et l'image qui sont associés au code-barres sur le site https://fr.openfoodfacts.org/ et enfin de rentrer ces données dans la base de données. Ensuite, ces informations vont être affichées sur le site Web. 


