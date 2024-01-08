import streamlit as st
import csv, os
from datetime import datetime


## user defined function
def log_to_csv(user_input):
    
    file_name = os.path.join(os.getcwd(), 'user_input_log.csv')
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user_input, datetime.now()])

st.title('Website Crawler')
st.title('Package Interface')
user_input = st.text_input('Enter Some text')

if st.button('Say Hello'):
    st.write(f'Hello {user_input}')

    if user_input:
        log_to_csv(user_input)

    st.success('Your input has been logged')

