# IoT_Spotify-Control-with-gesture-recognition
This project is an IoT system using Arduino Pro Nicla Vision to recognise gestures and use them to control spotify app.
The system uses an embedded AI model to recognize hand gestures in real time and control Spotify playback.

The AI model was trained using custom gesture datasets in Edge Impulse and deployed directly onto the Arduino Nicla Vision board. The board processes camera input locally and sends gesture commands to a Python application through Serial communication.

The Python application connects to the Spotify Web API and executes playback actions based on recognized gestures.

## Implemented Gestures

* Thumb Up → Next Song
* Thumb Down → Previous Song
* Palm → Play / Pause

## How It Works

1. Arduino Nicla Vision captures live camera frames.
2. The embedded AI model classifies hand gestures.
3. Recognized gestures are sent through Serial communication.
4. Python receives gesture commands.
5. Spotify API executes playback actions.

<img width="1890" height="725" alt="image" src="https://github.com/user-attachments/assets/14a84ae7-913c-4702-9ebe-1eba25912444" />

## Technologies Used

* Arduino Nicla Vision
* Edge Impulse
* TensorFlow Lite
* Python
* Spotify Web API
* PySerial
* Spotipy
