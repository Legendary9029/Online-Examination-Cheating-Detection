import streamlit as st
from utils.tab_monitor import monitor_tab_switch
from utils.video_analysis import real_time_monitoring
from utils.internet_monitor import check_internet_connection
from utils.workspace import monitor_workspace
from flask import Flask, request, jsonify
import threading
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# Flask app for backend
app_backend = Flask(__name__)

@app_backend.route('/tab_switch', methods=['POST'])
def log_tab_switch():
    try:
        data = request.json
        timestamp = data.get("timestamp")
        if not timestamp:
            return jsonify({"status": "error", "message": "Invalid payload"}), 400
        
        # Write tab switch event to log file
        with open("tab_switch_log.txt", "a") as log_file:
            log_file.write(f"Tab switched at {timestamp}\n")
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Run Flask server in a separate thread
def run_flask():
    app_backend.run(port=5000, debug=False, use_reloader=False)

threading.Thread(target=run_flask, daemon=True).start()

# Streamlit app
def main():
    st.title("Online Examination Cheating Detection")

    # Introduction and instructions
    st.write(
        "This system integrates multiple features to ensure minimal cheating in online examinations. "
        "All features are activated simultaneously for maximum effectiveness."
    )

    # Display all active features
    st.subheader("Active Features")
    st.write("- **Real-Time Monitoring**: Monitors video feed for cheating attempts.")
    st.write("- **Tab Movement Restriction**: Alerts on switching tabs.")
    st.write("- **Internet Connection Monitoring**: Notifies on internet disconnection.")
    st.write("- **Workspace Monitoring**: Ensures no unauthorized items in the workspace.")

    # Activate all features
    st.write("---")
    st.header("Feature Outputs")

    # Run Real-Time Monitoring
    st.subheader("1. Real-Time Monitoring")
    try:
        real_time_monitoring()
    except Exception as e:
        st.error(f"Error in Real-Time Monitoring: {e}")

    # Run Tab Movement Restriction
    st.subheader("2. Tab Movement Restriction")
    try:
        monitor_tab_switch()
    except Exception as e:
        st.error(f"Error in Tab Movement Restriction: {e}")

    # Run Internet Connection Monitoring
    st.subheader("3. Internet Connection Monitoring")
    try:
        check_internet_connection()
    except Exception as e:
        st.error(f"Error in Internet Connection Monitoring: {e}")

    # Run Workspace Monitoring
    st.subheader("4. Workspace Monitoring")
    try:
        monitor_workspace()
    except Exception as e:
        st.error(f"Error in Workspace Monitoring: {e}")

if __name__ == "__main__":
    main()
