import movie
import fresh_tomatoes
import urllib  # for using urlopen function
import ast     # for converting string into a dictionary


''' this function takes movie's Id as an argument and
    returns it's details in dictionary format. '''


def getMovieDetail(id):
    connection = urllib.urlopen("https://api.themoviedb.org/3/movie/"+id+"?api_key=fad4cc55173a7da4b7b2aac1142fc037")  # opening url
    output = connection.read()        # reading url
    value = ast.literal_eval(output)  # converting string into dictionary
    connection.close()                # closing url connection
    return value


# sending Ids of films to the funtion which return it's details
value = getMovieDetail('1726')
IronMan= movie.Movie(value.get('original_title'), value.get('overview'), value.get('poster_path'),
                 "https://www.youtube.com/watch?v=8hYlB38asDY",
                 value.get('release_date'), value.get('vote_average'))
value = getMovieDetail('550')
FightClub= movie.Movie(value.get('original_title'), value.get('overview'), value.get('poster_path'),
                 "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                 value.get('release_date'), value.get('vote_average'))


# creating list of movies
movies = [IronMan,FightClub]

# opening movie page
fresh_tomatoes.open_movies_page(movies)
