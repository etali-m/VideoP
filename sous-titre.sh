#!/bin/bash

# Vérifier si autosrt est installé
if ! command -v autosrt &> /dev/null; then
    echo "Le programme autosrt n'est pas installé. Veuillez l'installer avant de continuer."
    exit 1
fi

# Demander à l'utilisateur le chemin de la vidéo
read -p "Veuillez entrer le chemin de votre vidéo : " video_path

# Vérifier si le fichier vidéo existe
if [ ! -f "$video_path" ]; then
    echo "Le fichier vidéo n'existe pas. Veuillez vérifier le chemin et réessayer."
    exit 1
fi

# Utiliser autosrt pour générer les sous-titres
autosrt "$video_path" > video_path.srt

# Vérifier si la génération des sous-titres a réussi
if [ $? -eq 0 ]; then
    echo "Sous-titres générés avec succès."
else
    echo "Échec de la génération des sous-titres."
    exit 1
fi

