from gmusicapi import Mobileclient
import feedback
import configparser

RATING_NO_RATING = '0'
RATING_THUMBS_DOWN = '1'
RATING_THUMBS_UP = '5'
# API DOCS
# http://unofficial-google-music-api.readthedocs.io/en/latest/reference/mobileclient.html
# source code
# https://github.com/simon-weber/gmusicapi/blob/develop/gmusicapi/clients/mobileclient.py

def loadConfig(file="config.ini"):
    config = configparser.ConfigParser()
    config.read(file)
    return config


api = Mobileclient()
config = loadConfig()

logged_in = api.login(config['Credentials']["username"], config['Credentials']["password"], 'f8:a9:d0:0c:9d:82')
songs_list = api.get_all_songs()

songs_to_delete = []
# following is just for debugging
# wanted_keys = ['artist', 'title', 'id', 'rating']

for song in songs_list:
    if song['rating'] == RATING_THUMBS_DOWN:
        songs_to_delete.append(song)
        # songs_to_delete.append({k: song[k] for k in wanted_keys})

if not songs_to_delete:
    print("No songs to delete so far")
    exit(0)

# songs_to_delete = songs_to_delete[-2]
ids_to_delete = [song['id'] for song in songs_to_delete]
titles_to_delete = [song['title'] for song in songs_to_delete]

deleted = api.delete_songs(ids_to_delete)

# print(titles_to_delete)

feedbackText = ""
if (len(deleted) != len(songs_to_delete)):
    feedbackText = "Algo no ha anat bé"
else:
    feedbackText = "<h1>Deleted all %d songs:<h1><br>" % len(deleted)
    feedbackText += '<br>'.join(titles_to_delete)

print(feedbackText)

destEmail = config['Genericos']['DestinationEmail']
titleEmail = 'GMusicAPI batch feedback'

feedback.tryToSendEmail(destEmail, titleEmail, feedbackText)

'''
 'add_songs_to_playlist', 'add_store_track', 'change_song_metadata', 'create_playlist',
 'create_station', 'deauthorize_device', 'delete_playlist', 'delete_songs', 'delete_stations',
 'edit_playlist', 'get_album_info', 'get_all_playlists', 'get_all_songs',
 'get_all_stations', 'get_all_user_playlist_contents', 'get_artist_info', 'get_genres',
 'get_listen_now_items', 'get_listen_now_situations', 'get_promoted_songs', 'get_registered_devices',
 'get_shared_playlist_contents', 'get_station_tracks', 'get_stream_url', 'get_track_info',
 'increment_song_playcount', 'is_authenticated', 'is_subscribed', 'locale',
 'logger', 'login', 'logout', 'num_clients',
 'remove_entries_from_playlist', 'reorder_playlist_entry', 'search',
 'session', 'validate'] '''

'''
# to supress the unicodeerror
print("[")
for song in songs_to_delete:
    try:
        pprint.pprint(song)
    except UnicodeEncodeError as e:
        pass
    else:
        pass
    finally:
        pass
print("]")
'''
