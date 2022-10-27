# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:51:50 2022

@author: ludov
"""
import streamlit as st


st.title("Sign in")
with st.form(key='form'):
    st.session_state['Username'] = st.text_input("Username")
    st.session_state['Password'] = st.text_input("Password", type="password")
    st.session_state['Mail']=st.text_input("Mail")
    signin_button=st.form_submit_button(label='Sign In')

if signin_button:
    st.success("Welcome in the chat {}!".format(st.session_state['Username']))
    
    
    

        




