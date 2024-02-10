# Utiliser une image de base Ubuntu
FROM ubuntu:latest

# Installation des dépendances nécessaires
RUN apt-get update && apt-get install -y autosrt && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script Bash dans le conteneur
COPY sous-titre.sh /app/

# Donner les droits d'exécution au script
RUN chmod +x sous-titre.sh

# Commande par défaut pour exécuter le script Bash
CMD ["./sous-titre.sh"]
