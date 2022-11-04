#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:54:23 2022

@author: simonecossaro
"""

import streamlit as st
import backend as be
import base64

supabase = be.init_connection()

st.set_page_config( page_title="CHET", layout="centered")

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

#funzione che reindirizza ad un url
def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; URL=javascript:window.open('http://google.com','_parent');">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

# funzione che:
# se credenziali giuste reindirizza alla chats
# se credenziali errate messaggio d'errore
def check_login():
    if be.login(supabase, st.session_state["Username"], st.session_state["Password"]):
        link = "https://fedrosauro-chet-application-chet-room-0dx65z.streamlit.app/?user=" + st.session_state["Username"]
        nav_to(link)
    else:
        st.error('Username e/o password errati', icon="🚨")


set_background('schLogin3.png')
for i in range(8):
    st.write("")

with st.form("my_form"):
     st.session_state['Username'] = st.text_input("Username:")
     st.session_state['Password'] = st.text_input("Password:", type="password")
     b1 = st.form_submit_button("LOGIN")
     st.write('Non sei ancora registrato?')
     b2 = st.form_submit_button("SIGN IN")
if b1:
    check_login()
if b2:
    nav_to("https://fedrosauro-chet-application-chet-signin-jaygim.streamlitapp.com/")

st.markdown("""
        <style>
               .block-container {
                    padding-bottom: 0px;
                }
        </style>
        """, unsafe_allow_html=True)
