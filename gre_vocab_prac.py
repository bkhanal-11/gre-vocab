import streamlit as st
import json
import random

st.set_page_config(
    page_title="GRE Vocab",
    page_icon="🕹️",
    layout="centered"
)

def meaning_func():
    st.title('Welcome to GRE Vocab Practice')

    st.write('\n')
    st.write(f"{st.session_state.key}: {flashcard[st.session_state.key]['meaning']}")

def next_func():
    st.title('Welcome to GRE Vocab Practice')

    st.write('\n')
    rand = random.randint(0, total_words - 1)
    st.session_state.key = flashcard_list[rand]
    while flashcard[st.session_state.key]['meaning'] == '':
        rand = random.randint(0, total_words - 1)
        st.session_state.key = flashcard_list[rand]
    st.write(st.session_state.key)



with open('assets/flashcard_new.json') as f:
    flashcard = json.load(f)

flashcard_list = list(flashcard)
total_words = len(flashcard)

if 'key' not in st.session_state:
    st.title('Welcome to GRE Vocab Practice')

    st.write('\n')
    
    rand = random.randint(0, total_words - 1)
    st.session_state.key = flashcard_list[rand]
    while flashcard[st.session_state.key]['meaning'] == '':
        rand = random.randint(0, total_words - 1)
        st.session_state.key = flashcard_list[rand]
    st.write(st.session_state.key)

col1, col2 = st.columns(2)
with col1:
    st.button("Meaning", on_click=meaning_func)
with col2:
    st.button("Next", on_click=next_func)
