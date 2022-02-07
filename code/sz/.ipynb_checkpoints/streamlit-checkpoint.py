import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st

st.title('Project 5')

st.write('Moding climate')

page = st.sidebar.selectbox(
    'asdf',
    ('Stuff', 'More Stuff', 'Even more')
)

if page == 'Stuff':
    st.subheader('About this project')
    st.write('''
This is the one
    ''')

elif page == 'More Stuff':
    # header
    st.subheader('Maybe plot time')
    st.write('''We made these''')


elif page == 'Even more':
    st.subheader('Yes?')

    st.write('''
idk really
    ''')
