import streamlit as st import requests import json import pandas as pd import random from datetime import datetime

FIREBASE_API_KEY = "AIzaSyBnjOPY0yWreRdW9dD9l9G8F49wnO6WmfE"

st.set_page_config(page_title="NKFITNESS AI", layout="wide")

if "email_token" not in st.session_state: st.session_state.email_token = None st.session_state.email_user = ""

def register_user(email, password): return requests.post( f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}", headers={"Content-Type": "application/json"}, data=json.dumps({"email": email, "password": password, "returnSecureToken": True}) )

def login_user(email, password): return requests.post( f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}", headers={"Content-Type": "application/json"}, data=json.dumps({"email": email, "password": password, "returnSecureToken": True}) )

if not st.session_state.email_token: st.title("NKFITNESS AI - Email Login") mode = st.radio("Choose:", ["Login", "Register"]) email = st.text_input("Email") password = st.text_input("Password", type="password")

if st.button(mode):
    response = register_user(email, password) if mode == "Register" else login_user(email, password)
    if response.status_code == 200:
            st.session_state.email_token = response.json()["idToken"]
            st.session_state.email_user = email
            with open("login_log.txt", "a") as log:
                log.write(f"{datetime.now()} | {email} logged in

") st.session_state.email_user = email with open("login_log.txt", "a") as log: log.write(f"{datetime.now()} | {email} logged in\n") st.rerun() else: st.error(response.json()["error"]["message"]) st.stop()

st.sidebar.title("Welcome, Champion!") st.sidebar.markdown(f"Logged in as: {st.session_state.email_user}") user_name = st.sidebar.text_input("Enter your name", value="Champion") tabs = st.sidebar.radio("Navigate to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"]) if st.sidebar.checkbox("Show Who Logged In"): try: with open("login_log.txt", "r") as log: st.text(log.read()) except FileNotFoundError: st.warning("No log data yet.") goal = st.sidebar.selectbox("Fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"]) level = st.sidebar.radio("Fitness level:", ["Beginner", "Intermediate", "Advanced"]) diet_type = st.sidebar.radio("Diet Type:", ["Veg", "Non-Veg"]) if st.sidebar.checkbox("Show Who Logged In"): try: with open("login_log.txt", "r") as log: st.text(log.read()) except FileNotFoundError: st.warning("No log data yet.")

muscle_groups = { "Chest": [...], "Biceps": [...], "Triceps": [...], "Shoulders": [...], "Legs": [...], "Core": [...] }

if tabs == "Workout Plan": st.title(f"Workout Plan for {user_name}") for group, workouts in muscle_groups.items(): st.subheader(group) for i, (ex, link) in enumerate(workouts, 1): st.markdown(f"{i}. {ex}")

Diet plan logic remains here (unchanged)

Progress tracker and motivation blocks remain below

               
