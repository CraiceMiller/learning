from types import UnionType
from typing import Any


class TrackingSong:
    Storaging_Songs:list[dict]=[]
    Amount_Songs:int=0


    def __init__(self,title:str,
                 artist:str,
                 duration_seconds:int) -> None:
        self._title=title
        self._artist=artist
        self._duration=duration_seconds

        self.Storaging_Songs.append(self.__dict__)
        TrackingSong.Amount_Songs += 1

    #str 
    def __str__(self) -> str:
        return f'{self._title} by {self._artist}'
    
    def __repr__(self) -> str:
        return f"Track(title='[{self._title}]', artist='[{self._artist}]', duration_seconds=[{self._duration}])"

    def __getitem__(self,key:str)->str:
        if key == 'title':
            return self._title
        if key == 'artist':
            return self._artist
        if key == 'duration':
            return str(self._duration)
        return 'N/A'
    
    def __format__(self, __format_spec: str) -> str:
        minutes = self._duration // 60 
        seconds = self._duration % 60 

        if __format_spec == "min_sec":
              return f" {minutes:02}: {seconds:02}"
        
        if __format_spec =="short":
            return f" {self._title} by {self._artist}"
        
        if __format_spec =="full":
            return f" Title of the song: {self._title}. Artist: {self._artist}. Duration: {minutes:02}: {seconds:02}"
        
        return 'Unkown format especifier...'
    
    #bool
    def __eq__(self, __value) -> bool:
        return self._artist == __value._artist
    
    def __lt__(self,__value)-> bool:
        return self._duration < __value._duration 
    
    def __gt__(self,__value)-> bool:
        return self._duration > __value._duration 
    
    #int
    def __add__(self,__value)-> int:
        return self._duration + __value._duration 
    
    #self
    def __or__(self, __value: Any):
        new_title:str=f"{self._title} & {__value._title}"
        new_artist:str=f"{self._artist} & {__value._artist}"
        new_duration:int=self._duration + self._duration
        return TrackingSong(title=new_title,artist=new_artist, duration_seconds=new_duration )
    
   
    
  

    
    



def main()->None:
    #testing my own class :3
    song1:TrackingSong=TrackingSong(title="Fallen Angel",artist="Aimee B",duration_seconds=256)
    song2:TrackingSong=TrackingSong(title="Senbozakura",artist="Hatsune Miku",duration_seconds=243)
    song3:TrackingSong=TrackingSong(title="Rude",artist="MAGIC! ",duration_seconds=206)
    song4:TrackingSong=TrackingSong(title="Confessions of a Rotten girl",artist="Hatsune Miku",duration_seconds=197)
    print(f"Total of son is {TrackingSong.Amount_Songs}")

    all_song:list[TrackingSong]=[song1,song2,song3,song4]


    print("Simple Description: {}".format(song3))
    print("Specific description: {}".format(repr(song3)))
    print(f'Title: {song2["title"]}')
    print(f"Full description: {song1:full}")

    print(f"Duration combined: {song1 + song2}")
    
    text1:str="The first song is longer than the second one"
    text2:str="The second song is longer than the first one"
    print(text1 if song1 > song2 else text2)
    print(text1 if song1 < song2 else text2)

    for s in all_song:
        if song2 == s:
            print(f"{song2._title} and {s._title} has the same singer:  '{song2._artist}' ")

    print()

    print("Description of the aviable songs")
    for songs,classes in zip(TrackingSong.Storaging_Songs,all_song):
        for key,value in songs.items():
            if key == "_duration":
                print(f"{key}: {classes:min_sec}")
                continue 
            if key =="Amount_Songs":
                continue
            print(f"{key}: {value}")
        print()

    full_album:TrackingSong=song1|song2|song3|song4
    print(f"{full_album:short}")
    print(f"the total of the duration is {full_album:min_sec}")
    print(f"Total of son is {TrackingSong.Amount_Songs}")







   

if __name__ =='__main__':
    main()