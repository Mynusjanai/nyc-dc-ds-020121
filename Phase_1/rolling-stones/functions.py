## imports ##
import pandas as pd
import numpy as np
import requests as rq #interact with things & data that lives on the web
import json
import requests
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from zipfile import ZipFile



## style for notebook & plots - in matplotlib bookmark ##
style = 'dark_background'
plt.style.use(style)



## variables ##
json_data
all_genres = [album['genre'] for album in songs]
list_songs = [(lines[x].split('\t')) for x in range(len(lines))]
ranked_dict = ranking(list_songs)


## looping over a range
def 
for i in range(len(str)-1)



## example most popular artist function ##
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


## csv import ##
import csv
from collections import OrderedDict
with open('data.csv') as f:
    reader = csv.DictReader(f)  #create findby name()
    songs = [{k:v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace = True)]
songs



## lines split ##
[lines[x].split('\t') for x in range(len(lines))]



## lines ranking dictionary ##
def ranking(data):
    rank_items = []
    for line in data:
        rank_dict = {}
        rank_dict["Rank"]=line[0]
        rank_dict["Name"]=line[1]
        rank_dict["Artist"]=line[2]
        rank_dict["Year"]=line[3][:-1]
        rank_items.append(rank_dict)
    return rank_items



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
            song_year.append(albums)
        else:
            None
    return song_year



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
def top_word(data):
    words = []
    for word in all_titles(data):
        words.append(word.split())
    flat_list = [item for sublist in words for item in sublist]
    return max(flat_list, key = flat_list.count)



## decade histogram ##
import matplotlib.pyplot as plt
def decade_list(data):
    years = [(int(album['year'])//10*10) for album in data]
    return years
decade_list(data)

fig, ax = plt.subplots(figsize=(12,12))
plt.hist(decade_list(songs), bins = 20)
plt.show()



## alternate decade histogram ##
def decade_list(data):
    years = [(int(album['year'])//10*10) for album in data]
    return years
decade_list(data)

fig, ax = plt.subplots(figsize=(20, 10))
ax.hist(decade_list(songs), bins=7, color='darkslateblue')
ax.set_xlabel('Decades', size=30);
ax.set_ylabel('Albums', size=30)
ax.set_title('Album Histogram by Decade', size=50);
plt.show()                



## broken_out_genres ##
def broken_out_genre(data):
    genres = []
    for genre in all_genres(data):
        genres.append(genre.split(", "))
    flat_list_genre= []
    for sublist in genres:
        for item in sublist:
            flat_list_genre.append(item)
    return flat_list_genre



## histogram by genre ##
import matplotlib.pyplot as plt
def genre_list(data):
    for genre in data:
        genres = [album['genre'].split() for album in data]

    return genres
genre_list(data)

fig, ax = plt.subplots(figsize=(12,12))
ax.hist(genre_list(data), bins = 20)
;



## alternate histogram by genre (custom labels) ##
def genre_list(data):
    for genre in data:
        genres = [album['genre'] for album in data]

    return genres
genre_list(data)

fig, ax = plt.subplots(figsize=(20,10))
ax.set_xlabel('# of Genres', size=30);
ax.set_ylabel('Albums', size=30)
ax.set_title('Album Histogram by Genre', size=50);
ax.hist(genre_list(data), bins = 20, color='darkslateblue')
ax.set_xticks(genre_list(data), #size of ticks on x-axis
                        rotation = 60);



## ranking data cleaning from lines.txt
def ranking(data):
    rank_items = []
    for line in data:
        rank_dict = {}
        rank_dict["Rank"]=line[0]
        rank_dict["Name"]=line[1]
        rank_dict["Artist"]=line[2]
        rank_dict["Year"]=line[3][:-1]
        rank_items.append(rank_dict)
    return rank_items


## all titles
def all_titles(data):
    album_titles = []
    for album in data:
        album_titles.append(album['album'])
    return album_titles


## all artists
def all_artists(data):
    artist_list=[]
    for albums in data:
        artist_list.append(albums['artist'])
    return artist_list


## top artists from json_data
def top_artists(data):
    counter_dict = {}
    for tracks in all_artists(data): #loops over list of the artists for all albums includes repeats
        if tracks in counter_dict: #checking to see if artist alread in counter_dict
            counter_dict[tracks] += 1 #if it is, increment by 1
        else: #if 
            counter_dict[tracks] = 1 #add artist to the dictionary
    maximum_tracks = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_tracks:
            artist_lists.append(keys) 
    return artist_lists


## most songs
def most_songs(data):
    top_songs = [track['tracks', ] for track in json_data]
    
    return top_songs



## album with the most top songs ##
def albums_with_most_top_songs():
    artist_discog = []
    freq_dict = {}
    for name in ranked_dict:
        artist_discog.append(name['Name'])
    for x in artist_discog:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    for value in range(len(json_data)): 
        if json_data[value]['tracks'] == artist_discog: 
            freq_dict[x] += 1

    return freq_dict



## album with top songs
def albums_with_top_songs():
    artist_discog = []
    freq_dict = {}
    for name in ranked_dict:
        artist_discog.append(name['Name'])
    for x in artist_discog:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    for value in range(len(json_data)): 
        if json_data[value]['tracks'] == artist_discog: 
            freq_dict[x] += 1

    return freq_dict


## Songs that are on top albums
def songs_on_top_albums():
    featured_albums = []
    for items in ranked_dict.items():
        if values == json_data.values():
            featured_albums.append(keys)
    return featured_albums