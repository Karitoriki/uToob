import requests


def get_token() -> str:
    return requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "client_credentials"
        },
        headers={
            "Authorization": "Basic ZDMyNDBkYzllMjUwNDcwYjk4NjZlODJlMDkwZDVhN2M6NGE3MmQ4YzQwNTRkNGM4MDk5M2E5OGEyMWRiMzE5NzU="
        }
    ).json()["access_token"]


def get_track(token: str, title: str, artist: str):
    endpoint = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": f"track:{title} artist:{artist}",
        "type": "track"
    }
    print("Searching...")
    response = requests.get(
        endpoint,
        headers=headers,
        params=params).json()
    print(f"Found {len(response['tracks']['items'])} Tracks")
    for trackI in range(len(response['tracks']['items'])):
        track = response['tracks']['items'][trackI]
        titleSpot = track['name']
        artistSpot = ', '.join([track['artists'][art]['name']
                                for art in range(len(track['artists']))])
        print(f"{trackI}) {titleSpot} - {artistSpot}")
    
    return response["tracks"]["items"][int(input("Choose your track: "))] if len(response["tracks"]["items"]) != 0 else None

    # Get the album name and cover
    # album_name = track["album"]["name"]
    # album_cover_url = track["album"]["images"][0]["url"]
    # release_date = track['album']['release_date'][:-6]
    # album_artist = track['album']['artists'][0]['name']


def download_cover(image_url: str) -> bytes:
    return requests.get(image_url).content


if __name__ == "__main__":
    print("")
