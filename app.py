# app.py — NKFITNESS AI Trainer (Tabbed Layout)
import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="NKFITNESS AI Trainer", layout="wide", page_icon=":muscle:")
st.title("🏋️ NKFITNESS AI Trainer")

# --- Sidebar Tabs ---
tabs = st.sidebar.radio("Go to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

# --- Shared Inputs ---
st.sidebar.markdown("---")
name = st.sidebar.text_input("Enter your name:", "Abhigna")
goal = st.sidebar.selectbox("Select your fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
level = st.sidebar.radio("Choose your fitness level:", ["Beginner", "Intermediate", "Advanced"])

# --- Workout Plan Tab ---
if tabs == "Workout Plan":
    st.header(f"{name}'s Custom {goal} Workout Plan - {level} Level")

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

# --- Diet Plan Tab ---
elif tabs == "Diet Plan":
    st.header(f"{name}'s {goal} Diet Plan")
    diet_options = {
        "Lose Weight": [
            "Meal 1: Black Coffee + Boiled Eggs",
            "Meal 2: Grilled Chicken Salad",
            "Meal 3: Greek Yogurt + Almonds",
            "Meal 4: Steamed Veggies + Paneer",
            "Snack: Green Tea"
        ],
        "Gain Muscle": [
            "Meal 1: Oats + Whey + Peanut Butter",
            "Meal 2: Chicken + Rice + Broccoli",
            "Meal 3: Banana + Yogurt",
            "Meal 4: Whole Eggs + Sweet Potato",
            "Snack: Protein Shake"
        ],
        "Maintain Fitness": [
            "Meal 1: Scrambled Eggs + Toast",
            "Meal 2: Quinoa Bowl + Lentils",
            "Meal 3: Cottage Cheese + Fruit",
            "Meal 4: Hummus + Crackers",
            "Snack: Mixed Nuts"
        ]
    }
    for meal in diet_options[goal]:
        st.write(meal)

# --- Progress Tracker Tab ---
elif tabs == "Progress Tracker":
    st.header(f"{name}'s Weekly Progress Tracker")
    height = st.number_input("Enter height (cm):", min_value=100, max_value=250, value=175)
    weight = st.number_input("Enter weight (kg):", min_value=30, max_value=200, value=70)
    if height and weight:
        bmi = round(weight / ((height / 100) ** 2), 1)
        st.success(f"Your BMI is: {bmi}")

    st.subheader("Calories Burn Chart")
    progress_data = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, 8)],
        "Calories Burned": [random.randint(250, 600) for _ in range(7)]
    })
    st.line_chart(progress_data.set_index("Day"))

# --- Motivation Tab ---
elif tabs == "Motivation":
    st.header("Today's Motivation")
    quotes = [
        "Push yourself, because no one else is going to do it for you.",
        "Sweat is just fat crying.",
        "No excuses. Just results.",
        "You don’t find willpower, you create it.",
        "The body achieves what the mind believes."
    ]
    st.info(random.choice(quotes))

    st.markdown("### Want more?")
    st.markdown("- Coming soon: Progress uploads, voice coaching, and more!")

# Footer
st.markdown("---")
st.markdown("###### Made with :muscle: by NKFITNESS-AI")
