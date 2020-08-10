from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

class RegistrationForm(FlaskForm):
    username = StringField('Username')
    gamecode = StringField('GameCode')
    submit = SubmitField('Join')

class SongForm(FlaskForm):
    link = StringField('Spotify Link:')
    submit = SubmitField('Go')

class MessageForm(FlaskForm):
    msg = StringField('Guess the artist/song')
