README - Diagnosis Expert System
--------------------------------

Project Title:
A Rule-Based Expert System for Diagnosing Multiple Diseases Based on Unique Symptoms

Authors:
Muhammad Nadeem & Edward Kane
Department of Computer Science, Georgia State University

--------------------------------
Overview:
This web-based expert system helps users identify possible diseases based on their symptoms.
Each disease has a unique, non-overlapping symptom set. The system uses rule-based logic 
to evaluate matches and display a likely diagnosis or an “unclear” result if matches are insufficient.

The project has been upgraded from a terminal-based Python script to a Flask-powered web application.

--------------------------------
Included Files:

- app.py                           → Main Flask backend code
- templates/
    ├── home.html                  → Landing page
    ├── index.html                 → Diagnosis interface
    ├── about.html                 → Project description
    ├── future.html                → Expansion and AI possibilities
    └── navbar.html                → Reusable navigation bar
- static/
    └── style.css (optional)       → Custom CSS (if not using inline styles)
- UserManual.txt                   → How to run the project
- README.txt                       → This file
- AI-Project-IEEE-NK.pdf           → IEEE research paper
- Diagnosis_System_Presentation.pdf → Final presentation slides

--------------------------------
How to Run:

1. Open your terminal or command prompt

2. Navigate to the project folder:
   cd "C:\Users\User\Documents\AI Diagnosis"

3. Run the Flask application:
   python app.py

4. Open your browser and go to:
   http://127.0.0.1:5000/

5. Use the site:
   - Navigate to the "Diagnose" tab
   - Enter symptoms (e.g., fever, chills, sore throat)
   - View the preliminary diagnosis result

--------------------------------
Contact:

Muhammad Nadeem:  mnadeem2@student.gsu.edu  
Edward Kane:       ekane7@student.gsu.edu