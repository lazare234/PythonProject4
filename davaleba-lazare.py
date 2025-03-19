#davaleba1
# text = """ჯასურბეკ იახშიბოევის ქუჩაზე მცხოვრები
# კურიერის შაურმის მოლოდინში ველი"""
#
# with open('data.txt', 'w', encoding="utf-8") as file:
#     file.write(text)
#
# with open('data.txt', 'r', encoding="utf-8") as file:
#     lines = file.readlines()
#
#     line_number = 1
#     for line in lines:
#         words = line.split()
#         print(f"Line {line_number}: {len(words)} words")
#         line_number += 1

#davaleba2
class Movie:
    def __init__(self, title, genre, release_year, rating):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        if 0 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 0 and 5")

    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_release_year(self):
        return self.release_year

    def get_rating(self):
        return self.rating

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Released: {self.release_year}, Rating: {self.rating}"

class MovieDatabase:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            self.movies.append(movie)
        else:
            raise ValueError("Only Movie objects can be added")

    def display_all_movies(self):
        if not self.movies:
            print("No movies in the database.")
        for movie in self.movies:
            print(movie)


movie1 = Movie("Inception", "Sci-Fi", 2010, 4.8)
movie2 = Movie("The Dark Knight", "Action", 2008, 4.9)

movie_db = MovieDatabase()

movie_db.add_movie(movie1)
movie_db.add_movie(movie2)

movie_db.display_all_movies()