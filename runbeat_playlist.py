import time
import spotipy
import re
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Authentication settings
print("Setting up authentication...")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri="https://github.com/",
    scope="user-library-read playlist-modify-public"
))

# User input (replace with desired values or use input)
profile_link = str(input("User profile link: "))
# Regex to extract the profile ID from the link
regex_pattern = r"user\/(.+?)(\?si=.+)?$"

# Using regex to find matches in the profile link
match = re.search(regex_pattern, profile_link)

# Extracting the profile ID from group 1 or raising an error if not found
if match:
    profile_id = match.group(1)
else:
    raise ValueError("No profile ID found in the provided link.")

cadence = int(input("Cadence: "))  # Example cadence
cadence_range = 5  # Increasing tolerance to 5 BPM

# New limits for music selection parameters
energy_min = 0.7
valence_min = 0.5
danceability_min = 0.5
loudness_min = -10
instrumentalness_max = 0.5
acousticness_max = 0.3

# Function to make Spotify API requests with rate limit handling
def make_spotify_request(func, *args, **kwargs):
    while True:
        try:
            return func(*args, **kwargs)
        except spotipy.exceptions.SpotifyException as e:
            if e.http_status == 429:
                retry_after = int(e.headers.get('Retry-After', 10))  # Default of 10 seconds
                print(f"Rate limit exceeded, waiting for {retry_after} seconds...")
                time.sleep(retry_after)
            else:
                raise

# Function to get playlists and songs from a specific Spotify profile
def get_playlists_from_profile(sp, profile_id):
    print(f"Getting playlists from profile: {profile_id}...")
    playlists = make_spotify_request(sp.user_playlists, profile_id)
    songs = []
    while playlists:
        for playlist in playlists['items']:
            print(f"Analyzing playlist: {playlist['name']}")
            tracks = make_spotify_request(sp.playlist_tracks, playlist['id'])
            for item in tracks['items']:
                if item['track']:  # Check if the track exists
                    songs.append(item['track']['id'])
        if playlists['next']:
            playlists = make_spotify_request(sp.next, playlists)
        else:
            playlists = None
    print(f"Total songs collected: {len(songs)}")
    return songs

# Main processing
songs = get_playlists_from_profile(sp, profile_id)
filtered_songs = []

for i in range(0, len(songs), 50):  # Process 50 songs at a time
    song_ids_chunk = songs[i:i+50]
    features_list = make_spotify_request(sp.audio_features, song_ids_chunk)
    for features in features_list:
        if features:
            # Parameter checks with expanded BPM tolerance
            tempo = int(features['tempo'])
            if ((tempo in range(cadence - cadence_range, cadence + cadence_range + 1)) or
                (tempo in range(2 * cadence - 2 * cadence_range, 2 * cadence + 2 * cadence_range + 1)) or
                (tempo in range(cadence // 2 - cadence_range // 2, cadence // 2 + cadence_range // 2 + 1))):
                # Check other criteria (may need adjustment)
                if (energy_min <= features['energy'] <= 1.0 and
                    valence_min <= features['valence'] <= 1.0 and
                    danceability_min <= features['danceability'] <= 1.0 and
                    features['loudness'] >= loudness_min and
                    features['instrumentalness'] <= instrumentalness_max and
                    features['acousticness'] <= acousticness_max):
                    filtered_songs.append(features['id'])

# Create a custom playlist
print("Creating a custom playlist on Spotify...")
playlist_name = f"Running Playlist for {profile_id} - {cadence} BPM"
created_playlist = make_spotify_request(sp.user_playlist_create, sp.current_user()['id'], playlist_name)
make_spotify_request(sp.playlist_add_items, created_playlist['id'], filtered_songs)

# Get and print the playlist link
playlist_link = created_playlist['external_urls']['spotify']
print(f"Playlist '{playlist_name}' created with {len(filtered_songs)} songs.")
print(f"Playlist Link: {playlist_link}")
