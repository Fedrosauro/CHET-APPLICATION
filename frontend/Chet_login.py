#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:54:23 2022

@author: simonecossaro
"""

import streamlit as st
import backend as be
import webbrowser

st.set_page_config( page_title="CHET", layout="centered")

# se credenziali giuste viene reindirizzato alla pagina di google per ora
# se credenziali errate messaggio d'errore  
def check_login():
    if be.login(supabase):
       placeholder.empty() 
       webbrowser.open("https://www.google.it")
    else:
        st.error('Username e/o password errati', icon="🚨")
      
        
placeholder = st.empty()

with placeholder.container():
    st.title("CHET")
    with st.form("my_form"):      
        st.session_state['Username'] = st.text_input("Username:")
        st.session_state['Password'] = st.text_input("Password:", type="password")
        b1 = st.form_submit_button("LOGIN")
        st.write('Non sei ancora registrato?')
        b2 = st.write(f'''
                      <a target="_self" href="https://www.google.it?Username=st.session_state['Username']"> 
                      <button>
                      SIGN IN
                      </button>
                      </a>
                      ''',
                      unsafe_allow_html=True
                      )

if b1:
    check_login()
