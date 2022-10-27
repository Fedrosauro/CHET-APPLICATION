#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:54:23 2022

@author: simonecossaro
"""

import streamlit as st
import backend as be

st.set_page_config( page_title="CHET", layout="centered")

    
def check_login():
    if be.login(supabase):
       placeholder.empty() 
       exec(open("messageChat.py").read())
    else:
        st.error('Username e/o password errati', icon="🚨")
      
        
placeholder = st.empty()

with placeholder.container():
    st.title("CHET")
    st.session_state['Username'] = st.text_input("Username")
    st.session_state['Password'] = st.text_input("Password", type="password")
    b1 = st.button('LOGIN')
    st.write('Non sei ancora registrato?')
    b2 = st.button ('SIGN IN')

if b1:
    check_login()

if b2:
    placeholder.empty()
    exec(open("signIn.py").read())

