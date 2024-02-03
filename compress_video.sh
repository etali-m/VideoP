#!/bin/bash

# Demander à l'utilisateur le nom de la vidéo
read -p "Entrez le nom de la vidéo à compresser (sans extension) : " video_name

# Chemin de la vidéo à compresser
input_video="Input_videos/${video_name}"
output_video="Pipeline_outpouts/${video_name}_compressed.mp4"

# Vérification de l'existence de la vidéo
echo $input_video
if [ -f "$input_video" ]; then
    echo "Compression de la vidéo ${video_name}.mp4 en cours..."
    ffmpeg -i "$input_video" -vf scale=720:480 "$output_video"
    #ffmpeg -i "$input_video" -codec:v libx264 -preset fast "$output_video"
    echo "Compression terminée. La vidéo compressée est disponible : ${video_name}_compressed.mp4"
else
    echo "La vidéo ${video_name}.mp4 est introuvable dans le dossier 'Input_videos'. Veuillez vérifier le nom de la vidéo."
fi