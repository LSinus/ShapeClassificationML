import tensorflow as tf
import numpy as np
from PIL import Image

class_names = ["ellipse", "rectangle", "triangle"]

model_dir = "shapeRecognition.model"

model = tf.keras.models.load_model(model_dir)

image_dir = "test_images/IMG_063E40AAB463-1.jpeg"

img = tf.keras.utils.load_img(
    image_dir, target_size=(70, 70)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)