app.py — AI Fitness Trainer using Streamlit (Enhanced)

import streamlit as st import random import pandas as pd

st.set_page_config(page_title="NKFITNESS AI Trainer", layout="wide", page_icon=":muscle:") st.title("🏋️ NKFITNESS AI Trainer")

--- BMI & Calorie Tracker ---

st.header("Health Tracker") col1, col2, col3 = st.columns(3)

with col1: height = st.number_input("Enter height (cm):", min_value=100, max_value=250) with col2: weight = st.number_input("Enter weight (kg):", min_value=30, max_value=200) with col3: calories = st.slider("Target Daily Calories (kcal)", 1500, 3500, 2500)

if height and weight: bmi = round(weight / ((height / 100) ** 2), 1) st.success(f"Your BMI is: {bmi}")

st.markdown("---")

--- Workout Generator ---

st.header("Weekly Workout Plan") if st.button("Generate Workout Plan"): workouts = { "Monday": "Back & Biceps - Pull-ups, Barbell Rows, Dumbbell Curls", "Tuesday": "Chest & Triceps - Bench Press, Pushups, Tricep Dips", "Wednesday": "Leg Day - Squats, Lunges, Leg Press", "Thursday": "Shoulders & Core - Military Press, Planks, Crunches", "Friday": "HIIT - Jump Rope, Burpees, Mountain Climbers", "Saturday": "Mobility & Stretch - Yoga Flow, Foam Rolling", "Sunday": "Active Rest - Walk or Light Swim" } for day, plan in workouts.items(): st.write(f"{day}: {plan}")

st.markdown("---")

--- Diet Generator ---

st.header("Diet Recommendations") diets = { "Lean Bulk": [ "Meal 1: Oats + Whey + Peanut Butter", "Meal 2: Chicken + Rice + Broccoli", "Meal 3: Greek Yogurt + Banana", "Meal 4: Eggs + Toast + Avocado", "Snack: Protein Bar or Shake" ], "Fat Loss": [ "Meal 1: Black Coffee + Boiled Eggs", "Meal 2: Grilled Chicken Salad", "Meal 3: Cottage Cheese + Berries", "Meal 4: Green Smoothie + Nuts", "Snack: Boiled Chickpeas" ], "Maintenance": [ "Meal 1: Scrambled Eggs + Oats", "Meal 2: Turkey Sandwich + Apple", "Meal 3: Paneer + Brown Rice", "Meal 4: Protein Shake", "Snack: Trail Mix" ] } diet_type = st.selectbox("Choose your goal:", list(diets.keys())) for meal in diets[diet_type]: st.write(meal)

st.markdown("---")

--- Daily Progress Chart ---

st.header("Weekly Calorie Burn Tracker") progress_data = pd.DataFrame({ "Day": [f"Day {i}" for i in range(1, 8)], "Calories Burned": [random.randint(250, 600) for _ in range(7)] }) st.line_chart(progress_data.set_index("Day"))

st.markdown("---")

--- Motivational Quotes ---

st.header("Today's Motivation") quotes = [ "Push yourself, because no one else is going to do it for you.", "Sweat is just fat crying.", "No excuses. Just results.", "You don’t find willpower, you create it.", "The body achieves what the mind believes." ] st.info(random.choice(quotes))

Footer

st.markdown("###### Made with :muscle: by NKFITNESS-AI")

