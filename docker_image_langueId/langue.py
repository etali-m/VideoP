import os
import speech_recognition as sr
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

    identified_language = max(transcriptions, key=lambda k: len(transcriptions[k]))

    return identified_language, transcriptions[identified_language]

def write_language_to_file(language, output_file):
    with open(output_file, 'w') as file:
        file.write(language)

def main():
    #video_name = input("Entrez le chemin du fichier vidéo : ")
    #video_path = f"../Pipeline_outpouts/{video_name}"

     # Chemin du dossier contenant les vidéos compressées
    folder_path = "../Pipeline_outpouts"

    # Liste tous les fichiers dans le dossier
    files = os.listdir(folder_path)

    # Filtrer les fichiers pour ne conserver que les vidéos
    video_files = [file for file in files if file.endswith(".mp4")]

    if len(video_files) == 1:
        # Si une seule vidéo est trouvée, récupérer son nom
        video_name = video_files[0]
        video_path = os.path.join(folder_path, video_name)
        print(f"La seule vidéo trouvée dans le dossier est : {video_path}")
        
        # Utilisez video_path comme vous le souhaitez dans votre code
    elif len(video_files) == 0:
        print("Aucune vidéo trouvée dans le dossier.")
        return
    else:
        print("Plusieurs vidéos trouvées dans le dossier. Impossible de déterminer laquelle choisir automatiquement.")

    ######################## 

    audio_path = 'temp_audio.wav'
    extract_audio_from_video(video_path, audio_path)

    identified_language, transcription = identify_spoken_language(audio_path)

    if identified_language:
        print(f"Langue détectée dans la vidéo : {identified_language}")
        print("Transcription :")
        print(transcription)
        identified_language = identified_language[:2]
        # Écrire la langue identifiée dans un fichier
        write_language_to_file(identified_language, '../Pipeline_outpouts/langue.txt')
        print("Langue identifiée écrite dans identified_language.txt.")
    else:
        print("Échec de l'identification de la langue.")

    os.remove(audio_path)

if __name__ == "__main__":
    main()
