FROM ubuntu:latest

# Installation de ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copie du script dans le conteneur
COPY compress_video.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/compress_video.sh

# Définition du script comme point d'entrée
ENTRYPOINT ["compress_video.sh"]
