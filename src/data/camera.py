import cv2
import streamlit as st

from index import FaceExpression
from mediaPipe import MediaPipe

st.title("Bem vindo ao Virtual Fisio")
run = st.checkbox('Run')
if run:
    expressoes = st.checkbox('Expressões')
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)
fe = FaceExpression()
mp = MediaPipe()

while run:
    ret, frame = cam.read()
    media = mp.execute(frame)
    if(expressoes):
        media = fe.getExpression(media)
    frame = cv2.cvtColor(media, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')