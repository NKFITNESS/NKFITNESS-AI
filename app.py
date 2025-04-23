# NKFITNESS AI - Firebase Phone OTP Login + Workout App

import streamlit as st
import random
import pandas as pd

# --- Mock Firebase Phone OTP Login ---
st.set_page_config(page_title="NKFITNESS AI", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    st.title("NKFITNESS AI - Phone OTP Login")
    phone = st.text_input("Enter test phone number", value="+911234567890")
    otp = st.text_input("Enter OTP", value="123456")
    if st.button("Login"):
        if phone == "+911234567890" and otp == "123456":
            st.session_state.user = phone
            st.success(f"Welcome, {phone}!")
        else:
            st.error("Invalid phone or OTP.")
    st.stop()

# --- Sidebar + Tabs ---
st.sidebar.markdown(f"**Logged in as:** `{st.session_state.user}`")
tabs = st.sidebar.radio("Go to:", ["Workout Plan", "Motivation"])

st.title("🏋️ NKFITNESS AI Trainer")

# --- Workout Data ---
muscle_workouts = {
    "Chest": [
        ("Flat Bench Press", "https://www.youtube.com/watch?v=rT7DgCr-3pg"),
        ("Incline Dumbbell Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8"),
    ],
    "Back": [
        ("Deadlifts", "https://www.youtube.com/watch?v=op9kVnSso6Q"),
        ("Pull-Ups", "https://www.youtube.com/watch?v=eGo4IYlbE5g")
    ],
    "Biceps": [
        ("Barbell Curl", "https://www.youtube.com/watch?v=kwG2ipFRgfo")
    ],
    "Triceps": [
        ("Skull Crushers", "https://www.youtube.com/watch?v=d_KZxkY_0cM")
    ]
}

# --- Workout Plan UI ---
if tabs == "Workout Plan":
    st.header(f"Custom Workout Plan for {st.session_state.user}")
    for muscle, exercises in muscle_workouts.items():
        st.subheader(muscle)
        for title, link in exercises:
            st.markdown(f"- {title} — [Watch Video]({link})")

# --- Motivation UI ---
elif tabs == "Motivation":
    st.header("Stay Motivated")
    if "first_motivation" not in st.session_state:
        st.session_state.first_motivation = True

    if st.session_state.first_motivation:
        st.warning("FOR MOTIVATION: WATCH NISHANK GYM PHOTOS.")
        st.session_state.first_motivation = False
    else:
        st.info(random.choice([
            "No excuses, just results!",
            "Every rep counts!",
            "Progress, not perfection.",
            "Your body hears everything your mind says."
        ]))

st.markdown("---")
st.markdown("Built by NKFITNESS-AI")
