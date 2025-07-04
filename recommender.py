# ml/recommender.py

from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
import pandas as pd

# Load data
ratings = pd.read_csv('data/ratings.csv')
movies = pd.read_csv('data/movies.csv')

# Create Reader and Dataset
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Train-test split
trainset, testset = train_test_split(data, test_size=0.2)

# Train model
model = SVD()
model.fit(trainset)

# Get top N recommendations for a user
def get_recommendations(user_id, n=10):
    movie_ids = movies['movieId'].tolist()
    user_rated = ratings[ratings['userId'] == user_id]['movieId'].tolist()
    
    # Filter out already rated movies
    candidates = [mid for mid in movie_ids if mid not in user_rated]

    # Predict ratings
    predictions = [(mid, model.predict(user_id, mid).est) for mid in candidates]
    predictions.sort(key=lambda x: x[1], reverse=True)

    # Return top N recommended movies
    top_n = predictions[:n]
    return [(movies[movies['movieId'] == mid]['title'].values[0], round(score, 2)) for mid, score in top_n]

# Example usage
if __name__ == "__main__":
    user_id = 1
    recommendations = get_recommendations(user_id)
    for title, score in recommendations:
        print(f"{title} - Predicted Rating: {score}")