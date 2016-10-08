from urllib.request import urlopen
import json

address = 'https://api.vk.com/method/audio.get?owner_id=MY_ID&access_token=(тут мій токен)'
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
