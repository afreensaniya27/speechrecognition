from main import recognize_speech

import streamlit as st

st.title("Speech recognition app")

st.write("speak now")
to_write=recognize_speech()

st.write(f"you spoke : {to_write}")




