import streamlit as st

def render_login():
    st.set_page_config(
        page_title='Virtual Fisio', 
        page_icon='👩‍⚕️', 
        initial_sidebar_state='collapsed')
    col1, col2 = st.columns([0.45, 1])
    col2.image(image='virtual_fisio.png', width=250)
    s1, s2, s3 = st.columns([1.5, 2, 1.5])
    with s2.form('form_login'):
        st.text_input(label='ID', help='Seu ID de acesso ao Virtual Fisio')   
        st.checkbox('Manter conectado', value=True)
        st.form_submit_button('Entrar')