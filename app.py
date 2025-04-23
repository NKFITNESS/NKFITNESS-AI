import streamlit as st

st.set_page_config(page_title="NKFITNESS AI", layout="centered", initial_sidebar_state="auto")

st.title("NKFITNESS AI")
st.subheader("Welcome to your AI-powered fitness trainer!")

name = st.text_input("Enter your name:")
goal = st.selectbox("What's your fitness goal?", ["Lose Weight", "Build Muscle", "Stay Fit"])
level = st.radio("Your fitness level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Plan"):
    st.success(f"Hey {name}, here's your {goal.lower()} workout plan for a {level.lower()}!")
    st.write("**Day 1 - Full Body Routine**")
    st.write("- 10 pushups\n- 15 squats\n- 20 jumping jacks\n- 30 sec plank")

st.markdown("---")
st.caption("Made with Streamlit for NKFITNESS")
