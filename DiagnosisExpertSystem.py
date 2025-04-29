class DiagnosisExpertSystem:
    def __init__(self):
        # Each disease has **unique symptoms** with no overlap between diseases
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
        # If only one symptom is entered, find diseases that match it
        if len(symptoms) == 1:
            matched_diseases = []
            for disease, disease_symptoms in self.diseases.items():
                if symptoms[0] in disease_symptoms:
                    matched_diseases.append(disease)
            if matched_diseases:
                return f"Possible diseases based on symptom '{symptoms[0]}': {', '.join(matched_diseases)}"
            else:
                return f"No diseases found matching the symptom '{symptoms[0]}'"
        
        # Check symptoms against all diseases for multiple symptoms with a threshold of 2 matches
        for disease, disease_symptoms in self.diseases.items():
            matching_symptoms = [symptom for symptom in symptoms if symptom in disease_symptoms]
            # If 2 or more symptoms match, return the disease
            if len(matching_symptoms) >= 1:  # Adjusted threshold
                return f"Disease: {disease} with symptoms: {', '.join(matching_symptoms)}"
        
        return "Diagnosis unclear" 

# Function to get symptoms from the user
def get_user_input(first_input=True):
    if first_input:
        print("\nWelcome to the Expert Diagnosis System!")
        print("\nPlease provide your symptoms so we can help diagnose your condition.")
        print("\nYou can either type a single symptom or a list of symptoms separated by commas (e.g., 'fever, body ache, fatigue').")
    else:
        print("\nEnter more than one symptom for an accurate diagnosis")

    symptoms_input = input("Enter your symptoms: ").lower().split(',')  # Get input and convert to lowercase
    symptoms_input = [symptom.strip() for symptom in symptoms_input]  # Clean up extra spaces
    return symptoms_input

# Main program execution
if __name__ == "__main__":
    expert_system = DiagnosisExpertSystem()
    
    first_input = True  # Flag to track if it's the first input (show welcome message)
    
    while True:
        # Get symptoms from user (show welcome message if first input, else skip it)
        symptoms_input = get_user_input(first_input)
        
        # Diagnose based on input
        diagnosis = expert_system.diagnose(symptoms_input)
        print(diagnosis)
        
        # Ask user if they want to continue
        print("\nWould you like to enter more symptoms? (yes/no)")
        continue_input = input().lower()
        
        if continue_input != 'yes':
            print("\nThank you for using the expert system!")
            break
        else:
            first_input = False  # After first input, don't show the welcome message again
