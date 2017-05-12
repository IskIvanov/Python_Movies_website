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

movie = [toy_story,avatar,batman,lala_land]
fresh_tomatoes.open_movies_page(movie)

breaking_bad = media.Shows("Breaking Bad",
                        "A story of desparate man",
                        "http://meetinthelobby.com/wp-content/uploads/2013/09/Breaking-Bad-Poster-Season-4-Large.jpg",
                        "https://www.youtube.com/watch?v=HhesaQXLuRY",
                        " ",
                        " ")

Game_of_Thrones = media.Shows("Game of Thrones",
                    "The game called life",
                    "https://upload.wikimedia.org/wikipedia/en/e/e8/Game_of_Thrones_Season_1.jpg",
                    "https://www.youtube.com/watch?v=iGp_N3Ir7Do",
                    " ",
                    " ")



TV_show = [breaking_bad,Game_of_Thrones]
fresh_tomatoes.open_movies_page(movie)
