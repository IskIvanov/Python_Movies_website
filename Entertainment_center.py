import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    " ",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


batman = media.Movie("The dark knight",
                    "Batman storyline",
                    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

lala_land = media.Movie("LA LA Land",
                    "Story of love and life",
                    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

lala_land = media.Movie("LA LA Land",
                    "Story of love and life",
                    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                    "https://www.youtube.com/watch?v=0pdqf4P9MB8")
the_avangers = media.Movie("The Avangers",
                            "",
                            "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                            "https://www.youtube.com/watch?v=eOrNdBpGMv8")
movie = [toy_story,avatar,batman,lala_land]
fresh_tomatoes.open_movies_page(movie)
