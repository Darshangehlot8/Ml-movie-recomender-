# backend/app.py

from flask import Flask, jsonify
from ml.recommender import get_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Movie Recommender API!"

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    try:
        recommendations = get_recommendations(user_id)
        return jsonify({
            'user_id': user_id,
            'recommendations': [
                {'title': title, 'predicted_rating': score} 
                for title, score in recommendations
            ]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)