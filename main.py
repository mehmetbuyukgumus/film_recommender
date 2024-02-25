import streamlit as st
from recommendation_system.recommandation import film_recommendation
from film_infos.get_film_info import get_film_dataframe

main_data = get_film_dataframe()
recommended_data = film_recommendation(None)


def display_movie_card(title, overview, poster):
    # Kartları bir butonla oluştur
    if st.button(title):
        recommended_film = film_recommendation(title)
        st.write(f"{recommended_film['title'][1]}")
        st.write(f"{recommended_film['overview'][1]}")
        st.image(f"{recommended_film['poster'][1]}")


def main():
    st.title("Film Recommender")

    for movie, overview, poster in zip(main_data["title"], main_data["description"], main_data["poster"]):
        display_movie_card(movie, overview, poster)


if __name__ == "__main__":
    main()
