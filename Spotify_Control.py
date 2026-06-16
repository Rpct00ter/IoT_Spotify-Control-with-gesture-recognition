import serial
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Reading from serial
PORT = "COM17"
BAUDRATE = 115200

ser = serial.Serial(PORT, BAUDRATE)

#Spotify Auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="###",
    client_secret="###",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))
print("Spotify Gesture Controller Started")

#Main
while True:
    try:
        line = ser.readline().decode().strip()
        print("RAW SERIAL:", repr(line))
        if line:
            print("Gesture:", line)

        #NEXT SONG
        if line == "NEXT":
            sp.next_track()
            print("Next song")

        #PREVIOUS SONG
        elif line == "PREVIOUS":
            sp.previous_track()
            print("Previous song")

        #PLAY/PAUSE
        elif line == "PLAY_PAUSE":

            playback = sp.current_playback()

            if playback and playback['is_playing']:
                sp.pause_playback()
                print("Pause")

            else:
                sp.start_playback()
                print("Play")
        time.sleep(0.1)

    except Exception as e:
        print("Error:", e)