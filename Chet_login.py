#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:54:23 2022

@author: simonecossaro
"""

import streamlit as st
import backend as be
import webbrowser

supabase = be.init_connection()

st.set_page_config( page_title="CHET", layout="centered")

#funzione che reindirizza ad un url
def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

# se credenziali giuste viene reindirizzato alla pagina di google (per ora...poi si passerà alla chat)
# se credenziali errate messaggio d'errore
def check_login():
    if be.login(supabase, st.session_state["Username"], st.session_state["Password"]):
        nav_to("https:/www.google.it")   
    else:
        st.error('Username e/o password errati', icon="🚨")


# se preme su tasto sign in rediretto a google (per ora...poi si passerà alla pagina di sign in)

placeholder = st.empty()

with placeholder.container():
    st.title("CHET")
    with st.form("my_form"):
        st.session_state['Username'] = st.text_input("Username:")
        st.session_state['Password'] = st.text_input("Password:", type="password")
        b1 = st.form_submit_button("LOGIN")
        st.write('Non sei ancora registrato?')
        b2 = st.markdown(f'''
                      <a href="XXXXXXX?">
                      <button>
                      SIGN IN
                      </button>
                      </a>
                      ''',
                      unsafe_allow_html=True
                      )

if b1:
    check_login()
