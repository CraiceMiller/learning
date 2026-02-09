videogames = ['Hollow night', 'Banjo & Kazzoi', 'Megaman', 'Proffesor Layton']
animes =     ['Ranma 1/2', 'Nazo no kanojo X', 'Nichijou', 'Azumanga', 'Lucky Star']
webtoons =   ['Marionetta', 'Tenager Mercenary', 'My name is Death']

likes = [videogames, animes, webtoons]

for i in likes[1]:
    print(i, end=', ')
print('\n')

for i in likes:
    for x in i:
        print(x, end=' ')
    print()
