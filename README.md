# SmartMenu — AI-Powered Menu Recommendation System

## Summary
Building AI course project: SmartMenu is an AI-based system that recommends dishes to restaurant customers by analyzing preferences, dietary needs, and past orders. A simple, low-cost solution for small restaurants to improve customer experience.

---

## Background
Small restaurants often lack the resources to provide personalized menu suggestions like large chains do. Customers may be unsure what to order or unaware of suitable options. SmartMenu solves this by using basic customer data and simple machine learning to recommend dishes tailored to taste, budget, and dietary restrictions. Motivation: make ordering easier and improve customer satisfaction.

---

## How it is used
Context: restaurants, cafés, food trucks, canteens.  
Users: customers receive recommendations; restaurant staff use insights for menu planning.  
Example: A customer selects preferences (spicy/mild, vegan, low-cost, favorite ingredients). The system recommends 3–5 dishes that fit their profile.

---

## Data sources & AI methods

### **Data sources**
- Menu database (dish, ingredients, price, category)
- Customer preference input (spicy level, dietary rules, disliked ingredients)
- Historical orders (optional for advanced version)

### **AI/ML methods**
- Simple rule-based filtering (vegan, allergies, price range)
- Content-based recommendation system using:
  - Bag-of-words for ingredients
  - Cosine similarity for matching dishes to preferences
- Optional ML:
  - Classification model predicting “likelihood of order” based on historical data

This project intentionally stays simple for beginners.

---

## Challenges & limitations
- Limited data for new restaurants → weaker predictions.
- Dietary restrictions can be complex; must avoid harmful suggestions.
- Language barriers if menu items are not standardized.
- Accuracy depends on the quality of ingredient tagging.

---

## What next / Future improvements
- Add NLP to understand free-text customer requests (e.g., “I want something light and spicy”).  
- Integrate allergy detection and warnings.  
- Connect to a POS (Point-of-Sale) system for real-time learning.  
- Add reinforcement learning to optimize recommendations based on user feedback.

---

## Implementation roadmap (simple)
1. Build a small menu dataset (CSV/JSON).  
2. Create a Python recommendation engine using sklearn.  
3. Add a simple UI (web or mobile).  
4. Test with customers and collect feedback.

---

## Acknowledgments
Inspired by restaurant recommendation systems, open-source tutorials, and the Building AI course examples. Thanks to public datasets and Python ML libraries such as scikit-learn and pandas.



