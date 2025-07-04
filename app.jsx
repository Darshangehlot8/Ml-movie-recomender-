// src/App.jsx

import React, { useState } from 'react';
import axios from 'axios';
import MovieCard from './components/MovieCard';

function App() {
  const [userId, setUserId] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const fetchRecommendations = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/recommend/${userId}`);
      setRecommendations(response.data.recommendations);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <h1 className="text-3xl font-bold mb-6 text-center">🎬 Movie Recommender</h1>
      <div className="flex justify-center mb-6">
        <input
          type="number"
          placeholder="Enter User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          className="px-4 py-2 rounded-l-md text-black"
        />
        <button
          onClick={fetchRecommendations}
          className="bg-blue-600 px-4 py-2 rounded-r-md hover:bg-blue-700"
        >
          Get Recommendations
        </button>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {recommendations.map((movie, index) => (
          <MovieCard key={index} title={movie.title} rating={movie.predicted_rating} />
        ))}
      </div>
    </div>
  );
}

export default App;