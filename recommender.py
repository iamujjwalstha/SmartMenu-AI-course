"""
recommender.py
Simple content-based recommender for the SmartMenu project.
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SmartMenuRecommender:
    def __init__(self, menu_csv_path):
        self.menu = pd.read_csv(menu_csv_path)
        # create a combined text field for matching
        self.menu['text'] = (self.menu['dish'].fillna('') + ' ' +
                             self.menu['ingredients'].fillna('') + ' ' +
                             self.menu['category'].fillna('') + ' ' +
                             self.menu['description'].fillna(''))
        self.vectorizer = CountVectorizer(stop_words='english')
        self.item_vectors = self.vectorizer.fit_transform(self.menu['text'])

    def recommend(self, preferences, top_n=5, max_price=None, dietary_exclude=None):
        """
        preferences: string describing user's preferences (e.g., "vegan, light, spicy")
        max_price: float or None
        dietary_exclude: list of ingredients to exclude (e.g., ['nuts','milk'])
        """
        # Basic filtering by price
        candidates = self.menu.copy()
        if max_price is not None:
            candidates = candidates[candidates['price'] <= float(max_price)]
        # Exclude dietary ingredients
        if dietary_exclude:
            def ok(row):
                ingredients = (row['ingredients'] or '').lower()
                return not any(d.lower() in ingredients for d in dietary_exclude)
            candidates = candidates[candidates.apply(ok, axis=1)]
        if candidates.empty:
            return []

        # Vectorize candidates
        candidate_texts = candidates['text']
        candidate_vecs = self.vectorizer.transform(candidate_texts)

        pref_vec = self.vectorizer.transform([preferences])
        sim = cosine_similarity(pref_vec, candidate_vecs).flatten()
        candidates = candidates.reset_index(drop=True)
        candidates['score'] = sim
        # Sort by score then by price (lower better)
        candidates = candidates.sort_values(['score','price'], ascending=[False, True])
        results = candidates.head(top_n)[['dish','ingredients','category','price','description','score']]
        return results.to_dict(orient='records')

if __name__ == "__main__":
    # quick demo
    r = SmartMenuRecommender('data/menu.csv')
    prefs = "spicy chicken, quick, savory"
    print("Recommendations for:", prefs)
    for rec in r.recommend(prefs, top_n=5):
        print(rec['dish'], "-", rec['score'])
