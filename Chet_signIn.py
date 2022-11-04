# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:51:50 2022

@author: ludov
"""
import streamlit as st
import backend as be
import Chet_login as cl
import base64

supabase = be.init_connection()

st.set_page_config( page_title="Sign in", layout="centered")


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
    </style>
    ''' % (bin_str)
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('schLogin3.png')

#se passa il controllo si va alla chat
#se non lo passa messaggio d'errore
def check_signin():
    if be.signin(supabase, st.session_state["Username"], st.session_state['Password'], st.session_state['Mail']):
        cl.nav_to("https://fedrosauro-chet-application-chet-login-c65w2j.streamlit.app/")
    else:
        st.error('Dati inseriti non corretti', icon="🚨")

st.title("Sign in")
with st.form(key='form'):
    st.session_state['Username'] = st.text_input("Username")
    st.session_state['Password'] = st.text_input("Password", type="password")
    st.session_state['Mail'] = st.text_input("Mail")
    signin_button=st.form_submit_button(label='Sign In')

if signin_button:
    check_signin()
