# -*- coding: utf-8 -*-
"""CampusBuddy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1slsQLXwKEkGJmnkXGVeUc1d_Xzua5A4_
"""

import time

# Function to generate responses based on user input
def get_response(user_input):
    user_input = user_input.lower().strip()

    # logic for handeling qn and answers
    if "hours" in user_input or "timings" in user_input or "open" in user_input:
        return "🕘 Our college is open Monday to Saturday from 9 AM to 5 PM."

    elif "courses" in user_input or "programs" in user_input or "branches" in user_input:
        return ("🎓 I love that you’re curious about our programs!\n"
                "We offer B.Tech, M.Tech, MBA, and PhD programs across various disciplines.\n"
                "🔗 For more details: https://rbunagpur.in/programs-offered/")

    elif "location" in user_input or "where" in user_input or "address" in user_input:
        return "📍 The college is located in TechPark City, near the Central Railway Station."

    elif "admission" in user_input or "apply" in user_input or "join" in user_input:
        return ("📝 That’s one of our most asked questions! Here's the info...\n"
                "Admissions are open! Apply through our website: https://rbunagpur.in/admission-process/\n"
                "Or visit the admission office on campus.")

    elif "contact" in user_input or "phone" in user_input or "email" in user_input:
        return "📞 You can find all our contact info here: https://rbunagpur.in/contact/"

    elif "bye" in user_input or "exit" in user_input or "thank" in user_input:
        return "exit"

    else:
        # Log unanswered question to a file
        with open("unanswered_questions.txt", "a") as log_file:
            log_file.write(user_input + "\n")
        return ("🤔 Sorry, I don’t have information on that yet. "
                "Try asking something about admissions, courses, or contact details.")

# Main chatbot function
def chatbot():
    print("Hi there! 🎓 I’m CampusBuddy, your virtual college assistant.")
    print("Ask me anything about our college! (Type 'bye' or 'exit' to end)\n")

    # personalized user name for better interaction
    user_name = input("Please enter your name: ")
    print(f"\nWelcome, {user_name}! Let's get started.\n")

    while True:
        user_input = input(f"{user_name}: ")
        time.sleep(0.5)  # Simulate typing delay

        response = get_response(user_input)

        if response == "exit":
            print(f"CampusBuddy: 👋 Bye, {user_name}! It was great chatting with you. Good luck with your future!")
            break
        else:
            print(f"CampusBuddy: {response}")

# Run chatbot
if __name__ == "__main__":
    chatbot()

