
from imdb import Cinemagoer
import pandas as pd

# create an instance of the Cinemagoer class
ia = Cinemagoer()








# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    pirates_of_caribbean = ia.search_movie("Herr Der Ringe" , 5)
    movie_data = []
    for result in pirates_of_caribbean:
        movie_id = result.movieID
        movie = ia.get_movie(movie_id)
        title = movie.get('title')
        year = movie.get('year')
        genres = movie.get('genres')
        votes = movie.get('votes')
        director = movie.get('director')[0]['name'] if movie.get('director') else None
        writers = [writer.get('name') for writer in movie.get('writer')] if movie.get('writer') else None
        cast = [actor['name'] for actor in movie.get('cast')] if movie.get('cast') else None
        plot_outline = movie.get('plot outline')
        distributors = [distributor['name'] for distributor in movie.get('distributors')] if movie.get('distributors') else None

    movie_data.append({
            'Title': title,
            'Year': year,
            'Genres': genres,
            'Votes': votes,
            'Director': director
            # 'Cast': cast,
            # 'Plot Outline': plot_outline,
            # 'Distributor': distributor
        })


    df = pd.DataFrame(movie_data)
    print(df)



