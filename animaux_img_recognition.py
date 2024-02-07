import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def recognize_animals(image_path):
    model = InceptionV3(weights='imagenet')
    processed_image = load_and_preprocess_image(image_path)
    predictions = model.predict(processed_image)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    for _, animal, confidence in decoded_predictions:
        print(f"{animal}: {confidence * 100:.2f}%")

image_path = "oiseau.jpeg"
recognize_animals(image_path)

