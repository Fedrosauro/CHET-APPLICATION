import streamlit as st
import pandas as pd
from supabase import create_client, Client

############################# CONNECTION FUNCTION ###########################
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)
#############################################################################

############################### LOGIN FUNCTION ##############################
def login(supabase_conn, username, password):
    rows = supabase_conn.table("Users").select("*").execute()
    for row in rows.data:
        if username == row["Username"] and password == row["Password"]:
            return True
    return False
##############################################################################

############################## SIGNIN FUNCTION ###############################
def signin(supabase_conn, username, password, mail):
    #check if username or password or mail are empty or contains only whitespaced
    if username == "" or ' ' in username or password == "" or ' ' in password or mail == "" or ' ' in mail:
        return False

    rows = supabase_conn.table("Users").select("*").execute()
    for row in rows.data:
        if username == row["Username"]:
            return False

    supabase_conn.table("Users").insert({"Username":username , "Password":password, "Mail":mail}).execute()
    return True
##############################################################################

############################### SEND MESSAGE FUNC##############################
def send_message(supabase_conn, username, message, time):
    if message == "":
        return False
    supabase_conn.table("Messages").insert({"Content":message, "User":username, "Time":time}).execute()
    return True
##############################################################################

############################ PRINT DATAFRAME FUNC ############################
def get_Database_dataFrame(supabase_conn):
    return pd.DataFrame(supabase_conn.table("Messages").select("*").execute().data)
##############################################################################

############################## DELETE FUNCTION ###############################
def delete_message(supabase_conn, User_to_delete, Time_to_delete):
    supabase_conn.table("Messages").delete().eq('User', User_to_delete).eq('Time', Time_to_delete).execute()
##############################################################################

########################## GET ADMIN INFORMATION #############################
def get_admin_info(supabase_conn, username):
    return pd.DataFrame(supabase_conn.table("Users").select("Admin").eq("Username", username).execute().data)
##############################################################################
