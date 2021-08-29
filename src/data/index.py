import cv2
from model import FacialExpressionModel
import numpy as np

dir = ''


class FaceExpression:

    def __init__(self):
        self.facec = cv2.CascadeClassifier(dir + 'haarcascade_frontalface_default.xml')
        self.model = FacialExpressionModel(dir + "model.json", dir + "model_weights.h5")
        self.font = cv2.FONT_HERSHEY_PLAIN

    def getExpression(self, img):
        gray_fr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.facec.detectMultiScale(gray_fr, 1.3, 5)

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y + h, x:x + w]

            roi = cv2.resize(fc, (48, 48))
            pred = self.model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            cv2.putText(img, pred, (x + (w // 3), y - 5), self.font, 5, (0, 0, 255), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return img
