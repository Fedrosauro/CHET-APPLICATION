import streamlit as st
import pandas as pd
from streamlit_chat import message
import backend as be
from streamlit_autorefresh import st_autorefresh
from urllib.parse import urlparse
from urllib.parse import parse_qs
import datetime
import base64

st.markdown("""
        <style>
               .css-1n76uvr {
                    margin-top: -150px;
                }
        </style>
        """, unsafe_allow_html=True)

#funzione da invocare per far si che la pagina si aggiorni ogni 1000 millisecondi
#(così le azioni come la stampa dei messaggi vedono i database aggiornati)
st_autorefresh(interval=1000, key="dataframerefresh")

# funzione da invocare all'inizio per creare connessione al database
supabase=be.init_connection()

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

set_background('back4.png')

#CSS stuff
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}

.container{
  max-width: 400px;
  padding: 5px;
  word-wrap: break-word;
  display: inline-block;
  margin-bottom: 15px;
}

.user{
  font-weight: bold;
  font-size: 15px;
  margin-bottom: 3px;
  color:orange;
}

.time{
  font-size: 12px;
  text-align: right;
  margin-top: 3px;
  color:orange;
}

.change{
    float: right;
}

.no_change{

}

.white{
    color: white;
}

.orange{
    color: orange;
}

.border_white{
    border: 1px solid white;
    border-radius: 5px;
}

.border_orange{
    border: 1px solid orange;
    border-radius: 5px;
}

.speculare{
    color:orange;
}

.no_speculare{
    color:white;
}

</style>
""", unsafe_allow_html=True)

tabs_font_css = """
<style>
div[class*="stTextInput"] label {
  font-size: 20px;
  font-family:  "Courier New", monospace;
  text-align: Center;
  color: Orange;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)


#if "Username" not in st.session_state:
if st.experimental_get_query_params():
    st.session_state["Username"] = st.experimental_get_query_params()["user"]

st.markdown('<p class="big-font" style="font-family:Courier;color:Orange; font-size: 40px;">Chat </p>', unsafe_allow_html=True)

st.session_state['Message'] = st.text_input("Message:")
button =st.button("Send message")
if button:
    #quando viene premuto il tasto invia messaggio deve essere invocata la funzione send message e successivamente svuotato st.session_state['Message']
    #come qui
    if be.send_message(supabase, st.session_state['Username'][0] ,st.session_state['Message'], str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))):
        st.session_state['Message'] = ""
    else:
        st.error('Il messaggio non può essere vuoto', icon="🚨")

df= be.get_Database_dataFrame(supabase)
if not df.empty:
    for x in reversed(range(len(df.index))):
        series = df.loc[x]
        change_side = "no_change"
        color = "orange"
        border = "border_orange"
        speculare = "no_speculare"
        if st.session_state["Username"][0] == series.at["User"]:
            change_side = "change"
            color = "white"
            border = "border_white"
            speculare = "speculare"

        message = '''
            <div class = "container %s %s">
              <div class = "user %s">
                      %s
              </div>
              <div class = "%s">
                      %s
              </div>
              <div class = "time %s">
                      %s
              </div>
            </div>
            ''' % (border, change_side, color, series.at["User"], speculare, series.at["Content"], color, series.at["Time"])
        st.markdown(message, unsafe_allow_html=True)