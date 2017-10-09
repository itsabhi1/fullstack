import backend
import media
toy_story= media.Movie("Toy Story", "A story of a boy whose toys come to Life", "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.poster_image_url)
avatar=media.Movie("Avatar","A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=xTWLBuTak6I")
#print(avatar.storyline)
#avatar.show_trailer()
movies=[toy_story, avatar]
backend.open_movies_page(movies)
