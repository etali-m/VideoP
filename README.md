# Pipeline de traitement video vidP

Ce projet porte sur la création de pipeline de traitement automatique de video
Les vidéo sont stocké en local sur un ordinateur et doivent être traitées par un ensemble de conteneur pour y extraire des méta-données.
Les méta-données extraites et la vidéo compréssée sont ensuite agrégés par des VMs hébergés dans un cloud *AWS*
Le résultat sera affiché sur une page web publiquement accéssible.

## Comment exécuter le conteneur pour la compréssion de vidéo ?
`docker run -v /home/utilisateur/videos/Input_videos:/Input_videos -v /home/utilisateur/videos/Pipeline_outputs:/Pipeline_outputs video_compressor nom_de_la_video.mp4
`
## Comment exécuter le conteneur pour l'identification de la langue ?
eg: `sudo docker run -it -v /home/etali/Documents/Cours\ ENSPY/5MSI/Cloud\ computing/Proje\ Pipeline/VideoP/Pipeline_outputs:/Pipeline_outputs lang_identification
`
