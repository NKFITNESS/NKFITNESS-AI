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
                st.success("Registered successfully! You can now log in.")
            else:
                st.error(response.json()["error"]["message"])
        else:
            response = login_user(email, password)
            if response.status_code == 200:
    st.session_state.email_token = response.json()["idToken"]
    st.session_state.email_user = email
    st.experimental_rerun()  # This will immediately refresh and load the main app
            else:
                st.error(response.json()["error"]["message"])
    st.stop()

st.sidebar.title("Welcome!")
st.sidebar.markdown(f"**Logged in as:** `{st.session_state.email_user}`")
tabs = st.sidebar.radio("Navigate to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

goal = st.sidebar.selectbox("Select your fitness goal:", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
level = st.sidebar.radio("Choose your level:", ["Beginner", "Intermediate", "Advanced"])
diet_type = st.sidebar.radio("Diet Type:", ["Veg", "Non-Veg"])

# Muscle Workouts with Video Links
muscle_groups = {
    "Chest": [
        ("Flat Bench Press", "https://youtu.be/gRVjAtPip0Y"),
        ("Incline Dumbbell Press", "https://youtu.be/8iPEnn-ltC8"),
        ("Chest Fly", "https://youtu.be/eozdVDA78K0"),
        ("Cable Crossovers", "https://youtu.be/taI4XduLpTk"),
        ("Push-ups", "https://youtu.be/IODxDxX7oi4"),
        ("Decline Bench Press", "https://youtu.be/DL2ze5e6vDE"),
        ("Dips", "https://youtu.be/2z8JmcrW-As"),
        ("Pec Deck", "https://youtu.be/V2dJkNDT0sA"),
        ("Smith Machine Press", "https://youtu.be/av7-8igSXTs"),
        ("Incline Barbell Press", "https://youtu.be/SfjgM6QMnys")
    ],
    "Biceps": [
        ("Barbell Curl", "https://youtu.be/kwG2ipFRgfo"),
        ("Dumbbell Curl", "https://youtu.be/sAq_ocpRh_I"),
        ("Hammer Curl", "https://youtu.be/zC3nLlEvin4"),
        ("Preacher Curl", "https://youtu.be/1Tq3QdYUuHs"),
        ("EZ Bar Curl", "https://youtu.be/N8sR1tVI1ok"),
        ("Concentration Curl", "https://youtu.be/0AUGkch3tzc"),
        ("Cable Curl", "https://youtu.be/qyVTrlnxY9A"),
        ("Zottman Curl", "https://youtu.be/OYYA5NggLZw"),
        ("Incline Curl", "https://youtu.be/soxrZlIl35U"),
        ("Reverse Curl", "https://youtu.be/3n9JYzqN4AM")
    ],
    "Triceps": [
        ("Skull Crushers", "https://youtu.be/d_KZxkY_0cM"),
        ("Pushdowns", "https://youtu.be/2-LAMcpzODU"),
        ("Overhead Extensions", "https://youtu.be/YbX7Wd8jQ-Q"),
        ("Close-Grip Bench", "https://youtu.be/wxQfWae5wfg"),
        ("Dips", "https://youtu.be/2z8JmcrW-As"),
        ("Kickbacks", "https://youtu.be/YbX7Wd8jQ-Q"),
        ("Rope Pushdowns", "https://youtu.be/2-LAMcpzODU"),
        ("Diamond Push-ups", "https://youtu.be/J0DnG1_S92I"),
        ("Machine Press", "https://youtu.be/BcYtJWlL75s"),
        ("Reverse Pushdowns", "https://youtu.be/LNBvdcDqZJQ")
    ],
    "Shoulders": [
        ("Overhead Press", "https://youtu.be/2yjwXTZQDDI"),
        ("Lateral Raise", "https://youtu.be/3VcKaXpzqRo"),
        ("Front Raise", "https://youtu.be/-t7fuZ0KhDA"),
        ("Reverse Fly", "https://youtu.be/-1nGoEtjCN4"),
        ("Arnold Press", "https://youtu.be/vj2w851ZHRM"),
        ("Barbell Press", "https://youtu.be/B-aVuyhvLHU"),
        ("Cable Raise", "https://youtu.be/nr0Aq_rEn7k"),
        ("Shrugs", "https://youtu.be/m7n5Yb3ySMI"),
        ("Face Pulls", "https://youtu.be/rep-qVOkqgk"),
        ("Machine Press", "https://youtu.be/1QY-fcMy3C4")
    ],
    "Legs": [
        ("Squats", "https://youtu.be/aclHkVaku9U"),
        ("Leg Press", "https://youtu.be/IZxyjW7MPJQ"),
        ("Lunges", "https://youtu.be/QOVaHwm-Q6U"),
        ("Leg Extensions", "https://youtu.be/YyvSfVjQeL0"),
        ("Hamstring Curls", "https://youtu.be/1Tq3QdYUuHs"),
        ("Romanian Deadlifts", "https://youtu.be/2SHsk9AzdjA"),
        ("Walking Lunges", "https://youtu.be/QOVaHwm-Q6U"),
        ("Goblet Squats", "https://youtu.be/6xwGFn-J_Qo"),
        ("Hip Thrusts", "https://youtu.be/SEdqd1n0cvg"),
        ("Calf Raises", "https://youtu.be/-M4-G8p8fmc")
    ],
    "Core": [
        ("Plank", "https://youtu.be/pSHjTRCQxIw"),
        ("Crunches", "https://youtu.be/Xyd_fa5zoEU"),
        ("Leg Raises", "https://youtu.be/JB2oyawG9KI"),
        ("Russian Twists", "https://youtu.be/wkD8rjkodUI"),
        ("Mountain Climbers", "https://youtu.be/cnyTQDSE884"),
        ("V-Ups", "https://youtu.be/iP2fjvG0g3w"),
        ("Cable Crunch", "https://youtu.be/2pjEwYdZ4qU"),
        ("Bicycle Crunches", "https://youtu.be/Iwyvozckjak"),
        ("Toe Touches", "https://youtu.be/YSx4W3SAhKk"),
        ("Hanging Leg Raises", "https://youtu.be/rBJZ3zDS5nQ")
    ]
}

if tabs == "Workout Plan":
    st.title("Workout Plan")
    st.markdown(f"**Goal:** {goal} | **Level:** {level}")
    for group, workouts in muscle_groups.items():
        st.subheader(group)
        for i, (name, link) in enumerate(workouts, 1):
            st.markdown(f"{i}. [{name}]({link})")

diet_plans = {
    "Lose Weight": {
        "Veg": {
            "Beginner": ["Oats + Banana", "Vegetable Soup", "Fruit bowl"],
            "Intermediate": ["Brown rice + Daal", "Steamed broccoli", "Green Tea"],
            "Advanced": ["Quinoa + Chickpeas", "Protein shake", "Tofu + Spinach wrap"]
        },
        "Non-Veg": {
            "Beginner": ["Boiled eggs", "Grilled chicken salad", "Apple"],
            "Intermediate": ["Fish curry + Brown rice", "Yogurt", "Egg whites"],
            "Advanced": ["Chicken breast + Salad", "Omelette + Toast", "Protein shake"]
        }
    },
    "Gain Muscle": {
        "Veg": {
            "Beginner": ["Paneer + Roti", "Nuts + Milk", "Sweet potato"],
            "Intermediate": ["Protein oats", "Tofu + Rice", "Cottage cheese"],
            "Advanced": ["Quinoa + Paneer", "Protein bar", "Soybeans + Brown rice"]
        },
        "Non-Veg": {
            "Beginner": ["Egg sandwich", "Fish + Potato", "Banana shake"],
            "Intermediate": ["Chicken breast + Pasta", "Boiled eggs", "Tuna salad"],
            "Advanced": ["Omelette + Peanut butter toast", "Grilled chicken", "Protein smoothie"]
        }
    },
    "Maintain Fitness": {
        "Veg": {
            "Beginner": ["Fruit bowl", "Upma", "Vegetable sandwich"],
            "Intermediate": ["Poha + Nuts", "Chapati + Daal", "Green salad"],
            "Advanced": ["Tofu salad", "Protein bar", "Mixed vegetable curry"]
        },
        "Non-Veg": {
            "Beginner": ["Eggs + Toast", "Grilled chicken", "Banana"],
            "Intermediate": ["Tuna sandwich", "Milk + Cereal", "Fish curry"],
            "Advanced": ["Chicken + Sweet potato", "Egg salad", "Protein bar"]
        }
    }
}

if tabs == "Diet Plan":
    st.title(f"{diet_type} Diet Plan - {goal} ({level})")
    for item in diet_plans[goal][diet_type][level]:
        st.markdown(f"- {item}")

elif tabs == "Progress Tracker":
    st.title("Progress Tracker")
    weight = st.number_input("Weight (kg):", min_value=30, max_value=200, value=70)
    height = st.number_input("Height (cm):", min_value=100, max_value=250, value=170)
    bmi = round(weight / ((height / 100) ** 2), 1)
    st.success(f"Your BMI is: {bmi}")

    st.subheader("Weekly Calorie Burn")
    cal_df = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, 8)],
        "Calories Burned": [random.randint(200, 600) for _ in range(7)]
    })
    st.line_chart(cal_df.set_index("Day"))

    if st.button("Save Progress"):
        with open("progress_log.txt", "a") as f:
            f.write(f"{datetime.now()} | {st.session_state.email_user} | Weight: {weight} | Height: {height} | BMI: {bmi}\n")
        st.success("Progress saved!")

elif tabs == "Motivation":
    st.title("Motivation")
    st.markdown("**FOR MOTIVATION: GO WATCH NISHANK'S SHIRTLESS PHOTOS.**")
    quotes = [
        "Push yourself because no one else is going to do it for you.",
        "Pain is weakness leaving the body.",
        "Your body can stand almost anything. It’s your mind that you have to convince.",
        "Train insane or remain the same.",
        "Excuses don’t burn calories."
    ]
    st.info(random.choice(quotes))

st.markdown("---")
st.markdown("Made with 💪 by **NKFITNESS AI**")
