import coremltools as ct
import tensorflow as tf

tf_model = tf.keras.models.load_model("shapeRecognition.model")
ct_model = ct.convert(tf_model,inputs=[ct.ImageType(scale=1.0/255.0)])

ct_model.save("shapeRecognition.mlmodel")