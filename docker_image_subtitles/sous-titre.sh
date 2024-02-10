#!/bin/bash

# Vérifier si autosrt est installé
if ! command -v autosrt &> /dev/null; then
    echo "Le programme autosrt n'est pas installé. Veuillez l'installer avant de continuer."
    exit 1
fi

# Chemin du dossier contenant les vidéos compressées et le fichier de langue
video_folder="../Pipeline_outpouts"
lang_file="$video_folder/langue.txt"

# Obtenir le nom de la seule vidéo présente dans le dossier
video_file=$(ls -1 "$video_folder"/*.mp4 2>/dev/null | head -n 1)
echo $video_file;
# Vérifier si une vidéo a été trouvée
if [ -z "$video_file" ]; then
    echo "Aucune vidéo trouvée dans le dossier $video_folder."
    exit 1
fi

# Extraire le nom de fichier de la vidéo
video_name=$(basename "$video_file")

# Lire la langue des sous-titres à partir du fichier lang.txt
if [ -f "$lang_file" ]; then
    lang=$(cat "$lang_file")
else
    echo "Le fichier lang.txt n'a pas été trouvé dans le dossier $video_folder."
    exit 1
fi

# Utiliser autosrt pour générer les sous-titres avec la langue spécifiée
autosrt -S "$lang" "$video_file"

# Vérifier si la génération des sous-titres a réussi
if [ $? -eq 0 ]; then
    echo "Sous-titres générés avec succès pour la vidéo : $video_name"
else
    echo "Échec de la génération des sous-titres pour la vidéo : $video_name"
    exit 1
fi