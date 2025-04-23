import streamlit as st import requests import json import pandas as pd import random from datetime import datetime

FIREBASE_API_KEY = "AIzaSyBnjOPY0yWreRdW9dD9l9G8F49wnO6WmfE"

st.set_page_config(page_title="NKFITNESS AI - Full App", layout="wide")

if "email_token" not in st.session_state: st.session_state.email_token = None st.session_state.email_user = ""

def register_user(email, password): res = requests.post( f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}", headers={"Content-Type": "application/json"}, data=json.dumps({"email": email, "password": password, "returnSecureToken": True}) ) return res

def login_user(email, password): res = requests.post( f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}", headers={"Content-Type": "application/json"}, data=json.dumps({"email": email, "password": password, "returnSecureToken": True}) ) return res

if not st.session_state.email_token: st.title("NKFITNESS AI - Email Login") mode = st.radio("Choose:", ["Login", "Register"]) email = st.text_input("Email") password = st.text_input("Password", type="password")

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

st.sidebar.title("Welcome!") st.sidebar.markdown(f"Logged in as: {st.session_state.email_user}") tabs = st.sidebar.radio("Navigate to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

goal = st.sidebar.selectbox("Select your fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"]) level = st.sidebar.radio("Choose your level:", ["Beginner", "Intermediate", "Advanced"]) diet_type = st.sidebar.radio("Diet Type:", ["Veg", "Non-Veg"])

Workout Plan with video links

workout_videos = { "Flat Bench Press": "https://www.youtube.com/watch?v=gRVjAtPip0Y", "Incline Dumbbell Press": "https://www.youtube.com/watch?v=8iPEnn-ltC8", "Chest Fly": "https://www.youtube.com/watch?v=eozdVDA78K0", "Cable Crossovers": "https://www.youtube.com/watch?v=taI4XduLpTk", "Push-ups": "https://www.youtube.com/watch?v=_l3ySVKYVJ8", "Barbell Curl": "https://www.youtube.com/watch?v=kwG2ipFRgfo", "Dumbbell Curl": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo", "Hammer Curl": "https://www.youtube.com/watch?v=zC3nLlEvin4", "Skull Crushers": "https://www.youtube.com/watch?v=d_KZxkY_0cM", "Triceps Pushdowns": "https://www.youtube.com/watch?v=2-LAMcpzODU", "Overhead Press": "https://www.youtube.com/watch?v=2yjwXTZQDDI", "Lateral Raise": "https://www.youtube.com/watch?v=kDqklk1ZESo", "Deadlifts": "https://www.youtube.com/watch?v=op9kVnSso6Q", "Pull-ups": "https://www.youtube.com/watch?v=eGo4IYlbE5g", "Squats": "https://www.youtube.com/watch?v=Dy28eq2PjcM", "Leg Press": "https://www.youtube.com/watch?v=IZxyjW7MPJQ", "Lunges": "https://www.youtube.com/watch?v=QOVaHwm-Q6U", "Plank": "https://www.youtube.com/watch?v=pSHjTRCQxIw", "Crunches": "https://www.youtube.com/watch?v=Xyd_fa5zoEU" }

muscle_groups = { "Chest": ["Flat Bench Press", "Incline Dumbbell Press", "Chest Fly", "Cable Crossovers", "Push-ups"], "Biceps": ["Barbell Curl", "Dumbbell Curl", "Hammer Curl"], "Triceps": ["Skull Crushers", "Triceps Pushdowns"], "Shoulders": ["Overhead Press", "Lateral Raise"], "Back": ["Deadlifts", "Pull-ups"], "Legs": ["Squats", "Leg Press", "Lunges"], "Core": ["Plank", "Crunches"] }

if tabs == "Workout Plan": st.title("Workout Plan by Muscle Group") for group, exercises in muscle_groups.items(): st.subheader(group) for i, ex in enumerate(exercises, 1): link = workout_videos.get(ex, "") if link: st.markdown(f"{i}. {ex}") else: st.markdown(f"{i}. {ex}")

Diets

...

Progress Tracker

...

Motivation

...

               
