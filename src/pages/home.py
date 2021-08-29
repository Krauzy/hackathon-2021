import streamlit as st
import pandas as pd
from src.auth.check_auth import get_auth, get_key, set_key

def render():
    auth = None
    id = get_key()
    st.set_page_config(
        page_title='Virtual Fisio', 
        page_icon='👩‍⚕️', 
        initial_sidebar_state='collapsed')
    st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row; gap: 15px;}</style>', unsafe_allow_html=True)
    col1, col2 = st.columns([0.45, 1])
    col2.image(image='./public/virtual_fisio.png', width=250)
    auth = get_auth(id)
    print('auth: ', auth)
    place = st.empty()
    if auth is None:        
        s1, s2, s3 = place.columns([1.5, 2, 1.5])
        with s2.form('form_login'):
            id = st.text_input(label='ID', help='Seu ID de acesso ao Virtual Fisio', value=id)
            if st.form_submit_button('Entrar'):
                auth = get_auth(id)
    
    if auth == 'pacient':
        set_key(id)
        place.empty()
        st.sidebar.title('Profissional')
        st.sidebar.markdown('---')
        with st.sidebar.expander('Dra. Jaqueline'):
            st.write('Em Breve...')
            st.markdown('---')
            st.markdown('<a href="https://meet.google.com/" style="text-decoration: none;" target="_blank">🟢 meet</a>', True)
        with st.sidebar.expander('Dr. Lúcio'):
            st.write('Em Breve...')
            st.markdown('---')
            st.markdown('<a href="#" style="text-decoration: none;" target="_blank">🔴 meet</a>', True)

        st.markdown('---')
        if st.button('Sair'):
            set_key('')
            st.experimental_rerun()
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
        with st.expander('Amplitude de movimento dos ombros'):
            st.markdown('`Dra. Jaqueline | 24/08/2021 - 21:34`')
            st.markdown('## Amplitude de movimento dos ombros')
            st.caption('Estabilização do ombro enquanto levanta '
            + 'levemente o cotovelo o mais alto possível.\nDurante '
            + 'várias sessões, o cotovelo é gradualmente movido mais '
            + 'alto, aumentando assim a amplitude de movimento da articulação.')
            st.markdown('---')
            op = st.radio('Método de Análise', options=['Tempo Real', 'Assíncrono'], key='radio_1')
            if op == 'Assíncrono':
                st.file_uploader('Selecione o vídeo', type=['mp4', 'mkv'])
            else:
                st.write(' ')
                if st.checkbox('⚡ Executar', False, key='check_1'):
                    print(1)
                st.write(' ')
        with st.expander('Adução-abdução de quadril'):
            st.markdown('`Dra. Jaqueline | 23/05/2021 - 16:01`')
            st.markdown('## Adução-abdução de quadril')
            st.caption('Estes movimentos ajudam a estabilizar o quadril' 
            + ' e fazem a passada ficar mais segura.')
            st.markdown('---')
            op = st.radio('Método de Análise', options=['Tempo Real', 'Assíncrono'], key='radio_2')
            if op == 'Assíncrono':
                st.file_uploader('Selecione o vídeo', type=['mp4', 'mkv'])
            else:
                st.write(' ')
                if st.checkbox('⚡ Executar', False, key='check_2'):
                    print(1)
                st.write(' ')
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
    elif auth == 'fisio':
        set_key(id)
        place.empty()
        st.markdown('---')
        if st.button('Sair'):
            set_key('')
            st.experimental_rerun()
        st.markdown('# Informações')
        st.write(' ')
        l = [
            ['Nome:', 'Jaqueline da Silva Nogueira'],
            ['CPF:', '497.***.***.-12'],
            ['Dt. Nascimento:', '15/07/1972']
        ]
        for i in range(len(l)):
            h1, h2 = st.columns([1, 4])
            h1.write(l[i][0])
            h2.markdown('`' + l[i][1] + '`')
        with st.expander('Mais informações'):
            st.write('Em breve...')
        st.markdown('---')
        st.selectbox('Pacientes', options=[''])


