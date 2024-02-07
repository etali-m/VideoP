import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

def load_and_preprocess_image(img):
    img = cv2.resize(img, (299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def recognize_animals_in_video(video_path):
    model = InceptionV3(weights='imagenet')
    cap = cv2.VideoCapture(video_path)
    previous_animals = set()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        processed_frame = load_and_preprocess_image(frame)
        predictions = model.predict(processed_frame)
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        
        current_animals = set()
        for _, animal, confidence in decoded_predictions:
            current_animals.add(animal)
        
        new_animals = current_animals - previous_animals
        for animal in new_animals:
            print(f"{animal} detected.")
        
        previous_animals = current_animals
        
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

video_path = "path_to_your_video.mp4"
recognize_animals_in_video(video_path)

