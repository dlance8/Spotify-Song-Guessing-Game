# import os
# import sys
# import json
# import spotipy
# import webbrowser
# import spotipy.util as util
# from json.decoder import JSONDecodeError

# class StartPlayback(songObject):
#     def Start():
#     # Get the username from terminal
#     username = sys.argv[1]
#     scope = 'user-read-private user-read-playback-state user-modify-playback-state'  # You can find other scopes here: https://developer.spotify.com/documentation/general/guides/scopes/
#     client_id = 'ce89313ce56745faa9fba21be85de838'
#     client_secret = 'b76fb4e1082040bb8ca8ac3076a9e58e'
#     redirect_uri = 'http://www.google.com/'
#
#     # Erase cache and prompt for user permission
#     try:
#         token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) # add scope
#     except (AttributeError, JSONDecodeError):
#         os.remove(f".cache-{username}")
#         token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) # add scope
#
#     # Create our spotify object with permissions
#     spotifyObject = spotipy.Spotify(auth=token)
#
#     #Get current device
#     devices = spotifyObject.devices()
#     print(json.dumps(devices, sort_keys=True, indent=4))
#     deviceID = devices['devices'][0]['id']
#
#     #Start playback
#     spotifyObject.start_playback(deviceID, link) #'spotify:playlist:4mqjYC4Ov8u0DrkCcsALbA'


#playlist_uri = input("Enter a spotify uri:")
#spotifyObject.start_playback(deviceID, playlist_uri) #'spotify:playlist:4mqjYC4Ov8u0DrkCcsALbA'
