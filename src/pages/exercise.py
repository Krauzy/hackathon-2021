import streamlit as st
from time import sleep

def render_train():
    st.title('Virtual Fisio 👩‍⚕️')
    st.caption('Envelhecer ficou no passado...')
    st.markdown('---')
    st.markdown('# Amplitude de movimento dos ombros')
    st.caption('Estabilização do ombro enquanto levanta '
        + 'levemente o cotovelo o mais alto possível.\nDurante '
        + 'várias sessões, o cotovelo é gradualmente movido mais '
        + 'alto, aumentando assim a amplitude de movimento da articulação.')
    with st.expander('Ajuda'):
        s1, s2 = st.columns([0.45, 1])
        s2.image('a1.jpg', width=250)
    st.video(data='ex.mp4')
    with st.empty():
        if st.button('Iniciar ▶️'):
            st.error('Exercício está incorreto')
            sleep(6)
            st.success('Exercício está correto e está sendo fetio conforme o indicado')
            sleep(4)
            st.warning('Exercício está correto mas não está sendo feito conforme indicado: Faça um pouco mais rápido')
            sleep(2)
            st.success('Exercício está correto e está sendo fetio conforme o indicado')
            sleep(2)
            st.error('Exercício está incorreto')
            sleep(2)
            st.warning('Exercício está correto mas não está sendo feito conforme indicado: Faça um pouco mais rápido')
            sleep(1)
            st.success('Exercício está correto e está sendo fetio conforme o indicado')
            sleep(2)
            st.error('Exercício está incorreto')

    st.markdown('---')
    with st.expander('Informações'):
        l = [
            ['Exercício: ', 'Amplitude de movimento dos ombros'],
            ['Nível: ', '⭐⭐'],
            ['Conclusão: ', '39.45%'],
            ['Status: ', 'Imcompleto'],
            ['Diagnóstico Imediato: ', 'Necessário refazer'],
            ['Parecer do Responsável: ', 'Não disponível'],
            ['Evolução: ', '-21%']
        ]
        for i in range(len(l)):
            h1, h2 = st.columns([1, 4])
            h1.write(l[i][0])
            h2.markdown('`' + l[i][1] + '`')