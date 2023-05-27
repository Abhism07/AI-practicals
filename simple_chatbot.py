# Define the chatbot's responses based on user input
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I assist you?"

    if "how are you" in user_input:
        return "I'm good, thank you! How about you?"
    
    if "head pain" in user_input or "headache" in user_input:
        return "Headaches can be caused by various factors such as tension, migraines, or sinus problems. It's important to consult a healthcare professional for a proper diagnosis and treatment."
    
    if "cure" in user_input or "homemade remedy" in user_input or "homemade treatment" in user_input :
        return "Rest in a quiet, dark room,Apply a cold or warm compress,Stay hydrated,Get some sleep,Manage stress."
    
    if "cough" in user_input or "coughing" in user_input:
        return "Coughing can be caused by several factors, including respiratory infections, allergies, or even acid reflux. If you have a persistent cough or other concerning symptoms, it's best to seek medical advice."
    
    if "fever" in user_input or "temperature" in user_input:
        return "Fever is often a sign of an underlying infection. It's advisable to monitor your temperature and consult a doctor if it persists or is accompanied by other symptoms."
       "\nSymptoms - Elevated body temperature, often indicating an underlying infection or inflammatory condition."
    
    if "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"

    return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Chatbot interaction loop
while True:
    user_input = input("User: ")
    bot_response = get_bot_response(user_input)
    print("Chatbot:", bot_response)
