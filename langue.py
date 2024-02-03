import os
import speech_recognition as sr
import langid
import moviepy.editor as mp

def extract_audio_from_video(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def identify_spoken_language(audio_path, languages=['en-US', 'fr-FR', 'es-ES', 'de-DE']):
    recognizer = sr.Recognizer()
    transcriptions = {}

    for lang in languages:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        
        try:
            transcribed_text = recognizer.recognize_google(audio, language=lang)
            transcriptions[lang] = transcribed_text
        except sr.UnknownValueError:
            transcriptions[lang] = ""

    # Choisissez la langue avec le texte le plus long
    identified_language = max(transcriptions, key=lambda k: len(transcriptions[k]))

    return identified_language, transcriptions[identified_language]

def main():
    video_path = input("Entrez le chemin du fichier vidéo : ")

    # Vérifier si le fichier existe
    if not os.path.exists(video_path):
        print("Erreur : fichier introuvable.")
        return

    audio_path = 'temp_audio.wav'

    # Extraire l'audio de la vidéo
    extract_audio_from_video(video_path, audio_path)

    # Identifier la langue parlée et obtenir la transcription
    identified_language, transcription = identify_spoken_language(audio_path)

    if identified_language:
        print(f"Langue détectée dans la vidéo : {identified_language}")
        print("Transcription :")
        print(transcription)
    else:
        print("Échec de l'identification de la langue.")

    # Supprimer le fichier audio temporaire
    os.remove(audio_path)

if __name__ == "__main__":
    main()

