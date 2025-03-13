import streamlit as st 
import random 
import time

st.title("📝 Quiz Application")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"],
        "answer": "Shakespeare"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Hydrogen", "Gold", "Silver"],
        "answer": "Oxygen"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Select the correct answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct")
        st.balloons()
    else:
        st.error("❌ Incorrect Answer the answer is: " + question["answer"])
    time.sleep(3)
    st.session_state.current_question = random.choice(questions)
    st.rerun()
