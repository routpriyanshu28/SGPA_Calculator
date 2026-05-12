
import streamlit as st

st.title("SGPA Calculator")

grade_points = {
    "O": 10,
    "E": 9,
    "A": 8,
    "B": 7,
    "C": 6,
    "D": 5,
    "F": 0,
    "FR": 0
}

num_subjects = st.number_input(
    "Enter Number of Subjects",
    min_value=1,
    max_value=20,
    step=1
)

total_credit_points = 0
total_credits = 0

for i in range(num_subjects):

    st.subheader(f"Subject {i+1}")

    credits = st.number_input(
        f"Enter Credits for Subject {i+1}",
        min_value=0.0,
        step=1.0,
        key=f"credits_{i}"
    )

    grade = st.selectbox(
        f"Select Grade for Subject {i+1}",
        ["O", "E", "A", "B", "C", "D", "F", "FR"],
        key=f"grade_{i}"
    )

    grade_point = grade_points[grade]

    total_credit_points += credits * grade_point
    total_credits += credits

if total_credits > 0:

    sgpa = total_credit_points / total_credits

    st.success(f"Your SGPA is: {round(sgpa, 2)}")
