
favorite_animes = ["Nazo no kanojo X","Nichijou","Re:Zero","Stain gate",""]
favorite_songs = ["Don\'t be shy","Senbonzakura","Royals","Hell\'s Greater Dad"]
items = [None, "apple",None,None,"banana"]


for index,anime in enumerate(favorite_animes,start=1):
    if (anime!=""):
        print(index,anime)
    if (anime=="Re:Zero"):
        print(f"{anime} was my first anime!!!")

for index, thing in enumerate(items):
    if (thing==None):
        items[index]="Strawberry"
print(items)

for anime,song in zip(favorite_animes,favorite_songs):
    print(f"{anime:<20}{song}")

for index, (anime,song )in enumerate(zip(favorite_animes,favorite_songs),start=1):
    print(index, f"{anime:<20}{song}")



#falsy thing: "",0
if all(favorite_animes):
    print("ok :)")
else:
    print("no ok >:(")