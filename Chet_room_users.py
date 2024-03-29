import streamlit as st
import backend as be
from streamlit_autorefresh import st_autorefresh
import datetime
import Chet_login as cl

#function to refresh the page every second
st_autorefresh(interval=1000, key="dataframerefresh")

#initialize database connection
supabase=be.init_connection()

cl.set_background('back4.png')

#styling
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

                    div[class*="stTextInput"] label {
                      font-size: 20px;
                      font-family:  "Courier New", monospace;
                      text-align: Center;
                      color: Orange;
                    }
                </style>
            """, unsafe_allow_html=True)

#...read chet_room_admin.py for comments
if st.experimental_get_query_params():
    value = st.experimental_get_query_params()["value"][0]
st.session_state["Username"] = be.decode_string(value)

st.markdown('<p class="big-font" style="font-family:Courier;color:Orange; font-size: 40px;">Chat </p>', unsafe_allow_html=True)

st.session_state['Message'] = st.text_input("Message:")
button =st.button("Send message")
if button:
    if be.send_message(supabase, st.session_state['Username'] ,st.session_state['Message'], datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        st.session_state['Message'] = ""
    else:
        st.error('Il messaggio non può essere vuoto', icon="🚨")

#since this is the chat room for users we will only be able to send messages
df= be.get_Database_dataFrame(supabase)
if not df.empty:
    for x in reversed(range(len(df.index))):
        series = df.loc[x]
        change_side = "no_change"
        color = "orange"
        border = "border_orange"
        speculare = "no_speculare"
        if st.session_state["Username"] == series.at["User"]:
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
