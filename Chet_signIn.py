import streamlit as st
import backend as be
import Chet_login as cl

#initialize database connection
supabase = be.init_connection()

st.set_page_config(page_title="CHET", page_icon="💬")

cl.set_background('back3.png')

#signin function returns TRUE or FALSE if the new user was correctly added or not
def check_signin():
    if be.signin(supabase, st.session_state["Username"], st.session_state['Password'], st.session_state['Mail']):
        #goes back to the login page
        cl.nav_to("https://fedrosauro-chet-application-chet-login-c65w2j.streamlit.app/")
    else:
        st.error('Dati inseriti non corretti', icon="🚨")

tabs_font_css = """
                    <style>
                        div[class*="stTextInput"] label {
                          font-size: 20px;
                          font-family: "Courier New", monospace;
                          text-align: Center;
                          color: Orange;
                        }
                    </style>
                """
st.write(tabs_font_css, unsafe_allow_html=True)

for i in range(5):
    st.write("")

#main code
placeholder = st.empty()
with placeholder.container():
    with st.form(key='form', clear_on_submit=True):
        st.session_state['Username'] = st.text_input("Username:")
        st.session_state['Password'] = st.text_input("Password:", type="password")
        st.session_state['Mail'] = st.text_input("Mail:")
        signin_button=st.form_submit_button(label='Sign In')

if signin_button:
    check_signin()
