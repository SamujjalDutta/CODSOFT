import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    movies = pd.read_csv("tmdb_5000_movies.csv")
except FileNotFoundError:
    print("Dataset not found. Make sure 'tmdb_5000_movies.csv' is in the same folder.")
    exit()

movies = movies[['title', 'overview']].dropna()
movies = movies[movies['overview'].str.len() > 30].reset_index(drop=True)

vectorizer = TfidfVectorizer(stop_words='english')
overview_vectors = vectorizer.fit_transform(movies['overview'])


def recommend_by_mood(mood_input, top_n=5):
    mood_vec = vectorizer.transform([mood_input])
    similarity_scores = cosine_similarity(mood_vec, overview_vectors).flatten()
    similar_indices = similarity_scores.argsort()[-top_n:][::-1]

    print("\nThe recommended movies are:\n")
    for idx in similar_indices:
        title = movies.iloc[idx]['title']
        print("-", title)


if __name__ == "__main__":
    print("Mood-Based Movie Recommendation System")
    print("Describe your mood (e.g., 'I want something emotional', 'I'm feeling adventurous')")
    user_input = input("Enter your current mood or interest: ").strip()
    if len(user_input) < 5:
        print("Please describe your mood with more detail.")
    else:
        recommend_by_mood(user_input)
