# Task 4 - Mood-Based Movie Recommendation System

## Overview

This is a Python-based content-based recommendation system developed as part of the CodSoft AI Internship.  
It suggests movies to users based on their mood descriptions or interests by analyzing and comparing text from movie overviews.

The system uses TF-IDF vectorization and cosine similarity to find and recommend movies with the most relevant plot summaries.

## Project Context

This project was built for Task 3 of the CodSoft AI Internship Program, with the aim of understanding how recommendation engines work using content features.

Instead of choosing a movie title, the user simply describes their mood, and the system returns the top 5 matching movies.

Examples:
- "I want something romantic and emotional"
- "Looking for a dark thriller"
- "I feel adventurous and want a space movie"

## What It Demonstrates

- Use of TF-IDF vectorization to handle text data
- Implementation of cosine similarity to rank recommendations
- Preprocessing and combining movie overviews and genres
- How content-based filtering works in recommendation systems
- Clean user interaction through the terminal

## Features

- Suggests movies based on free-text mood input
- Uses content-based filtering
- Real-time search across ~5000 movies (from TMDB dataset)
- TF-IDF supports n-grams for better phrase matching
- Results are unique for each type of mood

## File Structure

Task 3 - Mood Based Movie Recommender/

├── mood_movie_recommender.py

├── tmdb_5000_movies.csv

└── README.md

## Technologies Used

- Python 3
- pandas
- scikit-learn

## How to Run

1. Open your terminal or code editor.
2. Make sure Python 3 is installed.
3. Install the required libraries:
   - pip install pandas scikit-learn
4. Download the TMDB movie dataset and place tmdb_5000_movies.csv in the same folder as the script.

   - Dataset link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

5. Run the program:

      - python mood_movie_recommender.py
6. Enter your mood (e.g., "I want a romantic story")

## Dataset Used

  - TMDB 5000 Movie Dataset (from Kaggle)
  - Columns used: title, overview, genres
  - Combined and processed to match user mood with plot themes

# Author

Samujjal Dutta
Developed as part of the CodSoft AI Internship Program

   
