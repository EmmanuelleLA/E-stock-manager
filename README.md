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

![Screenshot 2021-08-31 at 17 33 10](https://user-images.githubusercontent.com/88400903/131532848-75cad366-cec4-4031-9d0c-57520c60478c.png)
![Screenshot 2021-08-31 at 17 33 32](https://user-images.githubusercontent.com/88400903/131532864-4ae50b76-62c4-4ea0-8850-74eb3985d35c.png)
