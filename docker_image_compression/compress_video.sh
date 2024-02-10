#!/bin/bash

input_video="/Input_videos/$1"
output_video="/Pipeline_outputs/${1}_compressed.mp4"

if [ -f "$input_video" ]; then
    echo "Compression de la vidéo $1 en cours..."
    ffmpeg -i "$input_video" -vf scale=720:480 "$output_video"
    echo "Compression terminée. La vidéo compressée est disponible : ${1}_compressed.mp4"
else
    echo "La vidéo $1 est introuvable dans le dossier 'Input_videos'. Veuillez vérifier le nom de la vidéo."
fi
