import streamlit as st
from supabase import create_client, Client

############################# CONNECTION FUNCTION ###########################
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)
#############################################################################

############################### LOGIN FUNCTION ##############################
def login(supabase_conn):
    rows = supabase_conn.table("Users").select("*").execute()
    for row in rows.data:
        if st.session_state["Username"] == row["Username"] and st.session_state["Password"] == row["Password"]:
            return True
    return False
##############################################################################

############################## SIGNIN FUNCTION ###############################
def signin(supabase_conn):
    #check if username or password or mail are empty or contains only whitespaced
    if st.session_state["Username"] == "" or ' ' in st.session_state["Username"] or st.session_state["Password"] == "" or ' ' in st.session_state["Password"] or st.session_state["Mail"] == "" or ' ' in st.session_state["Mail"]:
        return False

    rows = supabase_conn.table("Users").select("*").execute()
    for row in rows.data:
        if st.session_state["Username"] == row["Username"]:
            return False

    supabase_conn.table("Users").insert({"Username":st.session_state["Username"] , "Password":st.session_state["Password"], "Mail":st.session_state["Mail"]}).execute()
    return True
##############################################################################
