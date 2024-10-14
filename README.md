Gateway Meshtastic eJebberd – Mise en marche
Adapté par ON3MEE

Vous trouverez les informations complètes dans "Lisez-moi.pdf"

Introduction

Voici le projet d’un gateway Meshtastic eJabberd. Le gateway permet de se connecter à un réseau Meshtastic via un client de messagerie de tchat instantané XMPP sur un LAN. Cela permet de pouvoir se connecter à plusieurs stations (PC, smartphone, …) sur un seul nœud Meshtastic à une interface de tchat web ou via des applications de tchat clientes XMPP. Ces applications clientes ressemblent à un tchat Messenger et sont compatible Windows, Android, IOS, …

L’objectif initial du projet est de pouvoir mettre quelques PC (ou smartphones) sur le même nœud meshtastic et afficher un seul tchat pour un poste de commandement de services de secours. Un nœud Meshtastic n’accepte qu’un seul utilisateur !

Coté conception, je me suis basé sur la distribution Freedom Box pour le serveur XMPP et son client web et sur le projet Meshwatch (https://github.com/datagod/meshwatch) qui fait l’interface avec le nœud Meshtastic. J’ai adapté le code source de Meshwatch pour y intégrer le client PYXMPP2 (https://github.com/Jajcus/pyxmpp2 ). 

![image](https://github.com/user-attachments/assets/a998855e-65cd-4f86-953e-1e7c3c2276ba)

AVERTISSEMENT !!!

Je vous préviens que je ne suis pas un codeur et que je déteste PYTHON. Epargnez-moi des remarques du genre : « Vous codez mal, … » . Je suis très conscient que le projet ici n’est pas du tout bien pensé et que c’est du bricolage. Mais ça fonctionne. 

Je vous mets le code à disposition. N’hésitez pas à l’améliorer et à même reprendre le projet. Je suis 100 % ouvert à toute aide comme le veut le monde du logiciel libre.

Remerciements
Je remercie ON3CED (http://www.on3ced.com/)  pour leur aide apportée pour les différents essais du réseau Meshtastic et du gateway Freedom Box.

On peut aussi remercier datagod (https://github.com/datagod/meshwatch/commits?author=datagod)  qui a créé l’outil Meshtalk qui a permis le développement de ce projet.

Contenu du package

![image](https://github.com/user-attachments/assets/0395e9fc-a932-421f-b601-4660a736e624)

-	Code source

Ce sont les listings des programmes modifiés et utilisé.

-	Logiciels clients XMPP

Les installs de différentes applications clientes XMPP pour Windows, Linux et Android.

-	2023-06-09 … .zip

C’est l’image Freedom Box modifiée à installer sur la carte SD.

![image](https://github.com/user-attachments/assets/61496215-e2d5-4afd-8572-ff209f3e5085)

Prérequis

Il faut câbler en respectant le schéma de la page précédente. On peut y ajouter des points d’accès WIFI, etc …

Concernant le routeur, il est indispensable de configurer le nom de domaine correctement : localdomain. 

Les comptes XMPP n’accepte que des adresses de ce genre : user@machinex.localdomain . Pas d’adresse IP !!! user@192.168.1.1 ne fonctionnera pas !!! Si la résolution du domaine ne fonctionne pas, le système ne pourra pas fonctionner !

On règle ces paramètres dans le web CLI du routeur.

Dans ce projet, le nom de domaine est localdomain. Le nom de machine est meshtastic. Les comptes utilisateurs sont user1 ; user2 ; … Cela donne une adresse du style : 

user1@meshtastic.localdomain.

Dans certains cas, il faudra une adresse du style : user1@meshtastic et non user1@meshtastic.localdomain. Cela dépendra de votre routeur. Il faudra donc faire des tests pour déterminer le bon suffixe. Dans ce cas, il faudra modifier les adresses dans le code source de la freedom box (voir annexe de ce document).

Concernant les adresses IP, c’est à vous de décider. Il n’y a pas d’IP à respecter. Le rpi est configuré en IP dynamique. Il est cependant conseillé de fixer l’adresse IP de la freedom box.

Concernant le WIFI, c’est aussi à vous de décider.

Fonctionnement du programme Meshwatch adapté par ON3MEE

![image](https://github.com/user-attachments/assets/03cc7234-c0a6-4b38-a8c6-116d437079a5)

Vue de Meshwatch

![image](https://github.com/user-attachments/assets/26b6ccd2-87d9-4b19-b012-df301b2f25bc)

![image](https://github.com/user-attachments/assets/dffbe7d8-26ae-411a-b240-27e0c122c22d)

A gauche, le projet d’une gobox  Meshtastic pour le terrain. On peut y voir un module T BEAM relié en USB à un RPI 3B+ et un routeur WIFI D-LINK. A  droite, la vue de Meshwatch sur l’écran. 
-	Freedom box
https://freedombox.org/fr/ 
La distribution Freedom Box pour raspberry pi est l’OS de tout le système. Elle inclut nativement un serveur XMPP et client web de tchat.
-	Meshtastic
Il faut installer tous les outils Meshtastic ensuite selon la procédure indiquée sur Meshwatch.
-	Meshwatch
https://github.com/datagod/meshwatch
Meshwatch (anciennement Meshtalk) est un outil développé en python pour afficher et envoyer des messages avec un rasperry pi.
Il faut suivre la procédure indiquée sur le github.
Bien mettre à jour les dépendances Meshtastic si vous utilisez la version Meshtastic V2.x !
-	PYXMPP2
https://github.com/Jajcus/pyxmpp2
PYXMPP2 est en client xmpp python. Il a été intégré au code source de Meshwatch afin de faire le lien entre le monde Meshtastic et le serveur XMPP.

Brève description du programme

Tous les programmes se trouvent dans « /home/admin/meshtalk ».
« meshwatchproc.sh » est le programme principal. C’est un watchdog.
« meshwatch.py » est le code source de Meshwatch.
« sendxmpp.py » est le sous-programme qui sert à envoyer des messages de Meshwatch vers XMPPPY2.
Les codes sources sont disponibles avec les fichiers du projet.

Démo :

![image](https://github.com/user-attachments/assets/9ce1e35d-e725-4574-bdb2-8bacfb9325a4)
![image](https://github.com/user-attachments/assets/d53aa427-87d6-4c0b-88db-3d4512eec429)
![image](https://github.com/user-attachments/assets/1e7e25ad-dd55-4397-b743-f6c9a451985b)
![image](https://github.com/user-attachments/assets/93f9e9e2-f23d-4f4c-b76e-fa095358b37e)
 
CONCLUSION
Voilà le projet Gateway Meshtastic Freedom Box.
Il peut être utilisé en l’état sur un LAN pour permettre à plusieurs stations de se connecteur sur un seul node.
Des évolutions vont être apportées pour enregistrer un log des messages par exemple.
N’hésitez pas à consulter mes autres tutoriels sur www.on3mee.be .
N’hésitez pas aussi à utiliser mon projet parallèle Freedom Box Off Grid : https://www.on3mee.be/informatique/freedom_box_off_grid.htm 

