import streamlit as st
from session_state import get  # Import the session state module
import hashlib

def main():
    # Check if IP address is stored in session state, if not, initialize it
    if 'ip' not in st.session_state:
        st.session_state.ip = st.experimental_get_query_params().get('client_ip', [None])[0]

    # Get the session ID (hash of the user's IP address)
    session_id = hashlib.md5(st.session_state.ip.encode()).hexdigest()

    # Get the user authentication status and username from the session state
    session_state = get(user_authenticated=False, username="", session_id=session_id)
    
    if not session_state.user_authenticated:  # Show login form if not authenticated
        st.title("Please Login")

        # Access usernames and passwords from secrets.toml
        usernames_and_passwords = st.secrets["passwords"]

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in usernames_and_passwords and password == usernames_and_passwords[username]:
                st.success("Login successful")
                session_state.user_authenticated = True
                session_state.username = username
                # Set a browser cookie to store user authentication information
                st.session_state[f"user_authenticated_{session_state.session_id}"] = True
                st.session_state[f"username_{session_state.session_id}"] = username
                st.rerun()
            else:
                st.error("😕 Incorrect username or password")
    else:  # Show the content of the other page if authenticated
        st.title("Homepage")
        st.markdown(f"Welcome, ***{session_state.username}***! to our Streamlit Multipage App")

        markdown_text = """
        Our app is designed to provide a comprehensive solution for managing and analyzing srr data. Whether you're a supervisor handling your team's day-to-day operations, a manager seeking insights and oversight, or an analyst diving deep into the data, we have you covered with our streamlined interface and powerful features.

        Here's a brief overview of what you can expect from each page:

        1. **Homepage**:
        This is your gateway to the app's functionality. From here, you can navigate to the different sections and explore the tools tailored to your needs.

        2. **Agent View**:
        Dive into the agent srr dashboard, where agents can efficiently track and manage service requests. Gain real-time insights into task status, pending requests, and overall performance to optimize workflow and enhance customer satisfaction.

        3. **Management View**:
        Building upon the agent view, the management view provides additional charts and metrics tailored for managerial needs. Gain deeper insights into team performance, resource allocation, and trends over time to make informed decisions and drive operational excellence.

        4. **SRR Analytics Tool**:
        This powerful tool empowers management to explore, transform, and visualize srr data with ease. Utilizing a simple drag-and-drop dashboard interface, users can uncover patterns, identify outliers, and extract valuable insights. Additionally, this page offers basic exploratory data analysis (EDA) to kickstart your data exploration journey.

        Whether you're on the front lines resolving service requests or at the helm steering strategic decisions, our app is here to support you every step of the way. Get ready to unlock the full potential of your srr data and elevate your operational efficiency with our Streamlit multipage app!
        """

        st.markdown(markdown_text)
        # st.write(f"Welcome, {session_state.username}! ")

        if st.button("Log Out"):
            session_state.user_authenticated = False
            session_state.username = ""
            # Clear the browser cookies for user authentication information
            st.session_state[f"user_authenticated_{session_state.session_id}"] = False
            st.session_state[f"username_{session_state.session_id}"] = ""
            st.rerun()

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

