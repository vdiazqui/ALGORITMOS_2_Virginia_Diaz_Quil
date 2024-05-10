from datetime import date

# Importamos la enumeración GENRE del ejercicio anterior
from enum import Enum

class GENRE(Enum):
    ROCK = "ROCK"
    POP = "POP"
    EDM = "EDM"
    COUNTRY = "COUNTRY"

class Song:
    def __init__(self, id, name, artist, duration, release_date, genres=[]):
        # Verificamos los tipos y valores de los parámetros
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID inválido")
        if not isinstance(name, str):
            raise ValueError("Nombre inválido")
        if not isinstance(artist, str):
            raise ValueError("Artista inválido")
        if not isinstance(duration, int) or duration <= 10:
            raise ValueError("Duración inválida")
        if not isinstance(release_date, date) or release_date > date.today():
            raise ValueError("Fecha de lanzamiento inválida")

        # Asignamos los parámetros a los atributos de la canción
        self.id = id
        self.name = name
        self.artist = artist
        self.duration = duration
        self.release_date = release_date
        self.genres = set(genres)  # Conjunto para almacenar los géneros de la canción

    # Métodos getters para obtener los atributos de la canción
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration

    def get_release_date(self):
        return self.release_date

    def get_genres(self):
        return list(self.genres)

    # Método para añadir un género a la canción
    def add_genre(self, genre):
        if not isinstance(genre, GENRE):
            raise ValueError("Género inválido")
        self.genres.add(genre)

    # Método para comparar dos canciones y determinar si son iguales
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self.id == other.id)

    # Método para representar una canción como una cadena de texto
    def __str__(self):
        return f"{self.artist} tocando {self.name} durante {self.duration} segundos."


def main():
    # Pruebas de la clase Song
    print("=================================================================.")
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))

    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))

    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")


# Verificamos si este módulo se está ejecutando directamente
if __name__ == "__main__":
    main()
