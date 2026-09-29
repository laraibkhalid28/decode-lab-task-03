# AI Job Recommendation System

This project is an AI-based job recommendation system developed for DecodeLabs Artificial Intelligence Project 3.

## Project Goal

The system recommends jobs based on the user's skills and interests.

## How It Works

1. User enters their skills.
2. Job skills are processed using TF-IDF.
3. Cosine similarity is used to compare user skills with job skills.
4. Jobs with the highest similarity scores are recommended.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit

## Dataset

The project uses a jobs dataset containing job titles and key skills.

## How to Run

Activate the virtual environment and run:

```bash
streamlit run app.py