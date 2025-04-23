# NKFITNESS AI Trainer (Final fixed version)
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

# Muscle Group Workouts (with safe link display)
muscle_workouts = {
    "Chest": [("Flat Bench Press", "https://www.youtube.com/watch?v=rT7DgCr-3pg"),
              ("Incline Dumbbell Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8")],
    "Back": [("Deadlifts", "https://www.youtube.com/watch?v=op9kVnSso6Q"),
             ("Pull-Ups", "https://www.youtube.com/watch?v=eGo4IYlbE5g")],
    "Biceps": [("Barbell Curls", "https://www.youtube.com/watch?v=kwG2ipFRgfo"),
               ("Hammer Curls", "https://www.youtube.com/watch?v=zC3nLlEvin4")],
    "Triceps": [("Dips", "https://www.youtube.com/watch?v=0326dy_-CzM"),
                ("Overhead Extensions", "https://www.youtube.com/watch?v=YbX7Wd8jQ-Q")],
    "Shoulders": [("Overhead Press", "https://www.youtube.com/watch?v=2yjwXTZQDDI"),
                  ("Lateral Raises", "https://www.youtube.com/watch?v=kDqklk1ZESo")],
    "Legs": [("Squats", "https://www.youtube.com/watch?v=Dy28eq2PjcM"),
             ("Lunges", "https://www.youtube.com/watch?v=QOVaHwm-Q6U")],
    "Core": [("Plank", "https://www.youtube.com/watch?v=pSHjTRCQxIw"),
             ("Leg Raises", "https://www.youtube.com/watch?v=l4kQd9eWclE")]
}

# Workout Plan Tab
if tabs == "Workout Plan":
    st.header(f"{name}'s Custom {goal} Workout Plan - {level} Level")

    plans = {
        "Lose Weight": {
            "Beginner": ["Day 1: 10 squats, 10 push-ups", "Day 2: Jumping jacks + rest", "Day 3: Stretch"],
            "Intermediate": ["Day 1: Core + HIIT", "Day 2: Cardio Circuits", "Day 3: Recovery walk"],
            "Advanced": ["Day 1: 3x circuit burn", "Day 2: HIIT + Sprints", "Day 3: Abs & Mobility"]
        },
        "Gain Muscle": {
            "Beginner": ["Day 1: Full-body 3x10", "Day 2: Push day", "Day 3: Rest"],
            "Intermediate": ["Day 1: Chest/Back", "Day 2: Legs", "Day 3: Arms/Core"],
            "Advanced": ["Day 1: Push", "Day 2: Pull", "Day 3: Legs", "Day 4: Core"]
        },
        "Maintain Fitness": {
            "Beginner": ["Day 1: Walk 30 mins", "Day 2: Bodyweight training", "Day 3: Yoga"],
            "Intermediate": ["Day 1: Jog + Core", "Day 2: Circuits", "Day 3: Swim or Rest"],
            "Advanced": ["Day 1: CrossFit style", "Day 2: Cardio mix", "Day 3: Full mobility"]
        }
    }

    st.success(f"Hi {name}! Here's your plan to {goal.lower()} at {level.lower()} level:")
    for day in plans[goal][level]:
        st.write(day)

    st.subheader("Suggested Exercises by Muscle Group")
    for muscle, workouts in muscle_workouts.items():
        st.markdown(f"**{muscle}**")
        for title, url in random.sample(workouts, min(2, len(workouts))):
            st.write(f"{title}: [Watch Video]({url})")

    if st.button("Save My Workout Plan"):
        with open("saved_workouts.txt", "a") as f:
            f.write(f"{datetime.now()} - {name} - {goal} - {level}\n")
        st.success("Workout plan saved successfully!")

# Diet Plan Tab
elif tabs == "Diet Plan":
    st.header(f"{name}'s {goal} Diet Plan")
    st.write("Coming soon...")

# Progress Tracker
elif tabs == "Progress Tracker":
    st.header("Progress Tracker")
    height = st.number_input("Enter height (cm):", min_value=100, max_value=250)
    weight = st.number_input("Enter weight (kg):", min_value=30, max_value=200)
    if height and weight:
        bmi = round(weight / ((height / 100) ** 2), 1)
        st.success(f"Your BMI is: {bmi}")

    data = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, 8)],
        "Calories Burned": [random.randint(200, 600) for _ in range(7)]
    })
    st.line_chart(data.set_index("Day"))

# Motivation Tab
elif tabs == "Motivation":
    st.header("Your Daily Dose of Motivation")
    st.info(random.choice([
        "Push yourself, because no one else is going to do it for you.",
        "No pain, no gain.",
        "Discipline is the bridge between goals and results.",
        "Don't quit. Suffer now and live the rest of your life as a champion."
    ]))

# Footer
st.markdown("---")
st.markdown("Made with :muscle: by NKFITNESS-AI")
