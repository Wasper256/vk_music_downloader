from urllib.request import urlopen
import json
from params import my_id, token

address = 'https://api.vk.com/method/audio.get?owner_id={0}&access_token={1}'.format(my_id, token)
data = urlopen(address)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)
songs = final_data['response'][1:]
for song in songs:
    song_artist = song['artist']
    song_title = song['title']
    song_url = song['url']
    cached_song = urlopen(song_url).read()
    filename = '{0}{1}.mp3'.format(song_artist, song_title)
    file = open(filename, 'wb')
    file.write(cached_song)
    file.close()
    print("Downloaded file {0}{1}.mp3 ".format(song_artist, song_title))

# https://oauth.vk.com/authorize?client_id=5458340&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=8&response_type=token&v=5.57&state=123456
