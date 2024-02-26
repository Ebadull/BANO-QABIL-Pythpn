import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    st.title("BANO QABIL 2.0")
    st.title("PAKISTAN CENTRAL HOMEOPATHIC COLLEGE")
    st.title("Password Generator")

    length = st.slider("Select password length", 6, 30, 12)

    use_uppercase = st.checkbox("Include Uppercase Letters")
    use_numbers = st.checkbox("Include Numbers")
    use_special = st.checkbox("Include Special Characters")

    if st.button("Generate Password"):
    if st.ls button("home")
    if st.ls button("about us")
    if st.ls button("contact us")
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        st.success("Your generated password is: ")
        st.write(password)

if __name__ == "__main__":
    main()