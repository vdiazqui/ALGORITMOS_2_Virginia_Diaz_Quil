from enum import Enum
from song import Song

# Definimos la enumeración para los géneros de las canciones
class Genre(Enum):
    ROCK = "ROCK"
    POP = "POP"
    EDM = "EDM"
    COUNTRY = "COUNTRY"

# Definimos la clase para representar una canción
class Song:
    def __init__(self, name, artist, release_date, duration):
        # Verificamos el tipo y valor de cada parámetro del constructor
        if not isinstance(name, str):
            raise ValueError("Nombre inválido")
        if not isinstance(artist, str):
            raise ValueError("Artista inválido")
        if not isinstance(release_date, str):
            raise ValueError("Fecha de lanzamiento inválida")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duración inválida")

        # Asignamos los parámetros a los atributos de la canción
        self.name = name
        self.artist = artist
        self.release_date = release_date
        self.duration = duration
        self.genres = set()  # Conjunto para almacenar los géneros de la canción

    # Método para añadir un género a la canción
    def add_genre(self, genre):
        if not isinstance(genre, Genre):  # Verificamos si el género es una instancia de la enumeración Genre
            raise ValueError("Género inválido")
        self.genres.add(genre)

    # Método para comparar dos canciones y determinar si son iguales
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self.name == other.name and
                self.artist == other.artist and
                self.release_date == other.release_date)

    # Método para representar una canción como una cadena de texto
    def __str__(self):
        return f"{self.artist} tocando {self.name} durante {self.duration} segundos."

# Definimos la función principal para realizar pruebas
def main():
    # Pruebas de la enumeración Genre
    print("=================================================================.")
    print("Test Case 1: Check Class GENRE - Name.")
    print("=================================================================.")

    if isinstance(Genre.ROCK, Genre):
        print("Test PASS. Se ha configurado correctamente el enum para ROCK.")
    else:
        print("Test FAIL. Comprueba el método __init__().")

    if isinstance(Genre.POP, Genre):
        print("Test PASS. Se ha configurado correctamente el enum para POP.")
    else:
        print("Test FAIL. Comprueba el método __init__().")

    if isinstance(Genre.EDM, Genre):
        print("Test PASS. Se ha configurado correctamente el enum para EDM.")
    else:
        print("Test FAIL. Comprueba el método __init__().")

    if isinstance(Genre.COUNTRY, Genre):
        print("Test PASS. Se ha configurado correctamente el enum para COUNTRY.")
    else:
        print("Test FAIL. Comprueba el método __init__().")

    # Pruebas de la clase Song
    print("=================================================================.")
    print("Test Case 2: Check Class Song - Name.")
    print("=================================================================.")

    # Creamos objetos de canción
    song1 = Song("Canción 1", "Artista 1", "2023-01-01", 180)
    song2 = Song("Canción 2", "Artista 2", "2023-01-02", 200)
    song3 = Song("Canción 1", "Artista 1", "2023-01-01", 180)

    # Agregamos géneros a las canciones
    song1.add_genre(Genre.ROCK)
    song1.add_genre(Genre.POP)
    song2.add_genre(Genre.EDM)
    song3.add_genre(Genre.COUNTRY)

    # Pruebas del método __eq__()
    if song1 == song3:
        print("Test PASS. Las dos canciones son iguales.")
    else:
        print("Test FAIL. Las dos canciones no son iguales.")

    if song1 != song2:
        print("Test PASS. Las dos canciones no son iguales.")
    else:
        print("Test FAIL. Las dos canciones son iguales.")

    # Pruebas del método __str__()
    print(song1)
    print(song2)
    print(song3)
    print("hello")
# Ejecutamos la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
