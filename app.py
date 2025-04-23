import streamlit as st
import requests
import json
import pandas as pd
import random
from datetime import datetime

FIREBASE_API_KEY = "AIzaSyBnjOPY0yWreRdW9dDl9C8F49wnO6WmfEE"

st.set_page_config(page_title="NKFITNESS AI - Full App", layout="wide")

if "email_token" not in st.session_state:
    st.session_state.email_token = None
    st.session_state.email_user = ""

# Firebase Auth Functions
def register_user(email, password):
    res = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"email": email, "password": password, "returnSecureToken": True})
    )
    return res

def login_user(email, password):
    res = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"email": email, "password": password, "returnSecureToken": True})
    )
    return res

# Login/Register UI
if not st.session_state.email_token:
    st.title("NKFITNESS AI - Email Login")
    mode = st.radio("Choose:", ["Login", "Register"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button(mode):
        if mode == "Register":
            response = register_user(email, password)
            if response.status_code == 200:
                st.success("User registered! You can now log in.")
            else:
                st.error(response.json()["error"]["message"])
        else:
            response = login_user(email, password)
            if response.status_code == 200:
                st.session_state.email_token = response.json()["idToken"]
                st.session_state.email_user = email
                st.success(f"Welcome, {email}")
            else:
                st.error(response.json()["error"]["message"])
    st.stop()

# Main app once logged in
st.sidebar.title("Welcome!")
st.sidebar.markdown(f"**Logged in as:** `{st.session_state.email_user}`")
tabs = st.sidebar.radio("Navigate to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

goal = st.sidebar.selectbox("Select your fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
level = st.sidebar.radio("Choose your level:", ["Beginner", "Intermediate", "Advanced"])
diet_type = st.sidebar.radio("Diet Type:", ["Veg", "Non-Veg"])

# --- Workout Section ---
muscle_groups = {
    "Chest": ["Flat Bench Press", "Incline Dumbbell Press", "Chest Fly", "Cable Crossovers", "Push-ups",
              "Decline Bench Press", "Dips", "Pec Deck", "Smith Machine Press", "Incline Barbell Press"],
    "Biceps": ["Barbell Curl", "Dumbbell Curl", "Hammer Curl", "Preacher Curl", "EZ Bar Curl",
               "Concentration Curl", "Cable Curl", "Zottman Curl", "Incline Curl", "Reverse Curl"],
    "Triceps": ["Skull Crushers", "Triceps Pushdowns", "Overhead Extensions", "Close-Grip Bench",
                "Dips", "Kickbacks", "Rope Pushdowns", "Diamond Push-ups", "Machine Press", "Reverse Pushdowns"],
    "Shoulders": ["Overhead Press", "Lateral Raise", "Front Raise", "Reverse Fly", "Arnold Press",
                  "Barbell Press", "Cable Raise", "Shrugs", "Face Pulls", "Machine Press"],
    "Back": ["Deadlifts", "Pull-ups", "Barbell Rows", "Lat Pulldowns", "Seated Row",
             "T-Bar Row", "Cable Row", "Dumbbell Row", "Good Mornings", "Hyperextensions"],
    "Legs": ["Squats", "Leg Press", "Lunges", "Leg Extensions", "Hamstring Curls",
             "Romanian Deadlifts", "Walking Lunges", "Goblet Squats", "Hip Thrusts", "Calf Raises"],
    "Core": ["Plank", "Crunches", "Leg Raises", "Russian Twists", "Mountain Climbers",
             "V-Ups", "Cable Crunch", "Bicycle Crunches", "Toe Touches", "Hanging Leg Raises"]
}

if tabs == "Workout Plan":
    st.title("Workout Plan by Muscle Group")
    for group, exercises in muscle_groups.items():
        st.subheader(group)
        for i, ex in enumerate(exercises, 1):
            st.markdown(f"**{i}.** {ex}")

# --- Diet Section ---
diets = {
    "Lose Weight": {
        "Veg": ["Oats + Fruits", "Lentils + Salad", "Green Tea"],
        "Non-Veg": ["Boiled eggs", "Grilled chicken + Veggies", "Yogurt"]
    },
    "Gain Muscle": {
        "Veg": ["Paneer + Rice", "Protein shake", "Tofu wraps"],
        "Non-Veg": ["Egg whites", "Chicken breast + Rice", "Fish curry"]
    },
    "Maintain Fitness": {
        "Veg": ["Upma + Nuts", "Chapati + Daal", "Fruit smoothie"],
        "Non-Veg": ["Egg sandwich", "Grilled fish + Veggies", "Milk"]
    }
}

if tabs == "Diet Plan":
    st.title(f"{diet_type} Diet Plan for {goal}")
    for item in diets[goal][diet_type]:
        st.markdown(f"- {item}")

# --- Progress Tracker ---
elif tabs == "Progress Tracker":
    st.title("Progress Tracker")
    weight = st.number_input("Weight (kg):", min_value=30, max_value=200, value=70)
    height = st.number_input("Height (cm):", min_value=100, max_value=250, value=170)
    bmi = round(weight / ((height / 100) ** 2), 1)
    st.success(f"Your BMI is: {bmi}")

    st.subheader("Weekly Calorie Burn")
    cal_df = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, 8)],
        "Calories Burned": [random.randint(200, 600) for _ in range(7)]
    })
    st.line_chart(cal_df.set_index("Day"))

    if st.button("Save Progress"):
        with open("progress_log.txt", "a") as f:
            f.write(f"{datetime.now()} | {st.session_state.email_user} | Weight: {weight}kg | Height: {height}cm | BMI: {bmi}\n")
        st.success("Progress saved!")

# --- Motivation Tab ---
elif tabs == "Motivation":
    st.title("Daily Motivation")
    st.markdown("**FOR MOTIVATION: GO WATCH NISHANK'S SHIRTLESS PHOTOS.**")
    quotes = [
        "No excuses, just results!",
        "Progress, not perfection.",
        "The only bad workout is the one you didn’t do.",
        "Push harder than yesterday.",
        "Discipline beats motivation."
    ]
    st.info(random.choice(quotes))

st.markdown("---")
st.markdown("Made with 💪 by NKFITNESS-AI")
