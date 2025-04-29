Welcome to the AI-Project-Diagnosis-System – a simple, lightweight web application that simulates an expert system for diagnosing diseases based on symptoms.

This project was developed to demonstrate how rule-based AI can be applied to healthcare diagnosis using clear symptom-disease mappings without complex machine learning.


🧠 How It Works
The system uses a rule-based approach (no ML training required).

Users input their symptoms through a clean web interface.

Based on unique symptoms provided, the system suggests a possible diagnosis.

Each disease has a distinct set of symptoms to avoid overlap and ensure clarity.


⚙️ Technologies Used
Python (Flask) – backend server and routing

HTML/CSS – frontend design

JavaScript – basic interactivity

Bootstrap – styling and responsiveness

Rule-based logic – symptom-to-disease matching


📂 Project Structure

AI-Project-Diagnosis-System/
│
├── app.py               # Main Flask application
├── templates/
│   └── index.html        # Main webpage layout
├── static/
│   ├── style.css         # Custom styles
│   └── script.js         # JavaScript functionality
├── requirements.txt      # Python package dependencies
├── User_Manual.pdf       # Instructions for users
├── IEEE_Paper.pdf        # Project research paper (IEEE format)
├── Presentation_Slides.pptx # Final project presentation
└── README.md             # This file


🖥️ How to Run Locally
Clone this repository:

git clone https://github.com/Harris1250/AI-Project-Diagnosis-System.git
cd AI-Project-Diagnosis-System
Install dependencies:

pip install -r requirements.txt
Run the app:

python app.py
Open your browser and go to:


http://127.0.0.1:5000


💡 Example Diseases Covered
Flu – Fever, Body Ache, Fatigue, etc.

Common Cold – Runny Nose, Sneezing, etc.

COVID-19 – Loss of Taste/Smell, Shortness of Breath, etc.

Sinus Infection, Pneumonia, Allergies, Bronchitis, Strep Throat, and Mononucleosis – all with unique symptom sets.


📄 Additional Resources
📖 User Manual – Learn how to use the system effectively.

📚 IEEE Paper – In-depth technical documentation.

🎥 Presentation Slides – Quick overview of the system's design and functionality.


📬 Contact
If you have questions or feedback, feel free to reach out!

GitHub: Harris1250

🚀 Try it yourself and explore the power of simple AI diagnosis!
