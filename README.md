# Pipeline de traitement video vidP

Ce projet porte sur la création de pipeline de traitement automatique de video
Les vidéo sont stocké en local sur un ordinateur et doivent être traitées par un ensemble de conteneur pour y extraire des méta-données.
Les méta-données extraites et la vidéo compréssée sont ensuite agrégés par des VMs hébergés dans un cloud *AWS*
Le résultat sera affiché sur une page web publiquement accéssible.

## Exécuter le conteneur pour la compréssion de vidéo ?
eg : `docker run -v /chemin video d'entré:/Input_videos -v /chemin dossier de sortie:/Pipeline_outputs video_compressor nom_de_la_video.mp4
`
## Exécuter le conteneur pour l'identification de la langue ?
eg : `sudo docker run -it -v /chemin vers la video:/Pipeline_outputs lang_identification
`
## Exécuter le conteneur pour la génération des sous-titre ?
eg: `sudo docker run -it -v /chenmin vers la vidéo :/Pipeline_outputs subtitles`
