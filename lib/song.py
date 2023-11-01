class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist 
        self.genre = genre
        self.add_to_song_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)



    @classmethod
    def add_to_song_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)


    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    









# nintey_nine_probs = Song("99 Problems", "Jay-Z", "Rap")
# the_earth_is_a = Song("The Earth is a cold dead thing", "Explosions in the Sky", "Instrumental")
# stay_humble = Song("Stay Humble", "Kendrick Lamar", "Rap")
# damn = Song("DAMN.", "Kendrick Lamar", "Rap")

# print(nintey_nine_probs.genre)
# print(stay_humble.genre)
# print(Song.count)
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)