from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs(df, user_skills, top_n=5):

    # Convert user's skills into text
    user_skills = user_skills.lower().strip()

    # Combine user skills with job skills
    all_skills = df["Key Skills"].tolist() + [user_skills]

    # Convert text into numerical TF-IDF vectors
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(all_skills)

    # Last vector belongs to the user
    user_vector = tfidf_matrix[-1]

    # Job vectors
    job_vectors = tfidf_matrix[:-1]

    # Calculate similarity between user and every job
    similarity_scores = cosine_similarity(
        user_vector,
        job_vectors
    ).flatten()

    # Add similarity score to dataframe
    result = df.copy()
    result["Similarity Score"] = similarity_scores

    # Highest similarity first
    result = result.sort_values(
        by="Similarity Score",
        ascending=False
    )

    # Return top recommendations
    return result.head(top_n)