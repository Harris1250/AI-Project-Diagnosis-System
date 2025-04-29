from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

class DiagnosisExpertSystem:
    def __init__(self):
        self.diseases = {
            'Flu': ['fever', 'body ache', 'fatigue', 'chills', 'sore throat'],
            'Common Cold': ['runny nose', 'sore throat', 'mild cough', 'sneezing'],
            'COVID-19': ['dry cough', 'loss of taste or smell', 'shortness of breath'],
            'Strep Throat': ['swollen lymph nodes', 'red spots on the roof of mouth', 'painful swallowing'],
            'Sinus Infection': ['sinus pressure', 'headache', 'nasal congestion', 'facial pain'],
            'Pneumonia': ['chest pain', 'coughing up mucus', 'shortness of breath'],
            'Allergies': ['itchy eyes', 'sneezing', 'nasal congestion', 'watery eyes'],
            'Bronchitis': ['persistent cough', 'wheezing', 'chest discomfort'],
            'Mononucleosis': ['swollen lymph nodes', 'extreme fatigue', 'sore throat']
        }

    def diagnose(self, symptoms):
        matches = []
        for disease, disease_symptoms in self.diseases.items():
            matched = [s for s in symptoms if s in disease_symptoms]
            if matched:
                matches.append((disease, matched))
        if not matches:
            return None, []
        matches.sort(key=lambda x: len(x[1]), reverse=True)
        best_match, matched_symptoms = matches[0]
        return best_match, matched_symptoms

expert_system = DiagnosisExpertSystem()

all_symptoms = sorted(list({
    symptom
    for symptoms in expert_system.diseases.values()
    for symptom in symptoms
}))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/diagnose', methods=['GET', 'POST'])
def diagnose():
    diagnosis = None
    matched_symptoms = []
    if request.method == 'POST':
        user_input = request.form.get('symptoms', '').lower()
        symptoms = [s.strip() for s in user_input.split(',') if s.strip()]
        if symptoms:
            diagnosis, matched_symptoms = expert_system.diagnose(symptoms)
        else:
            flash("Please enter at least one symptom.", "error")
    return render_template('index.html', diagnosis=diagnosis, matched=matched_symptoms, all_symptoms=all_symptoms)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/future')
def future():
    return render_template('future.html')

if __name__ == '__main__':
    app.run(debug=True)
