import streamlit as st

st.set_page_config(page_title="NKFITNESS AI")

st.title("NKFITNESS AI")
st.subheader("Welcome to your AI-powered fitness trainer!")

name = st.text_input("Enter your name")
goal = st.selectbox("Select your fitness goal", ["Lose Weight", "Build Muscle", "Stay Active"])
level = st.radio("Choose your fitness level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Plan"):
    st.success(f"Hi {name}! Here's your custom fitness plan to {goal.lower()} at {level.lower()} level.")
    st.write("**Day 1:** 15 push-ups, 20 squats, 10 burpees")
    st.write("**Day 2:** 20 jumping jacks, 25 sit-ups, 15 lunges")
    st.write("**Day 3:** Rest & hydration")
