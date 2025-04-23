NKFITNESS AI - Full Version: Login, Levels, Diet, Progress Tracker

import streamlit as st import random import pandas as pd from datetime import datetime

--- App Config ---

st.set_page_config(page_title="NKFITNESS AI", layout="wide")

--- Mock Phone OTP Login ---

if "user" not in st.session_state: st.session_state.user = None

if not st.session_state.user: st.title("NKFITNESS AI - Phone OTP Login") phone = st.text_input("Enter test phone number", value="+911234567890") otp = st.text_input("Enter OTP", value="123456") if st.button("Login"): if phone == "+911234567890" and otp == "123456": st.session_state.user = phone st.success(f"Welcome, {phone}!") else: st.error("Invalid phone or OTP.") st.stop()

--- Sidebar Tabs & Personalization ---

st.sidebar.markdown(f"Logged in as: {st.session_state.user}") st.title("🏋️ NKFITNESS AI Trainer") tabs = st.sidebar.radio("Go to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

goal = st.sidebar.selectbox("Select your goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"]) level = st.sidebar.radio("Choose fitness level:", ["Beginner", "Intermediate", "Advanced"]) diet_type = st.sidebar.radio("Diet Type:", ["Veg", "Non-Veg"])

--- Workout Plan Generator ---

plans = { "Lose Weight": { "Beginner": ["Jumping jacks", "Squats", "Plank"], "Intermediate": ["Burpees", "Mountain climbers", "Lunges"], "Advanced": ["HIIT circuits", "Sprints", "Box jumps"] }, "Gain Muscle": { "Beginner": ["Push-ups", "Dumbbell rows", "Leg press"], "Intermediate": ["Bench press", "Pull-ups", "Barbell squat"], "Advanced": ["Deadlift", "Weighted dips", "Clean & press"] }, "Maintain Fitness": { "Beginner": ["Walking", "Bodyweight squats", "Shoulder taps"], "Intermediate": ["Jogging", "Push-ups", "Resistance bands"], "Advanced": ["CrossFit routines", "Jump rope", "Mobility drills"] } }

--- Diet Chart ---

diets = { "Lose Weight": { "Veg": ["Oats + Fruits", "Lentils + Salad", "Green Tea"], "Non-Veg": ["Boiled eggs", "Grilled chicken + Veggies", "Yogurt"] }, "Gain Muscle": { "Veg": ["Paneer + Rice", "Protein shake", "Tofu wraps"], "Non-Veg": ["Egg whites", "Chicken breast + Rice", "Fish curry"] }, "Maintain Fitness": { "Veg": ["Upma + Nuts", "Chapati + Daal", "Fruit smoothie"], "Non-Veg": ["Egg sandwich", "Grilled fish + Veggies", "Milk"] } }

--- Workout Plan UI ---

if tabs == "Workout Plan": st.header(f"Workout Plan for {level} - Goal: {goal}") for exercise in plans[goal][level]: st.markdown(f"- {exercise}")

--- Diet Plan UI ---

elif tabs == "Diet Plan": st.header(f"{diet_type} Diet Plan for {goal}") for item in diets[goal][diet_type]: st.markdown(f"- {item}")

--- Progress Tracker ---

elif tabs == "Progress Tracker": st.header("Track Your Fitness Progress") weight = st.number_input("Enter your current weight (kg):", min_value=30, max_value=200, value=70) height = st.number_input("Enter your height (cm):", min_value=100, max_value=250, value=170) bmi = round(weight / ((height / 100) ** 2), 1) st.success(f"Your BMI is: {bmi}")

st.subheader("Weekly Calorie Burn Tracker")
cal_df = pd.DataFrame({
    "Day": [f"Day {i}" for i in range(1, 8)],
    "Calories Burned": [random.randint(200, 600) for _ in range(7)]
})
st.line_chart(cal_df.set_index("Day"))

if st.button("Save Progress"):
    with open("progress_log.txt", "a") as f:
        f.write(f"{datetime.now()} | {st.session_state.user} | Weight: {weight}kg | Height: {height}cm | BMI: {bmi}\n")
    st.success("Progress saved successfully!")

--- Motivation Tab ---

elif tabs == "Motivation": st.header("Daily Motivation") if "first_motivation" not in st.session_state: st.session_state.first_motivation = True

if st.session_state.first_motivation:
    st.warning("FOR MOTIVATION: WATCH NISHANK GYM PHOTOS.")
    st.session_state.first_motivation = False
else:
    st.info(random.choice([
        "No excuses, just results!",
        "Progress, not perfection.",
        "The only bad workout is the one you didn’t do.",
        "Push harder than yesterday."
    ]))

--- Footer ---

st.markdown("---") st.markdown("Built by NKFITNESS-AI with 💪")

