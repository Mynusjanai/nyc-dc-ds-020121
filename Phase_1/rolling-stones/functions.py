def most_popular_artist(our_data):
    
    counter_dict = {}
    for artist in all_artists(our_data): #loops over list of the artists for all albums includes repeats
        if artist in counter_dict: #checking to see if artist alread in counter_dict
            counter_dict[artist] += 1 #if it is, increment by 1
        else: #if 
            counter_dict[artist] = 1 #add artist to the dictionary
    maximum_albums = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_albums:
            artist_lists.append(keys) 
    return artist_lists


## find by name ##
def album_name(string, data):
        for albums in data:
            if albums['album'] == string:
                return albums
            else: 
                None
            
## find by rank ##
def album_rank(string, data):
        for albums in data:
            if albums['number'] == string:
                return albums
            else: 
                None
                
## find by year ##
def album_year(string, data):
    song_year = []
    for albums in data: 
        if albums['year'] == string:
            song_year.append(albums())
        else:
            None
    return albums

## find by years ##
def album_in_years(start, end, data):
    song_years = []
    for album in data:
        if int(album['year']) >= start and int(album['year']) <= end:
            song_years.append(album)
        else:
            None
    return song_years

## find by ranks ##
def album_in_ranks(start, end, data):
    song_ranks = []
    for album in data:
        if int(album['number']) >= start and int(album['number']) <= end:
            song_ranks.append(album)
        else:
            None
    return song_ranks
            
## all titles ##
def all_titles(data):
    album_titles = []
    for album in data:
        album_titles.append(album['album'])
    return album_titles

## all artists ##
def all_artists(data):
    album_artists = []
    for album in data:
        album_artists.append(album['artist'])
    return album_artists

## artists w/ most albums - come back to this ##
def top_artists(data):
    return max(all_artists(data), key = all_artists(data).count)

## most popular word ##
def top_word(songs):
    words = []
    for word in all_titles(songs):
        words.append(word.split())
    flat_list = [item for sublist in words for item in sublist]
    return max(flat_list, key = flat_list.count)