#!/bin/bash

# Paramètres de connexion SSH
SSH_USER="ubuntu"
SSH_HOST="ec2-52-86-140-4.compute-1.amazonaws.com"
SSH_KEY="Pipeline_outputs/agregation_key.pem"

# Chemin du dossier local contenant les fichiers à copier
LOCAL_DIR="Pipeline_outputs"

# Chemin du dossier sur l'instance EC2 où les fichiers seront copiés
REMOTE_DIR="Video_data"

# Connexion SSH et copie des fichiers
scp -i "$SSH_KEY" "$LOCAL_DIR"/*.mp4 "$SSH_USER@$SSH_HOST:$REMOTE_DIR/"
scp -i "$SSH_KEY" "$LOCAL_DIR"/*.txt "$SSH_USER@$SSH_HOST:$REMOTE_DIR/"
scp -i "$SSH_KEY" "$LOCAL_DIR"/*.srt "$SSH_USER@$SSH_HOST:$REMOTE_DIR/"

# Vérification des erreurs éventuelles
if [ $? -eq 0 ]; then
    echo "Copie des fichiers terminée avec succès. Suppression des fichiers locaux."
    rm -f "$LOCAL_DIR"/*.mp4
    rm -f "$LOCAL_DIR"/*.txt
    rm -f "$LOCAL_DIR"/*.srt
else
    echo "Erreur lors de la copie des fichiers."
fi
