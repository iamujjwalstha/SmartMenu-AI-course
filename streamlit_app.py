<<<<<<< HEAD
import streamlit as st
import pandas as pd
from recommender import SmartMenuRecommender

st.title("🍽️ SmartMenu – AI-powered dish recommendations")

recommender = SmartMenuRecommender("data/menu.csv")

st.write("Enter your preferences and let the AI recommend dishes!")

preferences = st.text_input("Your preferences (e.g., 'spicy chicken', 'vegan', 'light')")
max_price = st.number_input("Max price (€)", min_value=0.0, value=20.0)
dietary_exclude = st.text_input("Ingredients to avoid (comma-separated)")

if st.button("Get Recommendations"):
    exclude_list = [x.strip() for x in dietary_exclude.split(",")] if dietary_exclude else None
    results = recommender.recommend(
        preferences,
        top_n=5,
        max_price=max_price,
        dietary_exclude=exclude_list
    )

    if not results:
        st.warning("No matching dishes found.")
    else:
        for rec in results:
            st.subheader(rec["dish"])
            st.write(f"**Price:** €{rec['price']}")
            st.write(f"**Ingredients:** {rec['ingredients']}")
            st.write(f"**Description:** {rec['description']}")
            st.write(f"Similarity score: {round(rec['score'], 3)}")
            st.markdown("---")
=======
import streamlit as st
import pandas as pd
from recommender import SmartMenuRecommender

st.title("🍽️ SmartMenu – AI-powered dish recommendations")

recommender = SmartMenuRecommender("data/menu.csv")

st.write("Enter your preferences and let the AI recommend dishes!")

preferences = st.text_input("Your preferences (e.g., 'spicy chicken', 'vegan', 'light')")
max_price = st.number_input("Max price (€)", min_value=0.0, value=20.0)
dietary_exclude = st.text_input("Ingredients to avoid (comma-separated)")

if st.button("Get Recommendations"):
    exclude_list = [x.strip() for x in dietary_exclude.split(",")] if dietary_exclude else None
    results = recommender.recommend(
        preferences,
        top_n=5,
        max_price=max_price,
        dietary_exclude=exclude_list
    )

    if not results:
        st.warning("No matching dishes found.")
    else:
        for rec in results:
            st.subheader(rec["dish"])
            st.write(f"**Price:** €{rec['price']}")
            st.write(f"**Ingredients:** {rec['ingredients']}")
            st.write(f"**Description:** {rec['description']}")
            st.write(f"Similarity score: {round(rec['score'], 3)}")
            st.markdown("---")
>>>>>>> c231861 (Add streamlit_app.py)
