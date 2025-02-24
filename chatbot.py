import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic-Dataset.csv")

def get_response(question: str):
    question = question.lower()
    if "percentage of passengers were male" in question:
        male_count = df[df["Sex"] == "male"].shape[0]
        total_count = df.shape[0]
        percentage = (male_count / total_count) * 100
        return f"{percentage:.2f}% of the passengers were male."

    elif "average ticket fare" in question:
        avg_fare = df["Fare"].mean()
        return f"The average ticket fare was ${avg_fare:.2f}."

    elif "passengers embarked from each port" in question:
        embark_counts = df["Embarked"].value_counts().to_dict()
        return f"Passenger embarkation counts: {embark_counts}"

    return "No answer found"  # Default response

    # if "percentage of passengers were male" in question:
    #     male_percent = (df['Sex'] == 'male').mean() * 100
    #     return f"{male_percent:.2f}% of passengers were male."
    # elif "histogram of passenger ages" in question:
    #     plt.figure(figsize=(8, 5))
    #     sns.histplot(df['Age'].dropna(), bins=20, kde=True)
    #     plt.xlabel("Age")
    #     plt.ylabel("Count")
    #     plt.title("Histogram of Passenger Ages")
    #     plt.savefig("frontend/age_histogram.png")
    #     return "Generated histogram saved."
    # elif "average ticket fare" in question:
    #     return f"The average ticket fare was ${df['Fare'].mean():.2f}."
    # elif "passengers embarked from each port" in question:
    #     embark_counts = df["Embarked"].value_counts().to_dict()
    #     return f"Passengers embarked: {embark_counts}"
    # else:
    #     return "Sorry, I don't understand that question."
