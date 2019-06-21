# this programs was developed because I am a hardcore fans of blackpink..
# it will contains the song lists of this Korean girls band
# Note: Please don't laugh

# make a list of blackpink songs
blackpink_list_songs = []
print(blackpink_list_songs)

# append new blackpink's song
blackpink_list_songs.append('kill this love')
blackpink_list_songs.append('solo')

# sort all blackpink as alphabetical
blackpink_list_songs.sort()

# show all the blackpink songs as individual list
for index, blackpink_song in enumerate(blackpink_list_songs):
    print(index, blackpink_song.title())

# remove the unwanted blackpink song and insert the new song
del blackpink_list_songs[0]
blackpink_list_songs.remove('solo')

blackpink_list_songs.insert(0, 'kick it')
blackpink_list_songs.insert(1, 'kill this love')
blackpink_list_songs.insert(2, 'playing with fire')
blackpink_list_songs.insert(3, 'solo')
print("\n")

# reproduce all the blackpink songs as individual list
for index, blackpink_song in enumerate(sorted(blackpink_list_songs, reverse=True)):
    print(index, blackpink_song.title())

# show the size of all blackpink's song
blackpink_list_songs_length = len(blackpink_list_songs)
print(f"There are {blackpink_list_songs_length} blackpink's song in my list")

print(blackpink_list_songs)