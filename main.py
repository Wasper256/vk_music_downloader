from urllib.request import urlopen
import json


def download(my_id, token):
    address = 'https://api.vk.com/method/audio.get?owner_id={0}&access_token={1}'.format(my_id, token)
    data = urlopen(address)
    decoded_response = data.read().decode()
    final_data = json.loads(decoded_response)
    songs = final_data['response'][1:]
    song_url_all = []
    song_title_all = []
    c = 0
    for song in songs:
        song_artist = song['artist']
        song_title = song['title']
        song_url = song['url']
        song_url = list([song_url])
        song_url_all = song_url_all + song_url
        song_title = list([song_artist + song_title])
        song_title_all = song_title_all + song_title
        c += 1
    return song_url_all, song_title_all, c
# https://oauth.vk.com/authorize?client_id=5458340&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=8&response_type=token&v=5.57&state=123456
