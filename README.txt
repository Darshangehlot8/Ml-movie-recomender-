MoviMind

An AI-powered Movie Recommender System using **React.js**, **Flask**, and **TMDb API**.  
Provides personalized movie recommendations and trending titles with real posters, ratings, and release info.

 Features

Recommend movies based on user ID  
Fetch trending movies using TMDb API   
Real-time movie posters, ratings, and release dates  
React.js frontend with filtering options  
Flask backend with API routing  
Easy to customize with your own model or dataset


Project Structure
MoviMind_React_Backend/
├── movimind-backend/           # Flask backend
│   ├── app.py
│   ├── data/                   # Dataset folder
│   │   ├── movies.csv
│   │   └── ratings.csv
│   └── models/                 # (optional ML models)
│       └── recommender.pkl
├── movimind-frontend/          # React frontend
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.jsx
│       └── index.js
├── README.md                   # This file
└── requirements.txt            # Python dependencies

 Getting Started

 Clone the Repository
git clone https://github.com/your-username/movimind.git
cd movimind-React_Backend




Set Up Backend (Python + Flask)

Create and activate a virtual environment
cd movimind-backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows


Install dependencies
pip install -r requirements.txt

Start the Flask server
python app.py

Set Up Frontend (React)

cd movimind-frontend
npm install
npm run dev


> The React app runs at `http://localhost:5173` and connects to Flask at `http://localhost:5000`.


Download Dataset

Download the **MovieLens 100k dataset** from [here](https://grouplens.org/datasets/movielens/latest/).

Then:
- Extract and copy `movies.csv` and `ratings.csv`
- Paste them into:  
  `movimind-backend/data/`



Get a Free TMDb API Key

1. Sign up at: https://www.themoviedb.org/signup  
2. Visit: https://developer.themoviedb.org/  
3. Click **"Create" → "API Key"**
4. In `App.jsx`, replace:
```js
const TMDB_API_KEY = 'YOUR_TMDB_API_KEY';
```


Customize

- Add genres, user login, favorites, filters, or even chat-based recommendations!
- Replace dummy data with a trained ML model and save it in `models/recommender.pkl`


Contact

Email: (gehlotdarshan712@gmail.com)  
Made with ❤️ by [Darshan Gehlot]


License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
