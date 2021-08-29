from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow as tf


class FacialExpressionModel(object):
    EMOTIONS_LIST = ["Nervoso", "Nojo", "Medo", "Feliz", "Neutro", "Triste", "Surpreso"]

    def __init__(self, model_json_file, model_weights_file):
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        self.loaded_model.load_weights(model_weights_file)
        # self.loaded_model._make_predict_function()

    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]