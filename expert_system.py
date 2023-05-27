# Define the knowledge base
knowledge_base = {
    'disease_1': {
        'symptoms': ['fever', 'cough', 'fatigue'],
        'treatment': 'Rest, fluids, and over-the-counter fever reducers',
        'risk_factors': ['Weakened immune system', 'Close contact with an infected person']
    },
    'disease_2': {
        'symptoms': ['headache', 'nausea', 'sensitivity to light'],
        'treatment': 'Pain relievers, rest, and avoiding triggers',
        'risk_factors': ['Family history of migraines', 'Stress']
    },
    'disease_3': {
        'symptoms': ['abdominal pain', 'diarrhea', 'bloody stools'],
        'treatment': 'Antibiotics, fluid replacement, and rest',
        'risk_factors': ['Contaminated food or water', 'Poor sanitation']
    },
    'disease_4': {
        'symptoms': ['shortness of breath', 'wheezing', 'chest tightness'],
        'treatment': 'Bronchodilators, inhaled steroids, and avoiding triggers',
        'risk_factors': ['Allergies', 'Exposure to irritants like smoke or pollution']
    },
    'disease_5': {
        'symptoms': ['joint pain', 'swelling', 'stiffness'],
        'treatment': 'Pain relievers, physical therapy, and lifestyle changes',
        'risk_factors': ['Age (more common in older adults)', 'Genetic factors']
    },
    # Add more diseases and their associated information
}

# Define the inference engine
def diagnose(symptoms):
    possible_diagnoses = []
    for disease, info in knowledge_base.items():
        if any(symptom in symptoms for symptom in info['symptoms']):
            possible_diagnoses.append(disease)
    return possible_diagnoses

# User interface
def get_user_input():
    symptoms = []
    while True:
        symptom = input("Enter a symptom (or 'done' to finish): ")
        if symptom == 'done':
            break
        symptoms.append(symptom)
    return symptoms

def display_diagnosis(diagnoses):
    if len(diagnoses) > 0:
        print('Possible diagnoses:')
        for disease in diagnoses:
            print('- Disease:', disease)
            print('  Symptoms:', knowledge_base[disease]['symptoms'])
            print('  Treatment:', knowledge_base[disease]['treatment'])
            print('  Risk factors:', knowledge_base[disease]['risk_factors'])
            print()
    else:
        print('No matching diagnosis found.')

# Main program
def main():
    symptoms = get_user_input()
    possible_diagnoses = diagnose(symptoms)
    display_diagnosis(possible_diagnoses)

# Run the program
if __name__ == '__main__':
    main()
