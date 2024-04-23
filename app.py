import streamlit as st
import shelve
from generate_responses import generate_response_action
def User():
    def user_login():
        st.title("User Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Add your login logic here
            st.success("Logged in as User!")

    def user_register():
        st.title("User Register")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            # Add your registration logic here
            st.success("Registered as User!")

    st.sidebar.title("User")
    option = st.sidebar.radio("Select Option", ["Login", "Register"])
    if option == "Login":
        return user_login()
    elif option == "Register":
        return user_register()


def Doctor():
    def doctor_login():
        st.title("Doctor Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Add your login logic here
            st.success("Logged in as Doctor!")

    def doctor_register():
        st.title("Doctor Register")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            # Add your registration logic here
            st.success("Registered as Doctor!")

    st.sidebar.title("Doctor")
    option = st.sidebar.radio("Select Option", ["Login", "Register"])
    if option == "Login":
        return doctor_login()
    elif option == "Register":
        return doctor_register()

def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

# Function to save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()



def Assistance():
    st.title("Mental Health Support Chatbot")


    prompt = st.chat_input("Enter a prompt here")
    response = generate_response_action(prompt)
    USER = "user"
    ASSISTANT = "assistant"

    if prompt:
        # Save user input to chat history
        st.session_state.messages.append({"role": USER, "content": prompt})
        st.session_state.messages.append({"role": ASSISTANT, "content": response})
        save_chat_history(st.session_state.messages)

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == USER:
            st.chat_message(USER).write(f"{message['content']}")
        elif message["role"] == ASSISTANT:
            st.chat_message(ASSISTANT).write(f" {message['content']}")
def main():
    st.sidebar.title("Menu")
    option = st.sidebar.radio("Select Option", ["User", "Doctor", "AI Assistance"])

    if option == "User":
        User()
    elif option == "Doctor":
        Doctor()
    elif option == "AI Assistance":
        Assistance()


if __name__ == "__main__":
    main()
