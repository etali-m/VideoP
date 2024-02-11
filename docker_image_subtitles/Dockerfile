# Utiliser une image de base Ubuntu
FROM ubuntu:latest

# Installation des dépendances nécessaires
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y ffmpeg

# Installation de autosrt via pip
RUN pip install autosrt

# Copie du script dans le conteneur
COPY sous_titre.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/sous_titre.sh 

# Définition du script comme point d'entrée
ENTRYPOINT ["sous_titre.sh"]
