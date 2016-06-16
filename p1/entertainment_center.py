import fresh_tomatoes
import media

life_of_pi = media.Movie("Life of Pi",
                         "A boy stuck on a boat with wild animals",
                         "http://kidspiritonline.com/files/2012/11/life-of-pi-poster.jpg",
                         "https://www.youtube.com/watch?v=5GbXVo9DdZo")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


the_devil_wears_prada = media.Movie("The Devil Wears Prada",
                                    "A story of a journalist entering the fashion industry.",
                                    "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
                                    "https://www.youtube.com/watch?v=XTDSwAxlNhc")


# Creating array movies to store movie instances
movies = [life_of_pi, avatar, the_devil_wears_prada]
# Using fresh tomatoes function to open html page and passing movies array
fresh_tomatoes.open_movies_page(movies)
