# Pipeline de traitement video vidP

Ce projet porte sur la création de pipeline de traitement automatique de video
Les vidéo sont stocké en local sur un ordinateur et doivent être traitées par un ensemble de conteneur pour y extraire des méta-données.
Les méta-données extraites et la vidéo compréssée sont ensuite agrégés par des VMs hébergés dans un cloud *AWS*
Le résultat sera affiché sur une page web publiquement accéssible.

![Texte alternatif](https://raw.githubusercontent.com/etali-m/VideoP/main/architecture.png)



## Exécuter le conteneur pour la compréssion de vidéo ?
eg : `docker run -v /chemin video d'entré:/Input_videos -v /chemin dossier de sortie:/Pipeline_outputs video_compressor nom_de_la_video.mp4
`
## Exécuter le conteneur pour l'identification de la langue ?
eg : `sudo docker run -it -v /chemin vers la video:/Pipeline_outputs lang_identification
`
## Exécuter le conteneur pour la génération des sous-titre ?
eg: `sudo docker run -it -v /chenmin vers la vidéo :/Pipeline_outputs subtitles`


## Comment traiter un vidéo dans le pipeline ?
1. Ajouter la vidéo à traiter dans le dossier **Input_videos**
2. Modifier la valeur de la variable d'environnement dans le fichier *.env* avec le nom de la vidéo à traiter
eg : `VIDEO_FILE=test.mp4`
3. Lancer la stack de conteneur pour le traitement avec la commande : `sudo docker compose up`
4. Le résultat de la vidéo traité sera contenu dans le dossier **Pipeline_outputs**
5. Pour uploader les données générer sur notre instance EC2 : lancer le script `./upload.sh`

## Sur AWS
Nous avons créer deux instances : 
1. **Serv1_ubuntu** qui contient un serveur apache qui permet d'affichier la page web
2. **Serv_agregation** qui contient un script bash qui permet d'agréger la vidéo et les sous-titre uploader dans l'instance puis les envoie dans notre bucket S3 comme présenter sur le shéma plus haut

## Visualiser les vidéos sur la page web
Rendez vous à l'adresse : [Vidéo agrégées](http://34.227.63.150/video.html)

