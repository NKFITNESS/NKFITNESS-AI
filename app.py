import streamlit as st import pyrebase import pandas as pd import random from datetime import datetime

st.set_page_config(page_title="NKFITNESS AI", layout="wide")

Firebase Config

firebaseConfig = { "apiKey": "AIzaSyBnjOPY0yWreRdW9dD9l9G8F49wnO6WmfE", "authDomain": "nkfitnessai.firebaseapp.com", "projectId": "nkfitnessai", "storageBucket": "nkfitnessai.appspot.com", "messagingSenderId": "YOUR_SENDER_ID", "appId": "YOUR_APP_ID" }

firebase = pyrebase.initialize_app(firebaseConfig) auth = firebase.auth()

Login/Register

login_state = st.sidebar.radio("Choose:", ["Login", "Register"]) email = st.sidebar.text_input("Email") password = st.sidebar.text_input("Password", type="password")

if login_state == "Register": if st.sidebar.button("Register"): try: auth.create_user_with_email_and_password(email, password) st.sidebar.success("Registered successfully. Please log in.") except Exception as e: st.sidebar.error(f"Registration error: {e}") elif login_state == "Login": if st.sidebar.button("Login"): try: user = auth.sign_in_with_email_and_password(email, password) st.sidebar.success("Logged in successfully.") st.session_state.logged_in = True except Exception as e: st.sidebar.error("Login failed. Check your credentials.")

if not st.session_state.get("logged_in"): st.stop()

Name input

name = st.text_input("Enter your name") fitness_level = st.selectbox("Choose your fitness level", ["Beginner", "Intermediate", "Advanced"]) goal = st.selectbox("Select your fitness goal", ["Lose Weight", "Gain Muscle", "Maintain Fitness"]) tab = st.sidebar.radio("Go to:", ["Workout Plan", "Diet Plan", "Progress Tracker", "Motivation"])

Workout Plan

