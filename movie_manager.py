# movie_manager.py

class Movie:
    def __init__(self, movie_id, title, director, year, genre):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    
    def __str__(self):
        return f"ID: {self.movie_id}, Title: {self.title}, Director: {self.director}, Year: {self.year}, Genre: {self.genre}"


class MovieManager:
    def __init__(self):
        self.movies = {}  # Stores movies as {movie_id: Movie_object}
    
    def add_movie(self, movie_id, title, director, year, genre):
        # Check if ID already exists
        if movie_id in self.movies:
            print("Error: Movie ID already exists!")
            return False
        
        # Validate year is an integer
        if not isinstance(year, int):
            print("Error: Release year must be a number!")
            return False
        
        # Add the movie
        self.movies[movie_id] = Movie(movie_id, title, director, year, genre)
        print("Movie added successfully!")
        return True
    
    def view_all_movies(self):
        if not self.movies:
            print("No movies in the collection.")
            return
        
        print("\n--- All Movies ---")
        for movie in self.movies.values():
            print(movie)
    
    def search_movie(self, title):
        found_movies = []
        for movie in self.movies.values():
            if title.lower() in movie.title.lower():
                found_movies.append(movie)
        
        if not found_movies:
            print("No matching movies found.")
        else:
            print("\n--- Search Results ---")
            for movie in found_movies:
                print(movie)
    
    def update_movie(self, movie_id, **kwargs):
        if movie_id not in self.movies:
            print("Error: Movie ID not found!")
            return False
        
        movie = self.movies[movie_id]
        for key, value in kwargs.items():
            if hasattr(movie, key):
                setattr(movie, key, value)
            else:
                print(f"Warning: '{key}' is not a valid field. Skipping.")
        
        print("Movie updated successfully!")
        return True
    
    def delete_movie(self, movie_id):
        if movie_id not in self.movies:
            print("Error: Movie ID not found!")
            return False
        
        del self.movies[movie_id]
        print("Movie deleted successfully!")
        return True


def display_menu():
    print("\n==== Movie Collection Manager ====")
    print("1. Add a new movie")
    print("2. View all movies")
    print("3. Search movies by title")
    print("4. Update a movie")
    print("5. Delete a movie")
    print("6. Exit")


def main():
    manager = MovieManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Add New Movie ---")
            movie_id = input("Enter movie ID: ").strip()
            title = input("Enter movie title: ").strip()
            director = input("Enter director: ").strip()
            try:
                year = int(input("Enter release year: ").strip())
            except ValueError:
                print("Invalid year! Must be a number.")
                continue
            genre = input("Enter genre: ").strip()
            manager.add_movie(movie_id, title, director, year, genre)
        
        elif choice == "2":
            manager.view_all_movies()
        
        elif choice == "3":
            title = input("Enter movie title to search: ").strip()
            manager.search_movie(title)
        
        elif choice == "4":
            print("\n--- Update Movie ---")
            movie_id = input("Enter movie ID to update: ").strip()
            if movie_id not in manager.movies:
                print("Movie not found!")
                continue
            
            print("Leave blank to skip updating a field.")
            title = input("New title: ").strip()
            director = input("New director: ").strip()
            year = input("New year: ").strip()
            genre = input("New genre: ").strip()
            
            updates = {}
            if title: updates["title"] = title
            if director: updates["director"] = director
            if year:
                try:
                    updates["year"] = int(year)
                except ValueError:
                    print("Invalid year! Skipping update.")
            if genre: updates["genre"] = genre
            
            if updates:
                manager.update_movie(movie_id, **updates)
            else:
                print("No updates made.")
        
        elif choice == "5":
            movie_id = input("Enter movie ID to delete: ").strip()
            manager.delete_movie(movie_id)
        
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
