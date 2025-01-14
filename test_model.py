from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

model = load_model("vehicle_classifier.h5")

validation_dir = "data/validation"
validation_datagen = ImageDataGenerator(rescale=1.0 / 255.0)
validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode="binary"
)

loss, accuracy = model.evaluate(validation_generator)
print(f"Accuracy on the validation dataset: {accuracy * 100:.2f}%")
print(f"Loss on the validation dataset: {loss:.4f}")

def predict_image(image_path):
    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        print(f"Image '{image_path}' is classified as: VEHICLE")
    else:
        print(f"Image '{image_path}' is classified as: NON-VEHICLE")

image_path = "data/pisica.png"  # test
predict_image(image_path)
