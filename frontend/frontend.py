"""
creo un dataframe fake e printo i messaggi delle varie colonne
"""

import streamlit as st
import pandas as pd
from streamlit_chat import message

user= pd.Series(['ludo:', 'giovba:', 'fede:'])
text= pd.Series(['aaa', 'bbb', 'ccc'])

df = pd.DataFrame({'User': user, 'Text':text})
blankIndex=['']*len(df)
df.index= blankIndex

for x in range(len(df.index)):
    message(message=(df.iloc[[x]].to_string( index=False, header=False)))
    
    
