------------------------------------
I. Créer l'environnement virtuel
-------------------------------------
1. python3 -m venv env # pour créer un env virtuel 
2. source env/bin/activate # pour activer l'env virtuel
3. which python # pour la verification 


------------------------------------
II. Installer Django avec pip
-------------------------------------
tout d'abord assurer vous que l'env est activer

4. pip install --upgrade pip # mis a jour de pip
5. pip install django==3.1.6 # installer django avec une version précise   
6. python -m django --version # verification 
7. pip freeze > requirements.txt 
8. pip install -r requirements.txt # si on veut installer à nouveau  


------------------------------------
III. Créer un projet Django 
-------------------------------------
9. django-admin startproject <nom_projet> # pour initialiser un projet django 
10. django-admin --help 
11. django-admin help <commande>

------------------------------------
III. le structure d'un projet Django 
-------------------------------------

12. les fichiers : asgi.py && wsgi.py : utilier lors de déploiement de site sur un serveru web 

13. le fichier manage.py : pour lancer le serveur local 
14. le fichier urls.py : pour le Modéle URL 
15. le fichier settings.py # le fichier qui conteint tout les préferences de notre app 


------------------------------------
IV. lancer le serveur 
-------------------------------------

Django dispose d'un serveur (pour le dev et non la production ) 
pour lancer le serveur : 
16. python manage.py runserver (assurer vous d'activer l'env virtuel )
17. python manage.py migrate # pour appliquer les migrations 


------------------------------------
V. Créer un chemin d'URL :
-------------------------------------
par defaut on'a un chemin d'URL : path('admin/',admin.site.urls)

18 . from django.views.defaults import server_error #  view d'erreure 500 
     path('test/',server_error)

19. chemin URL : path('url/' , view) # avce view fonction : view(request)---> HttpResponse


------------------------------------
VI. le parmétre APPEEND_SLASH 
-------------------------------------

il s'agit d'une variable d'énvironnement qui fait une redriction d'url sans slash a la fin vers un url avce un slash à la fin 
par defaut : APPEEND_SLASH  = True 


------------------------------------
VII .  Créer une vue pour l'URL :
-------------------------------------

une vue (view) est une fonction ou une méthode qui traite une requête HTTP spécifique et renvoie une réponse. 

Une vue est responsable de l'interprétation des données de la requête, de l'exécution des traitements nécessaires et de la construction de la réponse à renvoyer au client.

Dans le contexte de Django, une vue est généralement définie comme une fonction dans un fichier Python, ou parfois comme une méthode dans une classe appelée "vue basée sur une classe". La fonction ou la méthode de la vue prend en général deux paramètres : la requête HTTP (request) et éventuellement d'autres paramètres, et elle renvoie une réponse HTTP.

Les vues dans Django sont configurées à l'aide du fichier urls.py, qui associe des URL spécifiques aux vues correspondantes. Lorsqu'un utilisateur accède à une URL donnée dans l'application Django, le framework utilise la configuration des URL pour déterminer quelle vue doit être appelée pour traiter cette requête.


------------------------------------
VIII .  Créer une template :
-------------------------------------
20. si on créer un dossier templates  il faut : 
---- ajouter le chemin dans la variable dans la liste DIRS (TEMPLATES) :
   'DIRS'=[os.path.join(BASE_DIR , "DocBlog/templates/")]
----- utiliser la fonction render : render(request , "page.html") (dans views.py)
	from django.shortcuts import render

 


--------------------------------------------
VV . Insérer des donnes dans une template  :
---------------------------------------------

21.On peut insérer des données dans  templete  grace e la paramétre context
de la fonction render : 
---------------> render(request , "index.html" , context = {cle1 : val1}
---------------> Et dans la page "index.html" On peut insérer ces donnes 
		grace à :{{cle1}} (On affiche val1 dans la page web )
---------------> Optionse de filter : avce la barre verticale "|"
		*. exemple1 : {{cle1| upper}} # pour afficher la val1 majscule
 		*. exemple2 : {{date | date :"d F Y H:i:s" }}
---------------> pour plus de infos sur filter : django templetes filter 

22. On peut changer la lange a l'aide de la variable : LANGUAGE_CODE 
pour FR : "fr-FR" pour ANG : "en-us"


--------------------------------------------
VVI . Créer une application en django  :
---------------------------------------------
23. python manage.py startapp <nom_app> # pour créer une application 

24. l'Archi de application :
	*. views.py : contient les vues de notre app 
	*. tests.py :pour faire de test de notre app
	*. modeles.py : conteint des modeles pour intéragi avec la base des donnes
	*. apps.py : pour gérer la configuration de notre app
25. pour la configuration il faut ajouter l'app dans le fichier settings 
dans la liste : INSTALED_APPS = [..... , '<nom_app>' ]



--------------------------------------------
IX . Créer des URL dans une app :
---------------------------------------------
26.on creé un fichier urls.py dans notre app : on utilise la fonction path , et la liste urlpatterns 
27. dans le fichier urls.py de notre projet principale on concatene ce deux chemins de url a l'aide de la fonction : include (from django.urls )
	*.exemple : path('blog/', "nom_app.urls")



--------------------------------------------
X . la vue principale d'une app :
---------------------------------------------
28. On creer un dossier de nom : templates dans ce fichier On ajout les fichiers html (attention au nom )
 RQ : blog/templates/blog/index.html : c'est le structure génerale pour les vues (pour éviter de pb de confusion )
29. dans la fonction vue : On ajout le chemin vers le fichire index.html : render(request , "blog/index.html")

--------------------------------------------
XI . recupération de donnees a partir de l'url :
---------------------------------------------

30. Dans le chemin d'url : path('article_<str:numero>' , vue) dans la fonction vue on peut prend comme paramétre nom_str :
	*.exemple : def vue(request , numero) :
			return render(request , f"article_{numero}")
 

--------------------------------------------
XII . ajouter des fichiers statiques : css 
---------------------------------------------
31 . le dossier "static": par defaut   django cherche dans une app les fichiers css dans le dossier static(attention au nom )
32. pour  charger les fichiers css dans le fichier index.html il faut uitiliser le "garbait de dajago" : 
----------> Gabarit de django :	Le gabarit définit la structure de la page et peut inclure des éléments tels que l'en-tête, le pied de page, la barre de navigation, et le contenu spécifique à chaque page. Les gabarits permettent également l'utilisation de variables, de boucles et de conditions pour rendre les pages dynamiques.
	*Exemple : pour insére le fichier de style.css dans le fichier index.html : 
			  {% load static %}
			  <link rel="stylesheet" href="{% static 'css/style.css' %}">

33. pour le dossier qui ne sont pas de app : il faut ajouter dans le fichier settings.py : 
	STATICFILES_DIRS = [os.path.join(BASE_DIR , "chemin_vers_fichers_css"]


			















