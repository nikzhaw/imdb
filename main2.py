
from imdb import Cinemagoer

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


    pirates_of_caribbean = ia.search_movie("Herr Der Ringe")
    movie_data = []
    for result in pirates_of_caribbean:
        movie_id = result.movieID
        movie = ia.get_movie(movie_id)
        title = movie.get('title')
        rating = movie.get('rating')
        runtime = movie.get('runtime')
        # Weitere gewünschte Informationen können hier abgerufen werden

        movie_data.append({'Title': title, 'Rating': rating, 'Runtime': runtime})

    print(movie_data)


    pirates_of_caribbean = ia.search_movie("Jonny Depp Boat")

    for result in pirates_of_caribbean:
        print(result)





    results = ia.search_keyword('Zauberer')

    for result in results:
        print(result)

    people = ia.search_person('Herr der Ringe')
#    for person in people:
#       print(person.personID, person['name'])


    # get a movie
    movie = ia.get_movie('0133093')


    language = movie.guessLanguage()





    print(language)


    info = movie.get_current_info()



    print(info[2])




    xml = movie.summary()

    print(xml)


    # print the names of the directors of the movie
    print('Directors:')
    for director in movie['directors']:
        print(director['name'])

    # print the genres of the movie
    print('Genres:')
    for genre in movie['genres']:
        print(genre)

    # search for a person name
    people = ia.search_person('Mel Gibson')
    for person in people:
        print(person.personID, person['name'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
