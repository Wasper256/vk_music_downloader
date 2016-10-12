# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from params import my_id, token
from urllib.request import urlopen
import json

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = "invalid name"
        else:
            return redirect(url_for('https://oauth.vk.com/authorize?client_id=5458340&display=page&redirect_uri=localhost:5000/downloadmusic&scope=8&response_type=token&v=5.57&state=123456'))
    return render_template('home.html', error=error)


@app.route('/downloadmusic')
def downloadmusic():
    lst = download(my_id, token)
    songstring = lst[0]
    songstring = str(songstring)
    newss = songstring.split("###", 2)
    print(newss[1])
    return render_template('downloadmusic.html', x=newss[1], y=newss[0])


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
