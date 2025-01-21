Advanced Online Examination Cheating Detection Software
An innovative and robust Python-based online examination monitoring solution that ensures exam integrity by detecting and preventing cheating. Built using Streamlit for an intuitive user interface, this project incorporates cutting-edge AI technologies and practical solutions for real-world scenarios.

🚀 Key Features
Real-Time Monitoring

Facial recognition and gaze tracking (or head movement tracking for low-quality cameras) using YOLO and APIs like Azure Face API.
Detects video loopback attempts with temporal analysis and random action prompts.
Tab Movement Restriction

Alerts examiners on tab switching to prevent unauthorized browsing.
Handling Internet Disruptions

Examinees must restart the exam upon disconnection. Progress is periodically saved for resumption after examiner validation.
Device Power Loss Recovery

Autosave mechanisms ensure exam data and monitoring logs are preserved for session restoration.
Workspace Monitoring

Secondary camera support for desk scans and rough paper usage monitoring.
Post-Exam Analysis

AI-driven flagged activity reviews, including gaze patterns, head movements, and workspace anomalies.
Scalable Deployment

Hosted on the cloud for seamless multi-device support and high reliability.
📦 Built With
Python: Core programming language.
Streamlit: Interactive UI for examiners and examinees.
YOLO: Real-time object detection for monitoring.
Azure Face API: Facial recognition and gaze tracking.
MediaRecorder API: Browser-based recording for real-time monitoring.
FFmpeg: Video compression and frame analysis.
🌟 Why Choose This Software?
Cross-device compatibility.
Fallback solutions for low-quality cameras (head movement tracking).
Secure exam environment with scalable cloud hosting.
Modular and easy-to-extend architecture.
📚 How It Works
Before the Exam: Set up monitoring configurations, workspace requirements, and rules via Streamlit.
During the Exam: Monitor real-time activities with tab restriction, workspace tracking, and anti-spoofing measures.
After the Exam: Review flagged activities and suspicious behaviors in a detailed Streamlit dashboard.
🛠 Installation & Setup
Clone this repository:
bash
Copy
Edit
git clone https://github.com/your-username/exam-cheating-detection.git
cd exam-cheating-detection
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:
bash
Copy
Edit
streamlit run app.py
🤝 Contribution
Contributions are welcome! Feel free to submit pull requests or open issues for feature requests, bug reports, or improvements.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
