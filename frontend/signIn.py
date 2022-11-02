# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:51:50 2022

@author: ludov
"""
import streamlit as st
from urllib.parse import urlparse 
from urllib.parse import parse_qs

st.title("Sign in")
st.session_state['Username'] = st.text_input("Username")
st.session_state['Password'] = st.text_input("Password", type="password")
st.session_state['Mail']=st.text_input("Mail")
button = st.button("Submit")

items= {st.session_state['Username']}
url_test= 'https://www.ilpost.it/2022/10/25/path?user={}/'
for i in items: 
    url = url_test.format(i)
    st.write(url)
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)['user'][0]
    st.write(captured_value)
print(captured_value)

if button:
    st.success("Welcome in the chat {}!".format(st.session_state['Username']))
    
