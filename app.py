import streamlit as st

def main():
    st.title("Online Examination Cheating Detection")
    st.sidebar.title("Navigation")
    
    options = ["Home", "Real-Time Monitoring", "Post-Exam Analysis"]
    choice = st.sidebar.selectbox("Choose an option:", options)
    
    if choice == "Home":
        st.write("Welcome to the Cheating Detection System. Select an option from the sidebar.")
    elif choice == "Real-Time Monitoring":
        st.write("Real-Time Monitoring will be implemented here.")
    elif choice == "Post-Exam Analysis":
        st.write("Post-Exam Analysis will be implemented here.")

if __name__ == "__main__":
    main()
