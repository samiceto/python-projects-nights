import streamlit as st 
import random 
import string

def password_generator(lenght,use_digit,use_spacial):
    cheractor = string.ascii_letters

    if use_digit :
        cheractor += string.digits

    if use_spacial:
        cheractor += string.punctuation

    return "".join(random.choice(cheractor) for _ in range(lenght))


st.title("Password Generator")

lenght = st.slider("Select Password lenght", min_value=6, max_value=32, value=12)

use_digit = st.checkbox("Include Digits")
use_spacial = st.checkbox("Include Spacial charectors")

if st.button("Generate Password"):
    Password = password_generator(lenght,use_digit,use_spacial)
    st.write(f"Generated Password is: {Password}")