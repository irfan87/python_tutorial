def build_album(artist_name, album_title, tracks=None):
    album_dict = {'artist_name': artist_name, 'album_title': album_title}

    if tracks:
        album_dict['tracks'] = tracks

    for name, title in album_dict.items():
        print(f"{name.title()} - {title.title()}")

    return album_dict

artist_info_prompt = "Artist Name: "
album_info_prompt = "Album Title: "

while True:
    print("\nPlease insert your favorite artist information")
    print("Press 'q', or 'quit' or 'Quit' to exit from the program")

    artist_name = input(artist_info_prompt)

    if artist_name == 'q' or artist_name == 'quit' or artist_name == 'Quit':
        break

    album_title = input(album_info_prompt)

    if album_title == 'q' or album_title == 'quit' or album_title == 'Quit':
        break

    gather_artist_album_info = build_album(artist_name, album_title)

    print(gather_artist_album_info)

print("Bye bye =)")