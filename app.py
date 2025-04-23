# NKFITNESS AI Trainer - Massive Muscle Group Expansion + First-Time Motivation Quote
import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NKFITNESS AI Trainer", layout="wide", page_icon=":muscle:")
st.title("🏋️ NKFITNESS AI Trainer")

# Sidebar
tabs = st.sidebar.radio("Go to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])
st.sidebar.markdown("---")
name = st.sidebar.text_input("Enter your name:", "Abhigna")
goal = st.sidebar.selectbox("Select your fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
level = st.sidebar.radio("Choose your fitness level:", ["Beginner", "Intermediate", "Advanced"])

# Muscle Workouts (Expanded)
muscle_workouts = {
    "Chest": [
        ("Flat Bench Press", "https://www.youtube.com/watch?v=rT7DgCr-3pg"),
        ("Incline Dumbbell Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8"),
        ("Decline Barbell Press", "https://www.youtube.com/watch?v=KxQnD1wAqDY"),
        ("Cable Flys", "https://www.youtube.com/watch?v=taI4XduLpTk"),
        ("Push-ups", "https://www.youtube.com/watch?v=_l3ySVKYVJ8"),
        ("Incline Push-ups", "https://www.youtube.com/watch?v=F7jSp2xmmEE"),
        ("Chest Dips", "https://www.youtube.com/watch?v=2z8JmcrW-As")
    ],
    "Back": [
        ("Deadlifts", "https://www.youtube.com/watch?v=op9kVnSso6Q"),
        ("Pull-Ups", "https://www.youtube.com/watch?v=eGo4IYlbE5g"),
        ("Barbell Rows", "https://www.youtube.com/watch?v=FWJR5Ve8bnQ"),
        ("Lat Pulldowns", "https://www.youtube.com/watch?v=CAwf7n6Luuc")
    ],
    "Biceps": [
        ("Barbell Curl", "https://www.youtube.com/watch?v=kwG2ipFRgfo"),
        ("Hammer Curl", "https://www.youtube.com/watch?v=zC3nLlEvin4"),
        ("Incline Dumbbell Curl", "https://www.youtube.com/watch?v=soxrZlIl35U")
    ],
    "Triceps": [
        ("Skull Crushers", "https://www.youtube.com/watch?v=d_KZxkY_0cM"),
        ("Tricep Dips", "https://www.youtube.com/watch?v=0326dy_-CzM"),
        ("Pushdowns", "https://www.youtube.com/watch?v=2-LAMcpzODU")
    ],
    "Shoulders": [
        ("Overhead Press", "https://www.youtube.com/watch?v=2yjwXTZQDDI"),
        ("Lateral Raises", "https://www.youtube.com/watch?v=kDqklk1ZESo"),
        ("Arnold Press", "https://www.youtube.com/watch?v=vj2w851ZHRM")
    ],
    "Legs": [
        ("Barbell Squats", "https://www.youtube.com/watch?v=Dy28eq2PjcM"),
        ("Lunges", "https://www.youtube.com/watch?v=QOVaHwm-Q6U"),
        ("Leg Press", "https://www.youtube.com/watch?v=IZxyjW7MPJQ")
    ],
    "Core": [
        ("Plank Holds", "https://www.youtube.com/watch?v=pSHjTRCQxIw"),
        ("Russian Twists", "https://www.youtube.com/watch?v=wkD8rjkodUI"),
        ("Leg Raises", "https://www.youtube.com/watch?v=l4kQd9eWclE")
    ]
}

# Workout Plan
if tabs == "Workout Plan":
    st.header(f"{name}'s Custom {goal} Workout Plan - {level} Level")
    st.subheader("Suggested Exercises by Muscle Group")
    for muscle, exercises in muscle_workouts.items():
        st.markdown(f"### {muscle}")
        for title, link in random.sample(exercises, min(3, len(exercises))):
            st.write(f"{title}: [Watch Video]({link})")

    if st.button("Save My Workout Plan"):
        with open("saved_workouts.txt", "a") as f:
            f.write(f"{datetime.now()} - {name} - {goal} - {level}\n")
        st.success("Workout plan saved successfully!")

# Diet Plan
elif tabs == "Diet Plan":
    st.header(f"{name}'s {goal} Diet Plan")
    st.write("Coming soon...")

# Progress Tracker
elif tabs == "Progress Tracker":
    st.header("Progress Tracker")
    height = st.number_input("Height (cm):", min_value=100, max_value=250, value=175)
    weight = st.number_input("Weight (kg):", min_value=30, max_value=200, value=70)
    if height and weight:
        bmi = round(weight / ((height / 100) ** 2), 1)
        st.success(f"Your BMI is: {bmi}")

    st.subheader("Calories Burned This Week")
    df = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, 8)],
        "Calories": [random.randint(200, 500) for _ in range(7)]
    })
    st.line_chart(df.set_index("Day"))

# Motivation Tab
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

# Footer
st.markdown("---")
st.markdown("Built with :muscle: by NKFITNESS-AI")
