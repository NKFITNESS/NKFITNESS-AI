import streamlit as st
import pyrebase
import pandas as pd
import random
from datetime import datetime

# FIREBASE CONFIG
firebaseConfig = {
    "apiKey": "AIzaSyBnjOPY0yWreRdW9dD9l9G8F49wnO6WmfE",
    "authDomain": "nkfitnessai.firebaseapp.com",
    "projectId": "nkfitnessai",
    "storageBucket": "nkfitnessai.appspot.com",
    "messagingSenderId": "YOUR_SENDER_ID",
    "appId": "YOUR_APP_ID",
    "databaseURL": ""
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# LOGIN SECTION
st.title("NKFITNESS AI - Email Login")
auth_mode = st.radio("Choose:", ["Login", "Register"])
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if auth_mode == "Register":
    if st.button("Register"):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("Registered successfully. You can now log in.")
        except:
            st.error("Registration failed. Try a different email.")
else:
    if st.button("Login"):
        try:
            auth.sign_in_with_email_and_password(email, password)
            st.success("Login successful!")
        except:
            st.error("Login failed. Please check your credentials.")

# IF LOGGED IN, CONTINUE
if st.session_state.get("Authentication Successful") or auth_mode == "Login":
    st.title("Welcome to NKFITNESS AI!")
    name = st.text_input("Enter your name")
    goal = st.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
    level = st.radio("Select Your Level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Generate Workout Plan"):
        st.success(f"{name}, here's your custom workout plan to {goal.lower()} at {level.lower()} level.")

        muscle_groups = {
            "Chest": [("Bench Press", "https://youtu.be/gRVjAtPip0Y"),
                      ("Incline Press", "https://youtu.be/8iPEnn-ltC8"),
                      ("Push-Ups", "https://youtu.be/_l3ySVKYVJ8"),
                      ("Chest Fly", "https://youtu.be/eozdVDA78K0")],
            "Biceps": [("Barbell Curl", "https://youtu.be/kwG2ipFRgfo"),
                       ("Hammer Curl", "https://youtu.be/zC3nLlEvin4"),
                       ("Concentration Curl", "https://youtu.be/soxrZlIl35U")],
            "Triceps": [("Dips", "https://youtu.be/2z8JmcrW-As"),
                        ("Tricep Pushdown", "https://youtu.be/vB5OHsJ3EME"),
                        ("Skull Crushers", "https://youtu.be/d_KZxkY_0cM")],
            "Shoulders": [("Overhead Press", "https://youtu.be/2yjwXTZQDDI"),
                          ("Lateral Raise", "https://youtu.be/kDqklk1ZESo"),
                          ("Shrugs", "https://youtu.be/NUmGRzITZZ0")],
            "Legs": [("Squats", "https://youtu.be/aclHkVaku9U"),
                     ("Lunges", "https://youtu.be/QOVaHwm-Q6U"),
                     ("Leg Press", "https://youtu.be/IZxyjW7MPJQ")],
            "Core": [("Plank", "https://youtu.be/pSHjTRCQxIw"),
                     ("Crunches", "https://youtu.be/Xyd_fa5zoEU"),
                     ("Russian Twists", "https://youtu.be/wkD8rjkodUI")]
        }

        for muscle, exercises in muscle_groups.items():
            st.subheader(muscle)
            for exercise, link in exercises:
                st.markdown(f"- [{exercise}]({link})")

        # Diet Plan
        st.subheader("Sample Diet Plan")
        if goal == "Gain Muscle":
            st.write("- Breakfast: Eggs, toast, peanut butter")
            st.write("- Lunch: Chicken breast + rice")
            st.write("- Dinner: Salmon + potatoes + broccoli")
        elif goal == "Lose Weight":
            st.write("- Breakfast: Oats + fruit")
            st.write("- Lunch: Grilled chicken salad")
            st.write("- Dinner: Steamed veggies + lentils")
        else:
            st.write("- Balanced diet with moderate carbs, protein, and veggies")

        # Motivation
        st.subheader("Motivation")
        st.success("FOR MOTIVATION: WATCH NISHANK’S SHIRTLESS PHOTOS.")
