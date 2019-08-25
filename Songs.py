database = open("music.txt")
data = (database.read()).split("\n")
artists = []
song = []
link = []
genre = []
for i in data:
    information=i.split('\t')
    artists.append(information[0])
    song.append(information[1])
    link.append(information[2])
    genre.append(information[3])
'''print(artists)
print(song)
print(link)
print(genre)'''

