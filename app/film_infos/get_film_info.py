def get_film_dataframe():
    import pandas as pd
    import requests
    from film_titles.prep_film_name import film_titles
    import streamlit as st
    query_string = film_titles()
    query_string = query_string[0:20]
    film_title = []
    film_id = []
    film_description = []
    film_poster = []

    for film in query_string:
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {f"title": {film}}

        headers = {
            "Type": "get-movies-by-title",
            "X-RapidAPI-Key": st.secrets["API_KEY"],
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        data_title = response.json()
        if data_title["search_results"] != 0:
            film_title.append(data_title["movie_results"][0]["title"])
            film_id.append(data_title["movie_results"][0]["imdb_id"])

    for i in film_id:
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {f"movieid": {i}}

        headers = {
            "Type": "get-movie-details",
            "X-RapidAPI-Key": st.secrets["API_KEY"],
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        film_description.append(response.json()["description"])

    for images in film_id:
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {f"movieid": {images}}

        headers = {
            "Type": "get-movies-images-by-imdb",
            "X-RapidAPI-Key": st.secrets["API_KEY"],
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        film_poster.append(response.json()["poster"])

    film_df = pd.DataFrame()
    film_df["title"] = film_title
    film_df["description"] = film_description
    film_df["poster"] = film_poster
    return film_df
