app.py — NKFITNESS AI Trainer (With Muscle Groups + Save Button + Video Links)

import streamlit as st import random import pandas as pd from datetime import datetime

st.set_page_config(page_title="NKFITNESS AI Trainer", layout="wide", page_icon=":muscle:") st.title("🏋️ NKFITNESS AI Trainer")

--- Sidebar Tabs ---

tabs = st.sidebar.radio("Go to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

--- Shared Inputs ---

st.sidebar.markdown("---") name = st.sidebar.text_input("Enter your name:", "Abhigna") goal = st.sidebar.selectbox("Select your fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"]) level = st.sidebar.radio("Choose your fitness level:", ["Beginner", "Intermediate", "Advanced"])

--- Muscle Group Workouts with Video Links ---

muscle_workouts = { "Chest": [ ("Flat Bench Press", "https://www.youtube.com/watch?v=rT7DgCr-3pg"), ("Incline Dumbbell Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8"), ("Chest Flyes", "https://www.youtube.com/watch?v=eozdVDA78K0"), ("Push-Ups", "https://www.youtube.com/watch?v=l3ySVKYVJ8"), ("Cable Crossovers", "https://www.youtube.com/watch?v=taI4XduLpTk") ], "Back": [ ("Deadlifts", "https://www.youtube.com/watch?v=op9kVnSso6Q"), ("Pull-Ups", "https://www.youtube.com/watch?v=eGo4IYlbE5g"), ("Barbell Rows", "https://www.youtube.com/watch?v=FWJR5Ve8bnQ"), ("Lat Pulldowns", "https://www.youtube.com/watch?v=CAwf7n6Luuc"), ("Seated Rows", "https://www.youtube.com/watch?v=HJSVR_67OlM") ], "Biceps": [ ("Barbell Curls", "https://www.youtube.com/watch?v=kwG2ipFRgfo"), ("Hammer Curls", "https://www.youtube.com/watch?v=zC3nLlEvin4"), ("Concentration Curls", "https://www.youtube.com/watch?v=soxrZlIl35U"), ("EZ Bar Curls", "https://www.youtube.com/watch?v=uG2AjB5iJ3o"), ("Cable Curls", "https://www.youtube.com/watch?v=ykJmrZ5v0Oo") ], "Triceps": [ ("Tricep Dips", "https://www.youtube.com/watch?v=0326dy-CzM"), ("Skull Crushers", "https://www.youtube.com/watch?v=d_KZxkY_0cM"), ("Pushdowns", "https://www.youtube.com/watch?v=2-LAMcpzODU"), ("Overhead Extensions", "https://www.youtube.com/watch?v=YbX7Wd8jQ-Q"), ("Close Grip Bench Press", "https://www.youtube.com/watch?v=GODEdUr9ZL4") ], "Shoulders": [ ("Overhead Press", "https://www.youtube.com/watch?v=2yjwXTZQDDI"), ("Lateral Raises", "https://www.youtube.com/watch?v=kDqklk1ZESo"), ("Front Raises", "https://www.youtube.com/watch?v=-t7fuZ0KhDA"), ("Arnold Press", "https://www.youtube.com/watch?v=vj2w851ZHRM"), ("Face Pulls", "https://www.youtube.com/watch?v=rep-qVOkqgk") ], "Legs": [ ("Barbell Squats", "https://www.youtube.com/watch?v=Dy28eq2PjcM"), ("Lunges", "https://www.youtube.com/watch?v=QOVaHwm-Q6U"), ("Leg Press", "https://www.youtube.com/watch?v=IZxyjW7MPJQ"), ("RDLs", "https://www.youtube.com/watch?v=2SHsk9AzdjA"), ("Calf Raises", "https://www.youtube.com/watch?v=-M4-G8p8fmc") ], "Core": [ ("Plank Holds", "https://www.youtube.com/watch?v=pSHjTRCQxIw"), ("Russian Twists", "https://www.youtube.com/watch?v=wkD8rjkodUI"), ("Leg Raises", "https://www.youtube.com/watch?v=l4kQd9eWclE"), ("Bicycle Crunches", "https://www.youtube.com/watch?v=9FGilxCbdz8"), ("Mountain Climbers", "https://www.youtube.com/watch?v=nmwgirgXLYM") ] }

--- Workout Plan Tab ---

if tabs == "Workout Plan": st.header(f"{name}'s Custom {goal} Workout Plan - {level} Level")

plans = {
    "Lose Weight": {
        "Beginner": ["Day 1: 10 squats, 10 push-ups", "Day 2: 20 jumping jacks, 10 burpees", "Day 3: Rest"],
        "Intermediate": ["Day 1: 15 squats, 15 push-ups", "Day 2: 25 jumping jacks, 15 burpees", "Day 3: Core & HIIT"],
        "Advanced": ["Day 1: 20 squats, 20 push-ups, 10 burpees", "Day 2: 30 jumping jacks, 25 sit-ups", "Day 3: Sprints + Core"]
    },
    "Gain Muscle": {
        "Beginner": ["Day 1: Full-body (3x10)", "Day 2: Upper body", "Day 3: Rest"],
        "Intermediate": ["Day 1: Chest/Back", "Day 2: Legs", "Day 3: Arms/Core"],
        "Advanced": ["Day 1: Push", "Day 2: Pull", "Day 3: Legs", "Day 4: Core"]
    },
    "Maintain Fitness": {
        "Beginner": ["Day 1: Walk 30 mins", "Day 2: Bodyweight routine", "Day 3: Rest"],
        "Intermediate": ["Day 1: Jog + Stretch", "Day 2: Resistance Bands", "Day 3: Core Circuit"],
        "Advanced": ["Day 1: CrossFit style", "Day 2: Cardio & Core", "Day 3: Active Yoga"]
    }
}

st.success(f"Hi {name}! Here's your plan to {goal.lower()} at {level.lower()} level:")
for day in plans[goal][level]:
    st.write(day)

st.subheader("Suggested Exercises by Muscle Group")
for muscle, workouts in muscle_workouts.items():
    sample = random.sample(workouts, 3)
    st.markdown(f"**{muscle}**")
    for name, link in sample:
        st.markdown(f"- [{name}]({link})")

if st.button("Save My Workout Plan"):
    with open("saved_workouts.txt", "a") as f:
        f.write(f"{datetime.now()} - {name} - {goal} - {level}\n")
    st.success("Workout plan saved successfully!")

--- Diet, Progress, Motivation Tabs follow unchanged...

(Omitted here to focus on new workout logic. Let me know if you want the full file again.)

