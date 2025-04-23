app.py - NKFITNESS AI Trainer (Fixed syntax + safe video links rendering)

import streamlit as st import random import pandas as pd from datetime import datetime

st.set_page_config(page_title="NKFITNESS AI Trainer", layout="wide", page_icon=":muscle:") st.title("🏋️ NKFITNESS AI Trainer")

Sidebar Tabs

tabs = st.sidebar.radio("Go to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

Shared Inputs

st.sidebar.markdown("---") name = st.sidebar.text_input("Enter your name:", "Abhigna") goal = st.sidebar.selectbox("Select your fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"]) level = st.sidebar.radio("Choose your fitness level:", ["Beginner", "Intermediate", "Advanced"])

Muscle Group Workouts with Safe Rendering

muscle_workouts = { "Chest": [ ("Flat Bench Press", "https://www.youtube.com/watch?v=rT7DgCr-3pg"), ("Incline Dumbbell Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8"), ("Push-Ups", "https://www.youtube.com/watch?v=l3ySVKYVJ8") ], "Back": [ ("Deadlifts", "https://www.youtube.com/watch?v=op9kVnSso6Q"), ("Pull-Ups", "https://www.youtube.com/watch?v=eGo4IYlbE5g"), ("Barbell Rows", "https://www.youtube.com/watch?v=FWJR5Ve8bnQ") ], "Biceps": [ ("Barbell Curls", "https://www.youtube.com/watch?v=kwG2ipFRgfo"), ("Hammer Curls", "https://www.youtube.com/watch?v=zC3nLlEvin4"), ("Cable Curls", "https://www.youtube.com/watch?v=ykJmrZ5v0Oo") ], "Triceps": [ ("Tricep Dips", "https://www.youtube.com/watch?v=0326dy-CzM"), ("Pushdowns", "https://www.youtube.com/watch?v=2-LAMcpzODU"), ("Overhead Extensions", "https://www.youtube.com/watch?v=YbX7Wd8jQ-Q") ], "Shoulders": [ ("Overhead Press", "https://www.youtube.com/watch?v=2yjwXTZQDDI"), ("Lateral Raises", "https://www.youtube.com/watch?v=kDqklk1ZESo"), ("Arnold Press", "https://www.youtube.com/watch?v=vj2w851ZHRM") ], "Legs": [ ("Barbell Squats", "https://www.youtube.com/watch?v=Dy28eq2PjcM"), ("Lunges", "https://www.youtube.com/watch?v=QOVaHwm-Q6U"), ("Leg Press", "https://www.youtube.com/watch?v=IZxyjW7MPJQ") ], "Core": [ ("Plank Holds", "https://www.youtube.com/watch?v=pSHjTRCQxIw"), ("Russian Twists", "https://www.youtube.com/watch?v=wkD8rjkodUI"), ("Leg Raises", "https://www.youtube.com/watch?v=l4kQd9eWclE") ] }

Workout Plan Tab

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
    st.markdown(f"**{muscle}**")
    for name, link in random.sample(workouts, 2):
        st.write(f"{name}: [Watch]({link})")

if st.button("Save My Workout Plan"):
    with open("saved_workouts.txt", "a") as f:
        f.write(f"{datetime.now()} - {name} - {goal} - {level}\n")
    st.success("Workout plan saved successfully!")

Rest of tabs continue unchanged...

