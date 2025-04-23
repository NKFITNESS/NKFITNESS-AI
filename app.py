import streamlit as st  
import requests  
import json  
import pandas as pd  
import random  
from datetime import datetime

FIREBASE_API_KEY = "YOUR_FIREBASE_KEY"

# ---------------- Session ----------------
if "email_token" not in st.session_state:
    st.session_state.email_token = None
    st.session_state.email_user = ""

# ---------------- Auth ----------------
def register_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
    return requests.post(url, json={"email": email, "password": password, "returnSecureToken": True})

def login_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    return requests.post(url, json={"email": email, "password": password, "returnSecureToken": True})

# ---------------- Login UI ----------------
if not st.session_state.email_token:
    st.title("NKFITNESS AI - Email Login")
    mode = st.radio("Choose:", ["Login", "Register"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button(mode):
        response = register_user(email, password) if mode == "Register" else login_user(email, password)
        if response.status_code == 200:
            st.session_state.email_token = response.json()["idToken"]
            st.session_state.email_user = email
            st.success(f"Welcome, {email}")
        else:
            st.error(response.json()["error"]["message"])
    st.stop()

# ---------------- App Tabs ----------------
st.set_page_config(page_title="NKFITNESS AI", layout="wide")
st.sidebar.title("Welcome!")
st.sidebar.markdown(f"**Logged in as:** `{st.session_state.email_user}`")
tabs = st.sidebar.radio("Navigate to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])
goal = st.sidebar.selectbox("Fitness Goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
level = st.sidebar.radio("Fitness Level:", ["Beginner", "Intermediate", "Advanced"])
diet_type = st.sidebar.radio("Diet Type:", ["Veg", "Non-Veg"])

# ---------------- Video Links ----------------
video_links = {
    "Flat Bench Press": "https://youtu.be/gRVjAtPip0Y",
    "Incline Dumbbell Press": "https://youtu.be/8iPEnn-ltC8",
    "Chest Fly": "https://youtu.be/eozdVDA78K0",
    "Cable Crossovers": "https://youtu.be/taI4XduLpTk",
    "Push-ups": "https://youtu.be/_l3ySVKYVJ8",
    "Barbell Curl": "https://youtu.be/kwG2ipFRgfo",
    "Dumbbell Curl": "https://youtu.be/ykJmrZ5v0Oo",
    "Hammer Curl": "https://youtu.be/zC3nLlEvin4",
    "Skull Crushers": "https://youtu.be/d_KZxkY_0cM",
    "Triceps Pushdowns": "https://youtu.be/2-LAMcpzODU",
    "Overhead Press": "https://youtu.be/2yjwXTZQDDI",
    "Lateral Raise": "https://youtu.be/kDqklk1ZESo",
    "Deadlifts": "https://youtu.be/op9kVnSso6Q",
    "Pull-ups": "https://youtu.be/eGo4IYlbE5g",
    "Squats": "https://youtu.be/Dy28eq2PjcM",
    "Leg Press": "https://youtu.be/IZxyjW7MPJQ",
    "Lunges": "https://youtu.be/QOVaHwm-Q6U",
    "Plank": "https://youtu.be/pSHjTRCQxIw",
    "Crunches": "https://youtu.be/Xyd_fa5zoEU"
}

muscle_groups = {
    "Chest": ["Flat Bench Press", "Incline Dumbbell Press", "Chest Fly", "Cable Crossovers", "Push-ups"],
    "Biceps": ["Barbell Curl", "Dumbbell Curl", "Hammer Curl"],
    "Triceps": ["Skull Crushers", "Triceps Pushdowns"],
    "Shoulders": ["Overhead Press", "Lateral Raise"],
    "Back": ["Deadlifts", "Pull-ups"],
    "Legs": ["Squats", "Leg Press", "Lunges"],
    "Core": ["Plank", "Crunches"]
}

# ---------------- Tabs ----------------
if tabs == "Workout Plan":
    st.title("Workout Routines with Video Links")
    for muscle, exercises in muscle_groups.items():
        st.subheader(muscle)
        for i, ex in enumerate(exercises, 1):
            link = video_links.get(ex, "")
            st.markdown(f"**{i}.** [{ex}]({link})")

elif tabs == "Diet Plan":
    st.title("Custom Diet Plan")
    if diet_type == "Veg":
        st.write("- Oats + Fruits\n- Paneer\n- Tofu + Quinoa\n- Peanut butter toast\n- Lentils & Veggies")
    else:
        st.write("- Eggs + Toast\n- Chicken breast\n- Fish + Brown Rice\n- Greek Yogurt\n- Protein Shakes")

elif tabs == "Progress Tracker":
    st.title("Track Your Progress")
    weight = st.number_input("Enter current weight (kg):", min_value=30.0, max_value=200.0)
    calories = st.number_input("Calories consumed today:", min_value=0)
    st.success("Data saved! Track it daily to stay consistent.")

elif tabs == "Motivation":
    st.title("Motivation Zone")
    st.subheader("Quote of the Day:")
    st.success("FOR MOTIVATION: WATCH NISHANK'S SHIRTLESS PHOTOS.")

# ------------- End -------------
