"""
app.py
Simple Flask API to serve recommendations.
POST /recommend
{
  "preferences": "vegan, light",
  "top_n": 3,
  "max_price": 10,
  "dietary_exclude": ["egg"]
}
"""
from flask import Flask, request, jsonify
from recommender import SmartMenuRecommender
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)
MENU_PATH = os.path.join(BASE_DIR, 'data', 'menu.csv')
recommender = SmartMenuRecommender(MENU_PATH)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json(force=True)
    preferences = data.get('preferences', '')
    top_n = int(data.get('top_n', 5))
    max_price = data.get('max_price', None)
    dietary_exclude = data.get('dietary_exclude', None)
    results = recommender.recommend(preferences, top_n=top_n, max_price=max_price, dietary_exclude=dietary_exclude)
    return jsonify({'recommendations': results})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status':'ok'})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
