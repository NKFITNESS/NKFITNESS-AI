import streamlit as st import pyrebase import pandas as pd import random from datetime import datetime

Firebase configuration

firebaseConfig = { "apiKey": "AIzaSyBnjOPY0yWreRdW9dD9l9G8F49wnO6WmfE", "authDomain": "nkfitness-ai.firebaseapp.com", "projectId": "nkfitness-ai", "storageBucket": "nkfitness-ai.appspot.com", "messagingSenderId": "", "appId": "", "measurementId": "", "databaseURL": "" }

firebase = pyrebase.initialize_app(firebaseConfig) auth = firebase.auth()

st.title("NKFITNESS AI - Email Login")

menu = ["Login", "Register"] choice = st.radio("Choose:", menu) email = st.text_input("Email") password = st.text_input("Password", type='password')

if choice == "Register": if st.button("Register"): try: user = auth.create_user_with_email_and_password(email, password) st.success("Registered successfully. You can now log in.") except: st.error("Registration failed. Try a different email.") else: if st.button("Login"): try: user = auth.sign_in_with_email_and_password(email, password) st.success("Login successful!")

# Workout plan generator
        st.header("Welcome to NKFITNESS AI!")
        name = st.text_input("Enter your name")
        goal = st.selectbox("Select your fitness goal", ["Lose Weight", "Gain Muscle", "Stay Fit"])
        level = st.radio("Choose your fitness level", ["Beginner", "Intermediate", "Advanced"])

        if st.button("Generate Plan"):
            st.success(f"Hi {name}! Here's your custom plan to {goal.lower()} at {level.lower()} level:")

            workouts = {
                "Chest": [
                    ("Push-ups", "https://www.youtube.com/watch?v=_l3ySVKYVJ8"),
                    ("Bench Press", "https://www.youtube.com/watch?v=gRVjAtPip0Y"),
                    ("Incline Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8"),
                    ("Chest Fly", "https://www.youtube.com/watch?v=eozdVDA78K0"),
                    ("Decline Press", "https://www.youtube.com/watch?v=YxWjcX2ou6k"),
                    ("Cable Crossover", "https://www.youtube.com/watch?v=taI4XduLpTk"),
                    ("Dumbbell Press", "https://www.youtube.com/watch?v=VmB1G1K7v94"),
                    ("Chest Dips", "https://www.youtube.com/watch?v=2z8JmcrW-As"),
                    ("Machine Press", "https://www.youtube.com/watch?v=s0fOT6Xj2FQ"),
                    ("Squeeze Press", "https://www.youtube.com/watch?v=Ro_g8cHj5hM")
                ],
                "Biceps": [
                    ("Barbell Curl", "https://www.youtube.com/watch?v=kwG2ipFRgfo"),
                    ("Dumbbell Curl", "https://www.youtube.com/watch?v=sAq_ocpRh_I"),
                    ("Hammer Curl", "https://www.youtube.com/watch?v=zC3nLlEvin4"),
                    ("Concentration Curl", "https://www.youtube.com/watch?v=soxrZlIl35U"),
                    ("EZ Bar Curl", "https://www.youtube.com/watch?v=soxrZlIl35U"),
                    ("Cable Curl", "https://www.youtube.com/watch?v=KT9gW4EJFPs"),
                    ("Preacher Curl", "https://www.youtube.com/watch?v=Zrlxk6z0gzo"),
                    ("Incline Curl", "https://www.youtube.com/watch?v=ZQBej9XjVdc"),
                    ("Zottman Curl", "https://www.youtube.com/watch?v=6u-4YbMGqNc"),
                    ("Spider Curl", "https://www.youtube.com/watch?v=mK9e1SOwujY")
                ],
                "Triceps": [
                    ("Close Grip Bench Press", "https://www.youtube.com/watch?v=iGxF1O6uEjA"),
                    ("Triceps Pushdown", "https://www.youtube.com/watch?v=2-LAMcpzODU"),
                    ("Overhead Triceps Extension", "https://www.youtube.com/watch?v=YbX7Wd8jQ-Q"),
                    ("Skull Crushers", "https://www.youtube.com/watch?v=d_KZxkY_0cM"),
                    ("Dips", "https://www.youtube.com/watch?v=2z8JmcrW-As"),
                    ("Kickbacks", "https://www.youtube.com/watch?v=6SS6K3lAwZ8"),
                    ("Triceps Rope Extension", "https://www.youtube.com/watch?v=vB5OHsJ3EME"),
                    ("Diamond Push-ups", "https://www.youtube.com/watch?v=J0DnG1_S92I"),
                    ("Reverse Grip Pushdown", "https://www.youtube.com/watch?v=ODXUgqcxbVU"),
                    ("Close Grip Push-up", "https://www.youtube.com/watch?v=GJnvwQ1U8IY")
                ],
                "Shoulders": [
                    ("Shoulder Press", "https://www.youtube.com/watch?v=B-aVuyhvLHU"),
                    ("Lateral Raise", "https://www.youtube.com/watch?v=kDqklk1ZESo"),
                    ("Front Raise", "https://www.youtube.com/watch?v=-t7fuZ0KhDA"),
                    ("Rear Delt Fly", "https://www.youtube.com/watch?v=pDTHSxxD2Sg"),
                    ("Arnold Press", "https://www.youtube.com/watch?v=vj2w851ZHRM"),
                    ("Upright Row", "https://www.youtube.com/watch?v=6TSP1TRMUzs"),
                    ("Cable Lateral Raise", "https://www.youtube.com/watch?v=3VcKaXpzqRo"),
                    ("Face Pull", "https://www.youtube.com/watch?v=rep-qVOkqgk"),
                    ("Barbell Overhead Press", "https://www.youtube.com/watch?v=2yjwXTZQDDI"),
                    ("Dumbbell Shrugs", "https://www.youtube.com/watch?v=NUmGRzITZZ0")
                ],
                "Legs": [
                    ("Squats", "https://www.youtube.com/watch?v=aclHkVaku9U"),
                    ("Leg Press", "https://www.youtube.com/watch?v=IZxyjW7MPJQ"),
                    ("Lunges", "https://www.youtube.com/watch?v=QOVaHwm-Q6U"),
                    ("Hamstring Curl", "https://www.youtube.com/watch?v=1Tq3QdYUuHs"),
                    ("Leg Extensions", "https://www.youtube.com/watch?v=yR5qBK1vCZQ"),
                    ("Romanian Deadlift", "https://www.youtube.com/watch?v=2SHsk9AzdjA"),
                    ("Calf Raise", "https://www.youtube.com/watch?v=YMmgqO8Jo-k"),
                    ("Step Ups", "https://www.youtube.com/watch?v=7vxaWvydKCM"),
                    ("Jump Squats", "https://www.youtube.com/watch?v=U4s4mEQ5VqU"),
                    ("Sumo Squats", "https://www.youtube.com/watch?v=9ZuXKqRbT9k")
                ],
                "Core": [
                    ("Planks", "https://www.youtube.com/watch?v=pSHjTRCQxIw"),
                    ("Russian Twists", "https://www.youtube.com/watch?v=wkD8rjkodUI"),
                    ("Bicycle Crunches", "https://www.youtube.com/watch?v=9FGilxCbdz8"),
                    ("Leg Raises", "https://www.youtube.com/watch?v=l4kQd9eWclE"),
                    ("Mountain Climbers", "https://www.youtube.com/watch?v=nmwgirgXLYM"),
                    ("V-Ups", "https://www.youtube.com/watch?v=iP2fjvG0g3w"),
                    ("Sit-Ups", "https://www.youtube.com/watch?v=1fbU_MkV7NE"),
                    ("Flutter Kicks", "https://www.youtube.com/watch?v=K1Vbr-Yi5wQ"),
                    ("Crunches", "https://www.youtube.com/watch?v=Xyd_fa5zoEU"),
                    ("Toe Touches", "https://www.youtube.com/watch?v=JB2oyawG9KI")
                ]
            }

            for muscle, exercises in workouts.items():
                st.subheader(muscle)
                for ex, link in random.sample(exercises, 3):
                    st.markdown(f"- [{ex}]({link})")

            st.markdown("**Motivation**: _Go watch Nishank's shirtless photos!_")

    except:
        st.error("Invalid credentials or login failed. Please try again.")

