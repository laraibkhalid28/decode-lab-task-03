import pandas as pd


def load_data():
    df = pd.read_csv("data/jobs.csv")

    # Remove unnecessary index column
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Remove rows where job title or skills are missing
    df = df.dropna(subset=["Job Title", "Key Skills"])

    # Convert skills to lowercase
    df["Key Skills"] = df["Key Skills"].str.lower().str.strip()

    # Clean job titles
    df["Job Title"] = df["Job Title"].str.strip()

    return df