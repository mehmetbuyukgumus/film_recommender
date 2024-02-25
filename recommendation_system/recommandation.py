from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from film_infos.get_film_info import get_film_dataframe
import pandas as pd


def film_recommendation(movie):
    given_movie = movie
    if movie is not None:
        main_data = get_film_dataframe()

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(main_data["description"])

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        indices = pd.Series(main_data.index, index=main_data["title"])
        movie_index = indices[given_movie]

        similarity_scores = pd.DataFrame(cosine_sim[movie_index],
                                         columns=["score"])
        movie_indices = similarity_scores.sort_values("score", ascending=False)[1:6].index

        recommended_film = pd.DataFrame()
        recommended_film["title"] = main_data["title"].iloc[movie_indices]
        recommended_film["overview"] = main_data["description"].iloc[movie_indices]
        recommended_film["poster"] = main_data["poster"].iloc[movie_indices]
        return recommended_film
    return pd.DataFrame()
