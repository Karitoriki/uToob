import requests
from Spotify import get_token

# Set the API endpoint and authorization headers
endpoint = "https://api.spotify.com/v1/search"
headers = {
    "Authorization": f"Bearer {get_token()}"
}

# Set the query parameters
params = {
    "q": "track:Eyeliner artist:Cxldface",
    "type": "track"
}

# Send the GET request
response = requests.get(endpoint, headers=headers, params=params)

# Parse the response
data = response.json()

# Get the first track from the search results
track = data["tracks"]["items"][0]

# Get the album name and cover
album_name = track["album"]["name"]
album_cover_url = track["album"]["images"][0]["url"]

print(f"Album name: {album_name}")
print(f"Album cover URL: {album_cover_url}")
