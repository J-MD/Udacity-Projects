import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Movie about Toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "Marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#avatar.show_trailer()

the_avengers = media.Movie("The Avengers",
                        "Super hero movie 1",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8")

the_avengers2 = media.Movie("Avengers: Age of Ultron",
                        "Super hero movie 2",
                        "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                        "https://www.youtube.com/watch?v=tmeOjFno6Do")
the_avengers3 = media.Movie("Avengers: Infinity War",
                        "Super hero movie 3/",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Avengers_Infinity_War.jpg/220px-Avengers_Infinity_War.jpg",
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

movies = [toy_story, avatar, the_avengers, the_avengers2, the_avengers3]

#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
