def film_titles():
    import pandas as pd

    data = pd.read_csv('datasets/movie.csv')
    data = data["title"]
    data = data.apply(lambda x: x.split("(")[0])
    return data
