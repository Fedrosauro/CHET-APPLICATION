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
    rows = supabase_conn.table("Messages").select("*").execute()
    for row in rows.data:
        if User_to_delete == row["User"] and Time_to_delete==row["Time"]:
            supabase_conn.table("Messages").delete().eq('User', User_to_delete).eq('Time', Time_to_delete).execute()
            return True

    return False
##############################################################################

########################## GET ADMIN INFORMATION #############################
def get_admin_info(supabase_conn, username):
    return pd.DataFrame(supabase_conn.table("Users").select("Admin").eq("Username", username).execute().data)
##############################################################################

############################# ENCODING STRINGS ###############################
def encode_string(string):
   encode_str = ""
   for c in string:
       if len(str(ord(c))) == 2:
           encode_str += "0" + str(ord(c))
       else:
           encode_str += str(ord(c))
   return encode_str
##############################################################################

############################# DECODING STRINGS ###############################
def decode_string(string):
    decode_str = ""
    iterations = len(string)//3
    my_list = []

    for i in range(iterations):
        character = ""
        for j in range(3):
            character += string[(i * 3) + j]
        my_list.append(character)

    for item in my_list:
        if item[0] == "0":
            item = item[1:]
        decode_str += chr(int(item))

    return decode_str
##############################################################################
