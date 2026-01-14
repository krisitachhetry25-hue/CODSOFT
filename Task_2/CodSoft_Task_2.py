

movies = {
    "inception": "sci-fi",
    "interstellar": "sci-fi",
    "matrix": "sci-fi",
    "avengers": "action",
    "john wick": "action",
    "titanic": "romance",
    "the notebook": "romance",
    "forrest gump": "drama",
    "3 idiots": "drama",
    "pk": "drama",
    "dangal": "sports",
    "chhichhore": "drama",
    "bahubali": "action",
    "war": "action",
    "yeh jawaani hai deewani": "romance",
    "jab we met": "romance",
    "the pursuit of happiness":"drama",
    "phir hera pheri":"comedy",
    "graveyard of the fireflies":"drama",
    "laila majnu":"romance",
    "welcome":"comedy",
    "chak de india":"sports",
    "conjuring":"horror",
    "murder2":"thriller",
    "1920":"horror",
    "don't breathe":"thriller",
    "zathura-a space adventure":"sci-fi"
}




my_favmovie = input("Enter a movie you like to watch:  ").lower()

def recommend(my_favmovie):
    if my_favmovie not in movies:
        print("Sorry, the movie you are asking for is not found in our database.you can try for another one")
        return

    my_genre = movies[my_favmovie]
    print(f"\nBecause you like {my_favmovie.title()} ({my_genre}), you may also like:\n")

    for movie, genre in movies.items():
        if genre == my_genre and movie != my_favmovie:
            print("-", movie.title())


recommend(my_favmovie)
