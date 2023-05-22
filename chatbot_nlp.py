import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi, how can I assist you with medical information today?"]
    ],
    [
        r"how are you ?",
        ["I'm just a machine, but I'm here to help you. How can I assist you today?"]
    ],
    [
        r"(.*) (headache|head pain) ?",
        ["Headaches can be caused by various factors such as tension, migraines, or sinus problems. It's important to consult a healthcare professional for a proper diagnosis and treatment."]
    ],
    [
        r"(.*)(homemade treatment|cure|remedy|homemade remedies|remedies at home)",
        ["Rest in a quiet, dark room,Apply a cold or warm compress,Stay hydrated,Get some sleep,Manage stress."]
    ],
    [
        r"(.*) (fever|temperature) ?",
        ["Fever is often a sign of an underlying infection. It's advisable to monitor your temperature and consult a doctor if it persists or is accompanied by other symptoms."
       "\nSymptoms - Elevated body temperature, often indicating an underlying infection or inflammatory condition."],
       
    ],
    [
        r"(.*) (cough|coughing) ?",
        ["Coughing can be caused by several factors, including respiratory infections, allergies, or even acid reflux. If you have a persistent cough or other concerning symptoms, it's best to seek medical advice."]
    ],
    [
        r"(.*) (thank you|thanks) ?",
        ["You're welcome!", "Glad I could help!", "No problem! If you have any more questions, feel free to ask."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I'm not qualified to provide medical advice. It's important to consult a healthcare professional for accurate information regarding your specific condition."]
    ]
    
]

# Create the chatbot
def create_chatbot():
    chatbot = Chat(pairs, reflections)
    print("Medical Chatbot created successfully!")
    return chatbot

# Run the chatbot
def run_chatbot():
    chatbot = create_chatbot()
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        response = chatbot.respond(user_input)
        print(response)
# Run the chatbot program
if __name__ == "__main__":
    nltk.download("punkt")
    run_chatbot()
