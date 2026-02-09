from dataclasses import dataclass

@dataclass(kw_only=True)
class Song:
    title:str
    artist:str
    duration_seconds:int


class Tracking:
    def __init__(self,songs:list[Song]) -> None:
        self._songs=songs


def main()->None:
    songs_list:list[Song]=[
        Song(title="Fallen Angel",artist="Aimee B",duration_seconds=256),
        Song(title="Confessions of a Rotten girl",artist="Hatsune Miku",duration_seconds=197)

    ]

    print(songs_list)
    print()
    song1:Song=Song(title="Fallen Angel",artist="Aimee B",duration_seconds=256)
    song2:Song=Song(title="Senbozakura",artist="Hatsune Miku",duration_seconds=243)
    print(f"Descirption {song1 == song2}")

if __name__ =='__main__':
    main()