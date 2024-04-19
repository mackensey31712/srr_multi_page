import streamlit as st

def main():
    session_state = SessionState.get(user_authenticated=False, username="")

    if not session_state.user_authenticated:
        # Show the login form
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in ["mac", "Amfi", "Jag", "Henry"] and password == st.secrets["passwords"][username]:
                session_state.username = username
                session_state.user_authenticated = True
                st.success("Login successful")
            else:
                st.error("Invalid username or password")
    else:
        # Show the authenticated content
        st.title(f"Welcome, {session_state.username}!")
        st.markdown("Authenticated content goes here")
        if st.button("Log out"):
            session_state.user_authenticated = False
            session_state.username = ""

if __name__ == "__main__":
    main()



# import streamlit as st

# import hmac

# st.set_page_config(
#     page_title="SRR Homepage",
#     page_icon="👋"
# )

# def check_password():
#     """Returns `True` if the user had a correct password."""

#     def login_form():
#         """Form with widgets to collect user information"""
#         with st.form("Credentials"):
#             st.text_input("Username", key="username")
#             st.text_input("Password", type="password", key="password")
#             st.form_submit_button("Log in", on_click=password_entered)

#     def password_entered():
#         """Checks whether a password entered by the user is correct."""
#         if st.session_state["username"] in st.secrets[
#             "passwords"
#         ] and hmac.compare_digest(
#             st.session_state["password"],
#             st.secrets.passwords[st.session_state["username"]],
#         ):
#             st.session_state["password_correct"] = True
#             del st.session_state["password"]  # Don't store the username or password.
#             del st.session_state["username"]
#         else:
#             st.session_state["password_correct"] = False

#     # Return True if the username + password is validated.
#     if st.session_state.get("password_correct", False):
#         return True

#     # Show inputs for username + password.
#     login_form()
#     if "password_correct" in st.session_state:
#         st.error("😕 User not known or password incorrect")
#     return False


# if not check_password():
#     st.stop()


# st.header("Welcome to my Streamlit DA Projects")
# st.sidebar.success("Select a page above.")

# st.write(":point_left: Browse through my projects")

