import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Dummy user login setup
st.set_page_config(page_title="NKFITNESS AI", layout="centered")

# Simple login simulation
users = {"user@example.com": "password123"}

st.title("NKFITNESS AI - Email Login")

auth_mode = st.radio("Choose:", ["Login", "Register"])
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if auth_mode == "Register":
    if st.button("Register"):
        users[email] = password
        st.success("Registered successfully. You can now log in.")

elif auth_mode == "Login":
    if st.button("Login"):
        if users.get(email) == password:
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# If login is valid, show app
if users.get(email) == password:
    st.title("Welcome to NKFITNESS AI!")
    name = st.text_input("Enter your name", value="Champion")

    goal = st.selectbox("Select your fitness goal", ["Lose Weight", "Gain Muscle", "Stay Fit"])
    level = st.radio("Choose your fitness level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Generate Plan"):
        st.success(f"Hi {name}! Here's your custom fitness plan to {goal.lower()} at {level.lower()} level.")
        
        workouts = {
            "Chest": [("Bench Press", "https://youtu.be/gRVjAtPip0Y"),
                      ("Incline Dumbbell Press", "https://youtu.be/8iPEnn-ltC8"),
                      ("Chest Dips", "https://youtu.be/2z8JmcrW-As"),
                      ("Push-ups", "https://youtu.be/_l3ySVKYVJ8"),
                      ("Cable Fly", "https://youtu.be/eozdVDA78K0"),
                      ("Pec Deck Machine", "https://youtu.be/1GULjMS5Fqg"),
                      ("Decline Press", "https://youtu.be/8Q9p63rAdWc"),
                      ("Incline Fly", "https://youtu.be/6JtP6ju0IMw"),
                      ("Svend Press", "https://youtu.be/Wy87sZ6TbpM"),
                      ("Clap Push-ups", "https://youtu.be/tLz5WhF7Z0c")],

            "Biceps": [("Barbell Curl", "https://youtu.be/kwG2ipFRgfo"),
                       ("Hammer Curl", "https://youtu.be/zC3nLlEvin4"),
                       ("Preacher Curl", "https://youtu.be/xj6vmgZjeTE"),
                       ("Concentration Curl", "https://youtu.be/soxrZlIl35U"),
                       ("Incline Dumbbell Curl", "https://youtu.be/vPS88sHwdpM"),
                       ("Zottman Curl", "https://youtu.be/3nlq3aiUGC8"),
                       ("EZ Bar Curl", "https://youtu.be/XaLLwRf6qH4"),
                       ("Cable Curl", "https://youtu.be/YT5FkAq9AjU"),
                       ("Reverse Curl", "https://youtu.be/vB5OHsJ3EME"),
                       ("Chin-ups", "https://youtu.be/b-ztMQpj8yc")],

            "Triceps": [("Tricep Pushdown", "https://youtu.be/2-LAMcpzODU"),
                        ("Overhead Dumbbell Extension", "https://youtu.be/_gsUck-7M74"),
                        ("Skull Crushers", "https://youtu.be/d_KZxkY_0cM"),
                        ("Close-Grip Bench", "https://youtu.be/I4Fv4z2E0Zs"),
                        ("Dips", "https://youtu.be/2z8JmcrW-As"),
                        ("Kickbacks", "https://youtu.be/_gsUck-7M74"),
                        ("Rope Pushdowns", "https://youtu.be/Ej2RzqS-M78"),
                        ("Diamond Push-ups", "https://youtu.be/J0DnG1_S92I"),
                        ("Lying Triceps Extension", "https://youtu.be/6SS0UoT_6cE"),
                        ("Cable Overhead Extension", "https://youtu.be/VhKqoqDkTO0")],

            "Shoulders": [("Overhead Press", "https://youtu.be/2yjwXTZQDDI"),
                          ("Lateral Raise", "https://youtu.be/3VcKaXpzqRo"),
                          ("Front Raise", "https://youtu.be/-t7fuZ0KhDA"),
                          ("Shrugs", "https://youtu.be/NFzTWVKFI-g"),
                          ("Arnold Press", "https://youtu.be/vj2w851ZHRM"),
                          ("Rear Delt Fly", "https://youtu.be/Iwe6AmxVf7o"),
                          ("Upright Row", "https://youtu.be/VG2yEOKJp3Y"),
                          ("Cable Lateral Raise", "https://youtu.be/n6HIzGXN9gk"),
                          ("Plate Raise", "https://youtu.be/W-Jz4S8E7EY"),
                          ("Push Press", "https://youtu.be/B-aVuyhvLHU")],

            "Legs": [("Squats", "https://youtu.be/aclHkVaku9U"),
                     ("Lunges", "https://youtu.be/QOVaHwm-Q6U"),
                     ("Leg Press", "https://youtu.be/IZxyjW7MPJQ"),
                     ("Romanian Deadlift", "https://youtu.be/5WUXV2MNWsk"),
                     ("Leg Curl", "https://youtu.be/1Tq3QdYUuHs"),
                     ("Leg Extension", "https://youtu.be/YyvSfVjQeL0"),
                     ("Bulgarian Split Squat", "https://youtu.be/2C-uNgKwPLE"),
                     ("Step-ups", "https://youtu.be/YuR4c0Xj4sk"),
                     ("Jump Squats", "https://youtu.be/A-cFYWvaHr0"),
                     ("Wall Sit", "https://youtu.be/-cdph8hv0O0")],

            "Core": [("Plank", "https://youtu.be/pSHjTRCQxIw"),
                     ("Crunches", "https://youtu.be/Xyd_fa5zoEU"),
                     ("Russian Twist", "https://youtu.be/wkD8rjkodUI"),
                     ("Leg Raises", "https://youtu.be/JB2oyawG9KI"),
                     ("Mountain Climbers", "https://youtu.be/GE1mAJ1c0uQ"),
                     ("Bicycle Crunch", "https://youtu.be/Iwyvozckjak"),
                     ("Flutter Kicks", "https://youtu.be/Kk6eCdd0U8o"),
                     ("Side Plank", "https://youtu.be/K2VljzCC16g"),
                     ("Toe Touch", "https://youtu.be/abqTPksH3Vc"),
                     ("V-ups", "https://youtu.be/iP2fjvG0g3w")]
        }

        for group, moves in workouts.items():
            st.subheader(group)
            for w, link in moves:
                st.markdown(f"- [{w}]({link})")

        st.markdown("---")
        st.subheader("Diet Recommendation")
        if goal == "Lose Weight":
            st.write("High protein, low carbs. Drink water. Avoid sugar.")
        elif goal == "Gain Muscle":
            st.write("High protein, high carbs. Eat every 2-3 hours. Include whey and eggs.")
        else:
            st.write("Balanced macros. Stay hydrated. Eat fresh.")

        st.markdown("---")
        st.subheader("Progress Tracker")
        weight = st.number_input("Enter your current weight (kg)", min_value=30.0, max_value=200.0)
        calories = st.number_input("Enter your daily calorie intake", min_value=1000, max_value=5000)
        st.success(f"You're at {weight}kg with {calories} daily calories. Keep tracking!")

        st.markdown("---")
        st.subheader("Motivation")
        st.markdown("> **FOR MOTIVATION WATCH NISHANK'S SHIRTLESS PHOTOS**")
