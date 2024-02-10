#Image de base
FROM ubuntu:latest

#installation des outils nécessaires pour la compression
RUN apt-get update && apt-get install ffmpeg -y


#Definition du repertoire de travail
WORKDIR /app

#Copie du script de compression de video dans le conteneur
COPY /compress_video.sh /app/compress_video.sh
RUN chmod +x /app/compress_video.sh


#Commande pour lancer le script
CMD [ "./compress_video.sh" ]