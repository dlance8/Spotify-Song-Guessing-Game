from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, SongForm
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


app = Flask(__name__)
app.config['SECRET_KEY'] = '513a2ec6764d9811a3744e0e7319cc27'



@app.route("/")

@app.route("/home", methods=['GET', 'POST'])
def home():
    form = SongForm()
    if form.validate_on_submit():
        context_uri = form.link.data
        username = sys.argv[1]
        scope = 'user-read-private user-read-playback-state user-modify-playback-state'  # You can find other scopes here: https://developer.spotify.com/documentation/general/guides/scopes/
        client_id = 'ce89313ce56745faa9fba21be85de838'
        client_secret = 'b76fb4e1082040bb8ca8ac3076a9e58e'
        redirect_uri = 'http://www.google.com/'

        # Erase cache and prompt for user permission
        try:
            token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) # add scope
        except (AttributeError, JSONDecodeError):
            os.remove(f".cache-{username}")
            token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) # add scope

        # Create our spotify object with permissions
        spotifyObject = spotipy.Spotify(auth=token)

        #Get current device
        devices = spotifyObject.devices()
        print(json.dumps(devices, sort_keys=True, indent=4))
        deviceID = devices['devices'][0]['id']

        #Start playback
        spotifyObject.start_playback(deviceID, context_uri) #'spotify:playlist:4mqjYC4Ov8u0DrkCcsALbA'

    return render_template('home.html', form=form, form=)

@app.route("/register", methods=['GET', 'POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', title=Register, form=form)

if __name__ == '__main__':
    app.run(debug=True)
