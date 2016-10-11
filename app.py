# import the Flask class from the flask module
from flask import Flask, render_template
from params import my_id, token
from urllib.request import urlopen
import json

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    lst = download(my_id, token)
    print(lst[0])
    return render_template('downloadmusic.html', x="song_url_all", y="filename")


def download(my_id, token):
    address = 'https://api.vk.com/method/audio.get?owner_id={0}&access_token={1}'.format(my_id, token)
    data = urlopen(address)
    decoded_response = data.read().decode()
    final_data = json.loads(decoded_response)
    songs = final_data['response'][1:]
    song_title_all = []
    for song in songs:
        song_artist = song['artist']
        song_title = song['title']
        song_url = song['url']
#        song_url = list([song_url])
#        song_url_all = song_url_all + song_url
        song_title = list([song_artist + " " + song_title + "###" + song_url])
        song_title_all = song_title_all + song_title
    return song_title_all


if __name__ == '__main__':
    app.run(debug=True)
