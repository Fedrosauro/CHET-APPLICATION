import streamlit as st
import backend as be
import base64

supabase = be.init_connection()

st.set_page_config( page_title="CHET", page_icon=💬, layout="centered")

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
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

# funzione che:
# se credenziali giuste reindirizza alla chats
# se credenziali errate messaggio d'errore
def check_login():
    if be.login(supabase, st.session_state["Username"], st.session_state["Password"]):
        admin_value = be.get_admin_info(supabase, st.session_state["Username"]).loc[0].at["Admin"]
        placeholder.empty()
        st.write(f'''
            <p style="font-family:Courier;color:Orange; font-size: 20px;">Ciao %s!</p>
            '''% (st.session_state["Username"]),
                      unsafe_allow_html=True
                )

        encoded_name = be.encode_string(st.session_state["Username"])
        if admin_value == True:
            chat_botton = st.write(f'''
                          <a href="https://fedrosauro-chet-application-chet-room-admin-7dtfqu.streamlit.app/?value=%s">
                          <button>
                          VAI ALLA CHAT
                          </button>
                          </a>
                          ''' % (encoded_name),
                          unsafe_allow_html=True
                          )
        else:
            chat_botton = st.write(f'''
                          <a href="https://fedrosauro-chet-application-chet-room-users-kdnlq9.streamlit.app/?value=%s">
                          <button>
                          VAI ALLA CHAT
                          </button>
                          </a>
                          ''' % (encoded_name),
                          unsafe_allow_html=True
                          )
    else:
        st.error('Username e/o password errati', icon="🚨")


set_background('back3.png')

tabs_font_css = """
<style>
div[class*="stTextInput"] label {
  font-size: 20px;
  font-family: "Courier New", monospace;
  text-align: Center;
  color: Orange;

}

div[class*="stTextInput"] label {
  font-size: 20px;
  font-family:  "Courier New", monospace;
  text-align: Center;
  color: Orange;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

for i in range(5):
        st.write("")

placeholder = st.empty()
with placeholder.container():
    with st.form("my_form"):
        st.session_state['Username'] = st.text_input("Username:")
        st.session_state['Password'] = st.text_input("Password:", type="password")
        b1 = st.form_submit_button("LOGIN")
        registrarsi ='<p style="font-family:Courier;color:Orange; font-size: 20px;">Non sei ancora registrato?</p>'
        st.markdown(registrarsi, unsafe_allow_html=True)
        b2 = st.form_submit_button("SIGN IN")
if b1:
    check_login()
if b2:
    nav_to("https://fedrosauro-chet-application-chet-signin-jaygim.streamlitapp.com/")
