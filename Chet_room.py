import streamlit as st
import pandas as pd
from streamlit_chat import message
import backend as be
from streamlit_autorefresh import st_autorefresh
from urllib.parse import urlparse
from urllib.parse import parse_qs
import datetime

#funzione da invocare per far si che la pagina si aggiorni ogni 1000 millisecondi
#(così le azioni come la stampa dei messaggi vedono i database aggiornati)
#st_autorefresh(interval=1000, key="dataframerefresh")

# funzione da invocare all'inizio per creare connessione al database
supabase=be.init_connection()

#CSS stuff
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
.container{
  max-width: 400px;
  border: 1px solid white;
  border-radius: 5px;
  padding: 5px;
  word-wrap: break-word;
  display: inline-block;
  margin-bottom: 15px;
}

.user{
  font-weight: bold;
  font-size: 15px;
  margin-bottom: 3px;
}

.time{
  font-size: 12px;
  text-align: right;
  margin-top: 3px;
}

.change{
    background-color: #37515F;
    float: right;
}

.no_change{
    background-color: none;
}

</style>
""", unsafe_allow_html=True)

#if "Username" not in st.session_state:
if st.experimental_get_query_params():
    st.session_state["Username"] = st.experimental_get_query_params()["user"]
    st.session_state["Admin"] = st.experimental_get_query_params()["admin"]

st.markdown('<p class="big-font">Chat </p>', unsafe_allow_html=True)

#df_users= pd.read_csv('Chet_users.csv', sep=';')

#with st.sidebar:
#    st.title("Members")
#    for x in df_users.iloc[:,0]:
#        st.write(x)
st.session_state['Message'] = st.text_input("Message")
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
        change_color = "no_change"
        if st.session_state["Username"][0] == series.at["User"]:
            change_color = "change"

        if series.at["Admin"] == True:
            message = '''
                <div class = "container %s">
                  <div class = "user">
                      %s ♚
                  </div>
                  <div class = "content">
                      %s
                  </div>
                  <div class = "time">
                      %s
                  </div>
                </div>
            ''' % (change_color, series.at["User"], series.at["Content"], series.at["Time"])
        else:
            message = '''
                <div class = "container %s">
                  <div class = "user">
                      %s
                  </div>
                  <div class = "content">
                      %s
                  </div>
                  <div class = "time">
                      %s
                  </div>
                </div>
            ''' % (change_color, series.at["User"], series.at["Content"], series.at["Time"])
        st.markdown(message, unsafe_allow_html=True)
