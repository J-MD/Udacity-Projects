import media

# Creating Movie objects below. Movie class was imported from media.py.
the_avengers = media.Movie(
    "The Avengers",
    # PEP8 standards, I have to break the poster url's into several lines.
    "https://m.media-amazon.com/images/M/"
    "MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5Z"
    "GI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "Earth's mightiest heroes must come together and learn to fight as a team "
    "if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

the_avengers2 = media.Movie(
    "Avengers: Age of Ultron",
    "https://m.media-amazon.com/images/M/MV5BMTM4O"
    "GJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg"
    "@._V1_SY1000_SX675_AL_.jpg",
    "When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping "
    "program called Ultron, things go horribly wrong and it's up to Earth's mightiest "
    "heroes to stop the villainous Ultron from enacting his terrible plan.",
    "https://www.youtube.com/watch?v=tmeOjFno6Do")

the_avengers3 = media.Movie(
    "Avengers: Infinity War",
    "https://m.media-amazon.com/images/M/"
    "MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM"
    "@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "The Avengers and their allies must be willing to sacrifice all in an attempt to "
    "defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Storing created movies into an array.
# You can choose to store as many/few movies as you want in here.
# The movies stored in this array will be displayed on our webpage.
list = [the_avengers, the_avengers2, the_avengers3]
