import streamlit as st
import requests
import json
import pandas as pd
import random
from datetime import datetime

FIREBASE_API_KEY = "AIzaSyBnjOPY0yWreRdW9dD9l9G8F49wnO6WmfE"

st.set_page_config(page_title="NKFITNESS AI", layout="wide")

if "email_token" not in st.session_state:
    st.session_state.email_token = None
    st.session_state.email_user = ""

def register_user(email, password):
    res = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"email": email, "password": password, "returnSecureToken": True})
    )
    return res

def login_user(email, password):
    res = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"email": email, "password": password, "returnSecureToken": True})
    )
    return res

if not st.session_state.email_token:
    st.title("NKFITNESS AI - Email Login")
    mode = st.radio("Choose:", ["Login", "Register"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button(mode):
        if mode == "Register":
            response = register_user(email, password)
            if response.status_code == 200:
                st.success("User registered successfully! Please log in.")
            else:
                st.error(response.json()["error"]["message"])
        else:
            response = login_user(email, password)
            if response.status_code == 200:
                st.session_state.email_token = response.json()["idToken"]
                st.session_state.email_user = email
                st.rerun()
            else:
                st.error(response.json()["error"]["message"])
    st.stop()

# Sidebar
st.sidebar.title("Welcome, Champion!")
st.sidebar.markdown(f"**Logged in as:** `{st.session_state.email_user}`")
user_name = st.sidebar.text_input("Enter your name", value="Champion")
tabs = st.sidebar.radio("Navigate to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])
goal = st.sidebar.selectbox("Fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
level = st.sidebar.radio("Fitness level:", ["Beginner", "Intermediate", "Advanced"])
diet_type = st.sidebar.radio("Diet Type:", ["Veg", "Non-Veg"])

# Workout dictionary with YouTube links
def linkify(exercise, url):
    return f"[{exercise}]({url})"

muscle_groups = {
    "Chest": [
        ("Flat Bench Press", "https://www.youtube.com/watch?v=gRVjAtPip0Y"),
        ("Incline Dumbbell Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8"),
        ("Push-ups", "https://www.youtube.com/watch?v=_l3ySVKYVJ8"),
        ("Chest Fly", "https://www.youtube.com/watch?v=eozdVDA78K0"),
        ("Cable Crossover", "https://www.youtube.com/watch?v=taI4XduLpTk"),
        ("Decline Bench Press", "https://www.youtube.com/watch?v=YQ2jme4XRMA"),
        ("Dips", "https://www.youtube.com/watch?v=2z8JmcrW-As"),
        ("Incline Barbell Press", "https://www.youtube.com/watch?v=SrqOu55lrYU"),
        ("Smith Machine Press", "https://www.youtube.com/watch?v=dqndWyN0G1Q"),
        ("Pec Deck", "https://www.youtube.com/watch?v=TyKLXzXBSPU")
    ],
    "Biceps": [
        ("Barbell Curl", "https://www.youtube.com/watch?v=kwG2ipFRgfo"),
        ("Dumbbell Curl", "https://www.youtube.com/watch?v=sAq_ocpRh_I"),
        ("Hammer Curl", "https://www.youtube.com/watch?v=zC3nLlEvin4"),
        ("Preacher Curl", "https://www.youtube.com/watch?v=2L2lnxIcNmo"),
        ("EZ Bar Curl", "https://www.youtube.com/watch?v=x9kZ3-M5SXA"),
        ("Concentration Curl", "https://www.youtube.com/watch?v=8XmM1pBt3PE"),
        ("Zottman Curl", "https://www.youtube.com/watch?v=wECZAfmKJ7w"),
        ("Cable Curl", "https://www.youtube.com/watch?v=DAcWq32qDzI"),
        ("Incline Dumbbell Curl", "https://www.youtube.com/watch?v=soxrZlIl35U"),
        ("Reverse Curl", "https://www.youtube.com/watch?v=Vw2m5kYjYuU")
    ],
    "Triceps": [
        ("Skull Crushers", "https://www.youtube.com/watch?v=d_KZxkY_0cM"),
        ("Triceps Pushdowns", "https://www.youtube.com/watch?v=2-LAMcpzODU"),
        ("Overhead Extensions", "https://www.youtube.com/watch?v=_gsUck-7M74"),
        ("Close-Grip Bench", "https://www.youtube.com/watch?v=6JtP6ju0IMw"),
        ("Dips", "https://www.youtube.com/watch?v=0326dy_-CzM"),
        ("Kickbacks", "https://www.youtube.com/watch?v=-xa5jWlZYkI"),
        ("Rope Pushdowns", "https://www.youtube.com/watch?v=6SSIxhh0_J4"),
        ("Diamond Push-ups", "https://www.youtube.com/watch?v=J0DnG1_S92I"),
        ("Machine Press", "https://www.youtube.com/watch?v=Y2DS3Vxskcw"),
        ("Reverse Pushdowns", "https://www.youtube.com/watch?v=COuZG_w1YHM")
    ],
    "Shoulders": [
        ("Overhead Press", "https://www.youtube.com/watch?v=qEwKCR5JCog"),
        ("Lateral Raise", "https://www.youtube.com/watch?v=kDqklk1ZESo"),
        ("Front Raise", "https://www.youtube.com/watch?v=-t7fuZ0KhDA"),
        ("Reverse Fly", "https://www.youtube.com/watch?v=WrTEF5yBCcU"),
        ("Arnold Press", "https://www.youtube.com/watch?v=vj2w851ZHRM"),
        ("Barbell Press", "https://www.youtube.com/watch?v=2yjwXTZQDDI"),
        ("Cable Raise", "https://www.youtube.com/watch?v=q91bljllyqY"),
        ("Shrugs", "https://www.youtube.com/watch?v=3UWi44yN-wU"),
        ("Face Pulls", "https://www.youtube.com/watch?v=rep-qVOkqgk"),
        ("Machine Press", "https://www.youtube.com/watch?v=gvN_Rp_VWjU")
    ],
    "Legs": [
        ("Squats", "https://www.youtube.com/watch?v=Dy28eq2PjcM"),
        ("Leg Press", "https://www.youtube.com/watch?v=IZxyjW7MPJQ"),
        ("Lunges", "https://www.youtube.com/watch?v=QOVaHwm-Q6U"),
        ("Leg Extensions", "https://www.youtube.com/watch?v=8b1YMLN5zAI"),
        ("Hamstring Curls", "https://www.youtube.com/watch?v=Joba0kJVgQs"),
        ("Romanian Deadlifts", "https://www.youtube.com/watch?v=2SHsk9AzdjA"),
        ("Walking Lunges", "https://www.youtube.com/watch?v=wrwwXE_x-pQ"),
        ("Goblet Squats", "https://www.youtube.com/watch?v=6xwGFn-J_Qo"),
        ("Hip Thrusts", "https://www.youtube.com/watch?v=LM8XHLYJoYs"),
        ("Calf Raises", "https://www.youtube.com/watch?v=-M4-G8p8fmc")
    ],
    "Core": [
        ("Plank", "https://www.youtube.com/watch?v=pSHjTRCQxIw"),
        ("Crunches", "https://www.youtube.com/watch?v=Xyd_fa5zoEU"),
        ("Leg Raises", "https://www.youtube.com/watch?v=l4kQd9eWclE"),
        ("Russian Twists", "https://www.youtube.com/watch?v=wkD8rjkodUI"),
        ("Mountain Climbers", "https://www.youtube.com/watch?v=nmwgirgXLYM"),
        ("V-Ups", "https://www.youtube.com/watch?v=Z8i5zDA8fH4"),
        ("Cable Crunch", "https://www.youtube.com/watch?v=zwfVYxDGVrg"),
        ("Bicycle Crunch", "https://www.youtube.com/watch?v=9FGilxCbdz8"),
        ("Toe Touches", "https://www.youtube.com/watch?v=kAqFIyHKu4w"),
        ("Hanging Leg Raises", "https://www.youtube.com/watch?v=bkD9LwDBWW0")
    ]
}

if tabs == "Workout Plan":
    st.title(f"Workout Plan for {user_name}")
    for group, exs in muscle_groups.items():
        st.subheader(group)
        for i, (ex, link) in enumerate(exs, 1):
            st.markdown(f"{i}. {linkify(ex, link)}")

# Diet Section
diet_levels = {
    "Beginner": {
        "Veg": ["Oats + Banana", "Paneer Sandwich", "Lentils + Rice", "Boiled Veggies", "Green Smoothie"],
        "Non-Veg": ["Boiled Eggs", "Grilled Chicken + Rice", "Fish + Salad", "Protein Shake", "Yogurt"]
    },
    "Intermediate": {
        "Veg": ["Quinoa Bowl", "Sprouts", "Tofu Stir Fry", "Veggie Omelet (eggless)", "Smoothie Bowl"],
        "Non-Veg": ["Egg Whites + Toast", "Turkey Wraps", "Tuna Salad", "Grilled Salmon", "Boiled Chicken"]
    },
    "Advanced": {
        "Veg": ["Protein Pancakes", "Bulgur + Chickpeas", "Soy Chunks + Salad", "Greek Yogurt", "Hummus + Veggies"],
        "Non-Veg": ["Steak + Rice", "Beef Stir Fry", "Salmon Wraps", "Grilled Chicken Bowl", "Omelet + Toast"]
    }
}

if tabs == "Diet Plan":
    st.title(f"{diet_type} Diet Plan for {goal} - {level}")
    for item in diet_levels[level][diet_type]:
        st.markdown(f"- {item}")

elif tabs == "Progress Tracker":
    st.title("Progress Tracker")
    weight = st.number_input("Your Weight (kg):", min_value=30, max_value=200, value=70)
    height = st.number_input("Your Height (cm):", min_value=100, max_value=250, value=170)
    bmi = round(weight / ((height / 100) ** 2), 1)
    st.success(f"Your BMI is: **{bmi}**")

    st.subheader("Weekly Calorie Burn")
    cal_df = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, 8)],
        "Calories Burned": [random.randint(200, 600) for _ in range(7)]
    })
    st.line_chart(cal_df.set_index("Day"))

    if st.button("Save Progress"):
        with open("progress_log.txt", "a") as f:
            f.write(f"{datetime.now()} | {st.session_state.email_user} | Weight: {weight}kg | Height: {height}cm | BMI: {bmi}\n")
        st.success("Progress saved successfully!")

elif tabs == "Motivation":
    st.title("Daily Motivation")
    st.markdown("**FOR MOTIVATION: GO WATCH NISHANK'S SHIRTLESS PHOTOS.**")
    quotes = [
        "No excuses, just results!",
        "Progress, not perfection.",
        "Discipline beats motivation.",
        "Push harder than yesterday!",
        "You're stronger than you think!"
    ]
    st.info(random.choice(quotes))

st.markdown("---")
st.markdown("Built by **NKFITNESS AI**")
