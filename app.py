import streamlit as st

from src.preprocessing import load_data
from src.recommender import recommend_jobs


# Page configuration
st.set_page_config(
    page_title="AI Job Recommendation System",
    page_icon="💼",
    layout="wide"
)


# Title
st.title("💼 AI Job Recommendation System")

st.write(
    "Enter your skills or interests and the system will "
    "recommend jobs based on similarity."
)


# Load dataset
df = load_data()


# User input
user_skills = st.text_input(
    "Enter your skills",
    placeholder="Example: Python, Machine Learning, Data Analysis"
)


# Number of recommendations
number_of_jobs = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)


# Recommendation button
if st.button("Recommend Jobs"):

    if not user_skills.strip():

        st.warning("Please enter at least one skill.")

    else:

        recommendations = recommend_jobs(
            df,
            user_skills,
            number_of_jobs
        )

        st.subheader("Recommended Jobs")

        for _, job in recommendations.iterrows():

            st.write("### " + str(job["Job Title"]))

            st.write(
                "**Required Skills:** "
                + str(job["Key Skills"])
            )

            st.write(
                "**Similarity Score:** "
                + f"{job['Similarity Score']:.2f}"
            )

            st.divider()