video_links = { "Chest": { "Bench Press": "https://www.youtube.com/watch?v=gRVjAtPip0Y", "Incline Bench": "https://www.youtube.com/watch?v=SrqOu55lrYU", "Dumbbell Fly": "https://www.youtube.com/watch?v=eozdVDA78K0", "Push-ups": "https://www.youtube.com/watch?v=_l3ySVKYVJ8", "Cable Crossover": "https://www.youtube.com/watch?v=taI4XduLpTk", "Chest Dips": "https://www.youtube.com/watch?v=2z8JmcrW-As", "Decline Press": "https://www.youtube.com/watch?v=7f-K-XnHi28", "Machine Press": "https://www.youtube.com/watch?v=-aSJKBLhe_w", "Wide Push-ups": "https://www.youtube.com/watch?v=el0ua8sPo8w", "Svend Press": "https://www.youtube.com/watch?v=7kzYVgceK54" }, "Biceps": { "Barbell Curl": "https://www.youtube.com/watch?v=kwG2ipFRgfo", "Dumbbell Curl": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo", "Hammer Curl": "https://www.youtube.com/watch?v=zC3nLlEvin4", "Preacher Curl": "https://www.youtube.com/watch?v=ZurlMNnd_1M", "Concentration Curl": "https://www.youtube.com/watch?v=UwrlvvCUB_g", "Cable Curl": "https://www.youtube.com/watch?v=av7-8igSXTs", "EZ Bar Curl": "https://www.youtube.com/watch?v=soxrZlIl35U", "Spider Curl": "https://www.youtube.com/watch?v=z0cwJK9gO1Q", "Reverse Curl": "https://www.youtube.com/watch?v=e0hMnsZL-C8", "Zottman Curl": "https://www.youtube.com/watch?v=OyQ5b-VjOZk" }, "Triceps": { "Skull Crushers": "https://www.youtube.com/watch?v=d_KZxkY_0cM", "Triceps Pushdowns": "https://www.youtube.com/watch?v=2-LAMcpzODU", "Overhead Extension": "https://www.youtube.com/watch?v=YbX7Wd8jQ-Q", "Rope Pushdowns": "https://www.youtube.com/watch?v=-xa-2Ic8p4A", "Dips": "https://www.youtube.com/watch?v=2z8JmcrW-As", "Close-Grip Bench Press": "https://www.youtube.com/watch?v=2vjH2f0K9dU", "Kickbacks": "https://www.youtube.com/watch?v=6SSfXxbsU6E", "Reverse Pushdowns": "https://www.youtube.com/watch?v=Gozdh2djQEY", "Diamond Pushups": "https://www.youtube.com/watch?v=J0DnG1_S92I", "Machine Triceps Press": "https://www.youtube.com/watch?v=8zXZDiFzNUI" }, "Shoulders": { "Overhead Press": "https://www.youtube.com/watch?v=qEwKCR5JCog", "Lateral Raise": "https://www.youtube.com/watch?v=kDqklk1ZESo", "Front Raise": "https://www.youtube.com/watch?v=-t7fuZ0KhDA", "Reverse Fly": "https://www.youtube.com/watch?v=0JfYxMRsUCQ", "Arnold Press": "https://www.youtube.com/watch?v=vj2w851ZHRM", "Cable Lateral Raise": "https://www.youtube.com/watch?v=0RKL5QePHk8", "Barbell Shrug": "https://www.youtube.com/watch?v=U4s4mEQ5VqU", "Face Pull": "https://www.youtube.com/watch?v=vj2w851ZHRM", "Upright Row": "https://www.youtube.com/watch?v=JAq-Rr5lWk4", "Machine Press": "https://www.youtube.com/watch?v=yGq8V8_MIEk" }, "Legs": { "Squats": "https://www.youtube.com/watch?v=aclHkVaku9U", "Leg Press": "https://www.youtube.com/watch?v=IZxyjW7MPJQ", "Lunges": "https://www.youtube.com/watch?v=QOVaHwm-Q6U", "Goblet Squat": "https://www.youtube.com/watch?v=6xwGFn-J_Qg", "Leg Extensions": "https://www.youtube.com/watch?v=YyvSfVjQeL0", "Hamstring Curls": "https://www.youtube.com/watch?v=JbGSeE3nPec", "Romanian Deadlift": "https://www.youtube.com/watch?v=0hS5f5TXNVo", "Step Ups": "https://www.youtube.com/watch?v=dQqApCGd5Ss", "Hip Thrusts": "https://www.youtube.com/watch?v=LM8XHLYJoYs", "Calf Raises": "https://www.youtube.com/watch?v=-M4-G8p8fmc" }, "Core": { "Plank": "https://www.youtube.com/watch?v=pSHjTRCQxIw", "Crunches": "https://www.youtube.com/watch?v=Xyd_fa5zoEU", "Leg Raises": "https://www.youtube.com/watch?v=JB2oyawG9KI", "Russian Twists": "https://www.youtube.com/watch?v=wkD8rjkodUI", "Bicycle Crunch": "https://www.youtube.com/watch?v=9FGilxCbdz8", "Mountain Climbers": "https://www.youtube.com/watch?v=nmwgirgXLYM", "V-Ups": "https://www.youtube.com/watch?v=iP2fjvG0g3w", "Cable Crunch": "https://www.youtube.com/watch?v=z1U7WQW7JKY", "Toe Touches": "https://www.youtube.com/watch?v=eq6tVGPSSUQ", "Hanging Leg Raises": "https://www.youtube.com/watch?v=1dbbTUM9JY8" } }

if tab == "Workout Plan": st.title("Custom AI Workout Plan") st.success(f"Welcome {name}! Here's your workout plan to {goal.lower()} at {fitness_level.lower()} level.") for muscle, exercises in video_links.items(): st.subheader(f"{muscle} Workouts") for ex, link in exercises.items(): st.markdown(f"- {ex}")

Remaining tabs: Diet Plan, Progress Tracker, Motivation (unchanged)

...

