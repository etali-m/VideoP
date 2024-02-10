#utilisation de python comme image de base
FROM python:3.8

#Défintion du repertoire de travail
WORKDIR /app

#Copy du script d'identification de langue dans le conteneur
COPY langue.py /app/

#installation des dépendances
RUN pip install SpeechRecognition moviepy


#commande pour lancer le script
CMD ["python", "langue.py"]