import streamlit as st
import pandas as pd

def render_pacient():
    st.sidebar.title('Profissional')
    st.sidebar.markdown('---')
    with st.sidebar.expander('Dra. Jaqueline'):
        st.write('Em Breve...')
    with st.sidebar.expander('Dr. Lúcio'):
        st.write('Em Breve...')

    st.title('Virtual Fisio 👩‍⚕️')
    st.caption('Envelhecer ficou no passado...')
    st.markdown('---')
    st.markdown('# Informações')
    st.write(' ')
    l = [
        ['Nome:', 'Caio Kraut de Mendonça Marin'],
        ['CPF:', '498.***.***-64'],
        ['Dt. Nascimento:', '26/05/1999']
    ]
    for i in range(len(l)):
        h1, h2 = st.columns([1, 4])
        h1.write(l[i][0])
        h2.markdown('`' + l[i][1] + '`')
    with st.expander('Mais informações'):
        st.write('Em breve...')
    st.markdown('---')
    st.markdown('# Exercícios')
    st.caption('Para Hoje')
    with st.form('ex_1'):
        st.markdown('`Dra. Jaqueline | 24/08/2021 - 21:34`')
        y1, y2 = st.columns([1, 0.3])
        y1.markdown('## Amplitude de movimento dos ombros')
        # st.markdown('## Amplitude de movimento dos ombros')
        st.caption('Estabilização do ombro enquanto levanta '
        + 'levemente o cotovelo o mais alto possível.\nDurante '
        + 'várias sessões, o cotovelo é gradualmente movido mais '
        + 'alto, aumentando assim a amplitude de movimento da articulação.')
        st.form_submit_button('⚡ Treinar')
    with st.form('ex_2'):
        st.markdown('`Dra. Jaqueline | 23/05/2021 - 16:01`')
        y1, y2 = st.columns([1, 0.3])
        y1.markdown('## Adução-abdução de quadril')
        # st.markdown('## Amplitude de movimento dos ombros')
        st.caption('Estes movimentos ajudam a estabilizar o quadril' 
        + ' e fazem a passada ficar mais segura.')
        st.form_submit_button('⚡ Treinar')
    st.markdown('---')
    st.markdown('# Histórico')
    st.caption('Por semana')
    hist = [
        ['✔️', '✔️', '✔️', '✔️', '✖️'],
        ['✔️', '✔️', '✖️', '✔️', '✔️'],
        ['✔️', '✔️', '✔️', '✔️', '✖️'],
        ['✖️', '✖️', '✔️', '✔️', '✔️'],
        ['✔️', '✔️', '✔️', '✔️', '✔️'],
        ['✔️', '✖️', '✔️', '✖️', '✖️'],
        ['✔️', '✔️', '✔️', '✔️', '✔️'],
        ['✔️', '✔️', '✖️', '✔️', '✖️'],
    ]
    df = pd.DataFrame(hist, columns=['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira'])
    st.table(df)