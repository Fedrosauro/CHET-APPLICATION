# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:51:50 2022

@author: ludov
"""
import streamlit as st
import backend as be
import Chet_login as cl

#se passa il controllo si va alla chat
#se non lo passa messaggio d'errore
def check_signin():
    if be.signin(supabase):
        cl.nav_to("url_chat")
    else:
        st.error('Dati inseriti non corretti', icon="🚨")

st.title("Sign in")
with st.form(key='form'):
    st.session_state['Username'] = st.text_input("Username")
    st.session_state['Password'] = st.text_input("Password", type="password")
    st.session_state['Mail']=st.text_input("Mail")
    signin_button=st.form_submit_button(label='Sign In')

if signin_button:
    check_signin()
    
    
    

        




